#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu

import logging
import os
import random
import base64

from tord.handlers.base import BaseHandler
from tord.settings import settings


class BooksHandler(BaseHandler):
    
    def get(self):
        self.write("book")
        self.write_success(reason="ok")
    
    def post(self):
        """use this to upload a file"""
        # path = self.request.path
        # host = self.request.host
        # uri = self.request.uri
        # query = self.request.query
        # headers = self.request.headers
        # body = self.request.body
        # remote_ip = self.request.remote_ip
        files = self.request.files
        # print("path:{}".format(path))
        # print("host:{}".format(host))
        # print("uri:{}".format(uri))
        # print("query:{}".format(query))
        # print("headers:{}".format(headers))
        # print("body:{}".format(body))
        # print("remote_ip:{}".format(remote_ip))
        print("files:{} type:{}".format(files, type(files)))

        for file in files:
            print(file, type(file), "\n")
        
        file1 = files["file1"]
        files_dir = os.path.join(settings["root_path"], "files")
        file1_bak_path = os.path.join(files_dir, file1[0]["filename"] + ".bak")
        with open(file1_bak_path, "w", encoding="utf-8") as f:
            f.write(file1[0]["body"].decode("utf-8"))
        
        self.write_success()
