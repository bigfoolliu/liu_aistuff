#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用Python实现redis的基本功能
http://charlesleifer.com/blog/building-a-simple-redis-server-with-python/


The server we'll be building will be able to respond to the following commands:
服务端会响应以下命令：

GET <key>
SET <key> <value>
DELETE <key>
FLUSH
MGET <key1> ... <keyn>
MSET <key1> <value1> ... <keyn> <valuen>


We'll support the following data-types as well:
支持以下几种数据类型：

Strings and Binary Data
Numbers
NULL
Arrays (which may be nested)
Dictionaries (which may be nested)
Error messages
"""

# 使用gevent来异步处理客户端的请求
from gevent import socket
from gevent.pool import Pool
from gevent.server import StreamServer

from collections import namedtuple
from io import BytesIO
from socket import error as socket_error


# We'll use exceptions to notify the connection-handling loop of problems.
class CommandError(Exception):
    pass


class Disconnect(Exception):
    pass


Error = namedtuple('Error', ('message',))


class ProtocolHandler(object):
    """协议处理"""
    def handle_request(self, socket_file):
        # Parse a request from the client into it's component parts.
        pass

    def write_response(self, socket_file, data):
        # Serialize the response data and send it to the client.
        pass


class Server(object):

    def __init__(self, host='127.0.0.1', port=31337, max_clients=64):
        self._pool = Pool(max_clients)
        self._server = StreamServer(
            (host, port),
            self.connection_handler,
            spawn=self._pool)

        self._protocol = ProtocolHandler()
        self._kv = {}

    def connection_handler(self, conn, address):
        # Convert "conn" (a socket object) into a file-like object.
        socket_file = conn.makefile('rwb')

        # Process client requests until client disconnects.
        while True:
            try:
                data = self._protocol.handle_request(socket_file)
            except Disconnect:
                break

            try:
                resp = self.get_response(data)
            except CommandError as exc:
                resp = Error(exc.args[0])

            self._protocol.write_response(socket_file, resp)

    def get_response(self, data):
        # Here we'll actually unpack the data sent by the client, execute the
        # command they specified, and pass back the return value.
        pass

    def run(self):
        self._server.serve_forever()
