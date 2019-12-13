# -*- coding: utf-8 -*-

import tornado.web
import tornado.gen
import time
import json

from functools import wraps
import base64
from Crypto.Cipher import AES

import requests
import logging

from edge_box_api_gateway.settings import settings
from edge_box_api_gateway.model.userinfo import UserTicket, UserInfo
from edge_box_api_gateway.utils.misc import get_current_time_ms
from edge_box_api_gateway.driver.casbin import casbin


def encrypt(key, uid, timestamp):
    def uid2message(uid, timestamp):
        ret = "{}/{}/jx".format(uid, timestamp)
        aim_length = int(len(ret) / 16) * 16 + 16
        return ret + (" " * (aim_length - len(ret)))
    try:
        obj = AES.new(key, AES.MODE_CBC, 'default salt 16b')
        return obj.encrypt(uid2message(uid, timestamp))
    except TypeError:
        obj = AES.new(key.encode('utf-8'), AES.MODE_CBC, 'default salt 16b'.encode('utf-8'))
        return obj.encrypt(uid2message(uid, timestamp).encode('utf-8'))


def decrypt(key, message):
    def message2uid(text):
        if isinstance(text, bytes):
            text = str(text, encoding='utf-8')
        return tuple(text.strip().split("/"))
    try:
        obj = AES.new(key, AES.MODE_CBC, 'default salt 16b')
    except TypeError:
        obj = AES.new(key.encode('utf-8'), AES.MODE_CBC, 'default salt 16b'.encode('utf-8'))
    return message2uid(obj.decrypt(message))


def calc_ticket(uid, timestamp):
    key = settings["cookie_secret"]
    return encrypt(key, uid, timestamp)


class BaseHandler(tornado.web.RequestHandler):

    def get_current_uid(self):
        if settings["debug"]:
            return settings["debug_user"]
        return self.current_uid

    def set_current_uid(self):
        self.current_uid = None
        cookie = self.get_cookie(settings["login_cookie"])
        if cookie is None:
            return None
        t = base64.b64decode(cookie)
        uid, timestmap, token = decrypt(settings["cookie_secret"], t)
        if token != "jx":
            return False
        self.userinfo = UserInfo.get_user_by_id(uid)
        if self.userinfo.re_cookie:
            return False
        self.current_uid = uid
        return True

    def clear_login_cookies(self):
        self.clear_cookie(settings["login_cookie"])

    def set_login_cookie(self, uid):
        now = get_current_time_ms()
        tickets = UserTicket.get_ticket(uid)
        if len(tickets) == 0:
            ticket = UserTicket.new_ticket({
                "uid": uid,
                "ticket": calc_ticket(uid, now),
                "timestamp": now,
            })
        else:
            ticket = tickets[0]
        self.set_cookie(settings["login_cookie"], base64.b64encode(
            ticket.ticket), expires_days=1)

    def prepare(self):
        '''
           status_cookie:
            1.None 没有cookie
            2.True cookie有效
            3.False cookie失效 
        '''
        if not settings["debug"]:
            status_cookie = self.set_current_uid()
            url = self.request.uri.split('?')[0]
            if status_cookie is None:
                if not casbin.enforce("visitor", url, self.request.method):
                    return self.login_failed()
            else:
                uid = self.get_current_uid()
                if not status_cookie:
                    self.clear_login_cookies()
                    return self.login_failed()
                else:
                    if not casbin.enforce(self.userinfo.role, url, self.request.method):
                        return self.access_failed()

    def parse_json_body(self):
        try:
            if isinstance(self.request.body, bytes):
                data = str(self.request.body, encoding='utf-8')
            else:
                data = self.request.body
            if not data:
                return {}
            self.request_data = json.loads(data)
        except (KeyError, ValueError) as e:
            self.write_error(500, "bad json format: {}".format(str(e)))
            self.request_data = None
        return self.request_data

    def parse_query_arguments(self):
        ret = {}
        for k, v in self.request.query_arguments.items():
            if isinstance(v, list) and len(v) != 0:
                if isinstance(v[0], bytes):
                    ret[k] = str(v[0], encoding='utf-8')
                else:
                    ret[k] = v[0]
            else:
                ret[k] = v
        return ret

    def finish_request(self, body):
        self.write(json.dumps(body, sort_keys=True, separators=(',', ': ')))
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.finish()

    def write_success_json(self, data=None):
        self.set_status(200)
        if data is None:
            return self.finish_request({"desc": "success"})
        else:
            return self.finish_request({"desc": "success", "data": data})

    def login_failed(self):
        self.write_error(499, "bad login user: login failed")

    def access_failed(self):
        self.write_error(403, "you do not have permission to access this page")

    def write_error(self, status_code, desc, reason=None):
        result = {}
        reason = desc
        if reason:
            self.set_status(status_code, reason=reason)
        else:
            self.set_status(status_code)
        result['desc'] = desc
        self.finish_request(result)


