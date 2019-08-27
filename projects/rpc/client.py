#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from xmlrpclib import ServerProxy            #导入xmlrpclib的包 

s = ServerProxy("http://172.171.5.205:8080") #定义xmlrpc客户端 
print(s.fun_add(2,3))
