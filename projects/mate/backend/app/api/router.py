#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from app.api.upload import upload_bp
from app.api.download import download_bp


routers = [
    upload_bp,
    download_bp
]