class AsyncHandler(BaseHandler):

    def success(self, result=None):
        return 200, result

    def failed(self, status_code, result=None):
        return status_code, result

    def write_success(self, result):
        return self.write_success_json(result)

    @property
    def executor(self):
        return self.application.executor

    @tornado.gen.coroutine
    def async_worker(self, func, data):
        status, result = yield self.executor.submit(func, (data))
        if status == 200:
            return self.write_success(result)
        else:
            return self.write_error(status, result)

    def do_post(self, data):
        return self.failed(404, "no implement")

    def do_put(self, data):
        return self.failed(404, "no implement")

    def do_get(self, data):
        return self.failed(404, "no implement")

    def do_delete(self, data):
        return self.failed(404, "no implement")

    def post(self):
        data = self.parse_json_body()
        return self.async_worker(self.do_post, data)

    def put(self):
        data = self.parse_json_body()
        return self.async_worker(self.do_put, data)

    def get(self):
        data = self.parse_query_arguments()
        return self.async_worker(self.do_get, data)

    def delete(self):
        data = self.parse_query_arguments()
        return self.async_worker(self.do_delete, data)


class ProxyHandler(AsyncHandler):

    def post(self):
        self.do_post(None)
        return self.async_worker(self.do_proxy, requests.post)

    def put(self):
        self.do_put(None)
        return self.async_worker(self.do_proxy, requests.put)

    def get(self):
        self.do_get(None)
        return self.async_worker(self.do_proxy, requests.get)

    def delete(self):
        self.do_delete(None)
        return self.async_worker(self.do_proxy, requests.delete)

    def set_proxy_url(self, url):
        self.proxy_url = url

    def write_success(self, result):
        self.write_error(200, result)

    def write_error(self, status, result):
        self.set_status(status)
        self.write(result)
        self.finish()

    def do_proxy(self, func):
        try:
            url = self.proxy_url
        except:
            return self.failed(404, "not found proxy url")

        timeout = settings.get("proxy_timeout", 20)

        uid = self.current_uid
        if uid is not None:
            headers = {"user_id": uid, "user_name": UserInfo.get_user_by_id(uid).name}
        else:
            headers = {"user_id": "visitor", "user_name": "visitor"}

        try:
            query_args = self.parse_query_arguments()
            if self.request.body:
                res = func(url=url, data=self.request.body, headers=headers,
                           timeout=timeout, params=query_args)
            else:
                res = func(url=url, headers=headers, timeout=timeout, params=query_args)

            for k in res.headers:
                if k.lower() == "transfer-encoding" and res.headers[k].find("chunked") != -1:
                    continue
                self.set_header(k, res.headers[k])
            # send raw data with status_code, maybe rename func
            return self.failed(res.status_code, res.content)
        except Exception as e:
            self.clear()
            return self.failed(502, "proxy error: {}".format(e))


class ServiceProxyHandler(ProxyHandler):

    def initialize(self):
        self.service = None

    def post(self, url=""):
        self.set_proxy_url("{}{}".format(self.service, url))
        return self.async_worker(self.do_proxy, requests.post)

    def get(self, url=""):
        self.set_proxy_url("{}{}".format(self.service, url))
        return self.async_worker(self.do_proxy, requests.get)

    def put(self, url=""):
        self.set_proxy_url("{}{}".format(self.service, url))
        return self.async_worker(self.do_proxy, requests.put)

    def delete(self, url=""):
        self.set_proxy_url("{}{}".format(self.service, url))
        return self.async_worker(self.do_proxy, requests.delete)
