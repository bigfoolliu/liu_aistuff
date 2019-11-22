#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import random

from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")

# 开启CORS,使用资源的定位的方式，允许所有的/api/*下的路由都可以被任何人访问
cors = CORS(app, resources={"/api/*": {"origins": "*"}})


@app.route("/", defaults={"path": "."})
@app.route("/<path:path>")
def create_all(path):
    return render_template("index.html")


@app.route("/api/random")
def random_number():
    response = {
        "randomNumber": random.randint(1, 100)
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
