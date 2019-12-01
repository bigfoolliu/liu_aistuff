#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
入口运行文件
"""


from app import factory
from app.api.services import ArticleAPI

app = factory.create_app(config_name="DEVELOPMENT")


# ------------------------测试单表服务-------------------------
# TODO:delete later
article_view = ArticleAPI.as_view("article_api")
app.add_url_rule("/article/", defaults={"key": None}, view_func=article_view, methods=["GET",])
app.add_url_rule("/article/", view_func=article_view, methods=["POST",])
app.add_url_rule("/article/<string:key>", view_func=article_view, methods=["GET", "PUT", "DELETE"])


if __name__ == "__main__":
    app.run()
