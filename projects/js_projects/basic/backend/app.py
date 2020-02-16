#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from flask import Flask, Blueprint, current_app


app = Flask(__name__)


bp_test = Blueprint("test", "test", url_prefix="/test")


@bp_test.route("/ajax", methods=["GET"])
def ajax_test():
    # 设置响应头,
    return "ok", 200, [("Access-Control-Allow-Origin", "*"), ("Access-Control-Allow-Method", "POST,GET")]


@app.route("/", methods=["GET"])
def index():
    return "server is ready"


@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return current_app.send_static_file("./static/favicon.ico")


app.register_blueprint(bp_test)


if __name__ == '__main__':
    app.run()
