#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import base64
import json
import logging

import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def parse_json(self, raw_data):
        if raw_data == b"":
            return {}
        if isinstance(raw_data, bytes):
            try:
                data = str(raw_data, encoding="utf-8")
            except Exception:
                return {"data": str(base64.b64encode(raw_data), encoding="utf-8")}
        else:
            data = raw_data
        data = json.loads(data)
        return data

    def parse_json_body(self):
        try:
            self.request_data = self.parse_json(self.request.body)
        except (KeyError, ValueError) as e:
            self.write_error(500, "bad json format: {}".format(str(e)))
            self.request_data = None
        return self.request_data

    def finish_request(self, body):
        self.write(json.dumps(body, sort_keys=True, separators=(",", ": ")))
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.finish()

    def write_success_json(self, data=None):
        self.set_status(200)
        if data is None:
            return self.finish_request({"desc": "success"})
        else:
            return self.finish_request({"desc": "success", "data": data})

    def write_error(self, status_code, desc=None, reason=None, **kwargs):
        result = {}
        if reason:
            self.set_status(status_code, reason=reason)
        else:
            self.set_status(status_code)

        if desc is None and "exc_info" in kwargs:
            desc = str(kwargs["exc_info"][1])

        result['desc'] = desc
        self.finish_request(result)

    def get(self):
        raise NotImplementedError
    
    def post(self):
        raise NotImplementedError
    
    def write_success(self, reason=None):
        self.set_status(200, reason=reason)
        self.finish()
