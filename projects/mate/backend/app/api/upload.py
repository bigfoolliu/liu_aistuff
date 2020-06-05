#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from flask import Blueprint


upload_bp = Blueprint("upload",  __name__, url_prefix="/upload")


@upload_bp.route("/test", methods=["GET"])
def upload_test():
    """
    :return:
    """
    return "ok"
