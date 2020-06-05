#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from flask import Blueprint


download_bp = Blueprint("download", __name__, url_prefix="/download")
