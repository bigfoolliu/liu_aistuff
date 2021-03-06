#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from tord.handlers import (block_test, gocron, index, media, upload)


url_patterns = [
    (r"/", index.IndexHandler),
    (r"/books", upload.BooksHandler),
    (r"/images", media.ImageHandler),
    (r"/videos", media.VideoHandler),
    # (r"/async/test", async_test.Handler),
    (r"/block/test", block_test.BlockHandler),
    # (r"/async/(?P<url>/.*)", async_demo.Handler),  # FIXME:
    (r"/test", gocron.TestHandler),
]
