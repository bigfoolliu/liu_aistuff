#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from tord.handlers import base


class TestHandler(base.BaseHandler):

    def post(self):
        data = self.request.body
        print("body:", data, type(data))

        parameters = self.parse_query_arguments()
        print("parse_query_arguments:", parameters)

        name = self.get_argument("name")
        print("get_argument: ", name)

        body_arguments = self.get_body_arguments
        print("get_body_arguments: ", body_arguments, self.get_body_arguments("name"))

        query_arguments = self.request.query_arguments
        print("query_arguments: ", query_arguments, self.get_query_arguments("name"))

        self.write(data)
        self.finish()
