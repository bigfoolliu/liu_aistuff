#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Python实现简单的dns服务器
https://blog.csdn.net/trbbadboy/article/details/8093256?utm_source=blogxgwz9
"""


import socket as socketlib
import socketserver
import struct


class SinDNSQuery(object):
    """dns查询"""

    def __init__(self, data):
        i = 1
        self.name = ""
        while 1:
            d = ord(data[i])
            if d == 0:
                break
            if d < 32:
                self.name = self.name + "."
            else:
                self.name = self.name + chr(d)
            i += 1
        self.query_bytes = data[0:i+1]
        (self.type, self.classify) = struct.unpack(">HH", data[i+1:i+5])
        self.len = i+5
    
    def get_bytes(self):
        return self.query_bytes + struct.pack(">HH", self.type, self.classify)


class SinDNSAnswer(object):
    """dns应答rrs"""

    def __init__(self, ip):
        self.name = 49164
        self.type = 1
        self.classify = 1
        self.time_to_live = 190
        self.data_length = 4
        self.ip = ip
    
    def get_bytes(self):
        res = struct.unpack(">HHHLH", self.name, self.type, self.classify, self.time_to_live, self.data_length)
        s = self.ip.split(".")
        res = res + struct.pack("BBBB", int(s[0]), int(s[1]), int(s[2]), int(s[3]))
        return res


class SinDNSFrame(object):

    def __init__(self, data):
        (self.id, self.flags, self.quests, self.answers, self.author, self.addition) = struct.unpack(">HHHHHH", data[0:12])
        self.query = SinDNSQuery(data[12:])
    
    def get_name(self):
        return self.query.name
    
    def set_ip(self, ip):
        self.answer = SinDNSAnswer(ip)
        self.answers = 1
        self.flags = 33152
    
    def get_bytes(self):
        res = struct.pack(">HHHHHH", self.id, self.flags, self.quests, self.answers, self.author, self.addition)
        res = res + self.quests.get_bytes()
        if not self.answers == 0:
            res = res + self.answers.get_bytes()
        return res


class SinDNSServer(object):
    """dns server"""

    def __init__(self, port=53):
        SinDNSServer.name_map = {}
        self.port = port
    
    def add_name(self, name, ip):
        SinDNSServer.name_map[name] = ip
    
    def start(self):
        HOST, PORT = "0.0.0.0", self.port
        server = socketserver.UDPServer((HOST, PORT), SinDNSUdpHandler)
        server.serve_forever()


class SinDNSUdpHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        dns = SinDNSFrame(data)
        socket = self.request[1]
        name_map = SinDNSServer.name_map

        if dns.query.type == 1:
            name = dns.get_name()
            to_ip = None
            if_rom = "map"
            if name_map.__contains__(name):
                to_ip = name_map[name]
            elif name_map.__contains__("*"):
                to_ip = name_map["*"]
            else:
                try:
                    to_ip = socketlib.getaddrinfo(name, 0)[0][4][0]
                    if_rom = "sev"
                except Exception as e:
                    print("get ip failed: ", e)
            if to_ip:
                dns.set_ip(to_ip)
            print("{}:{}--->{}:{}".format(self.client_address[0], name, to_ip, if_rom))
            socket.sendto(dns.get_bytes(), self.client_address)
        else:
            socket.sendto(data, self.client_address)


if __name__ == "__main__":
    sev = SinDNSServer()
    sev.add_name("www.abc.com", "192.168.0.1")
    sev.add_name("www.xyz.com", "192.168.0.2")
    sev.start()
