#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
入口运行文件
"""


from app import factory


app = factory.create_app(config_name="DEVELOPMENT")

if __name__ == "__main__":
    app.run()
