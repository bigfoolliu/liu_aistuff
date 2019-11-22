#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
接口返回实例测试文件
"""


from flask import Flask, jsonify
import yaml
from utils.code import ResponseCode, ResponseMessage
from utils.response import ResMsg


app = Flask(__name__)

with open("../config/msg.yaml", encoding="utf-8") as f:
    msg_conf = yaml.safe_load(f.read())
app.config.update(msg_conf)


@app.route("/", methods=["GET"])
def test():
    res = ResMsg()    
    test_dict = dict(name="liu", age=12)
    res.update(data=test_dict)
    return jsonify(res.data)


if __name__ == "__main__":
    app.run(debug=True)
