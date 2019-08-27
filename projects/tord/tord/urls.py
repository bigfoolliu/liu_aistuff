#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from tord.handlers import index, media, upload, gocron

url_patterns = [
    (r"/", index.IndexHandler),
    (r"/books", upload.BooksHandler),
    (r"/images", media.ImageHandler),
    (r"/videos", media.VideoHandler),
    # (r"/async", async.AsyncDemoHandler),
    (r"/test", gocron.TestHandler),
]
