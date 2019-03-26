#!/usr/bin/env python
#!coding:utf-8


"""
使用flask框架来使用网络摄像头识别人脸
"""
import face_recognition
from flask import Flask, jsonify, request, redirect


# 允许上传的图片格式
ALLOWED_EXTENSIONS = {"png", "jpeg", "jpg", "gif"}


app = Flask(__name__)


def allowed_file(file_name):
    return "." in file_name and file_name.rsplit(".", 1)[1].lower in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_image():
    """上传图片"""
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if file and allowed_file(file.filename):
            return detect_faces_in_image(file)
    return """
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>Upload a picture and see if it's a picture of Obama!</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    """


def detect_faces_in_image(file_stream):
    """检测在图片中的人脸"""
    pass
