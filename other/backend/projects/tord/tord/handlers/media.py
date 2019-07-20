#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import logging
import os
import random

from tord.handlers.base import BaseHandler
from tord.settings import settings


class ImageHandler(BaseHandler):
    
    def get(self):
        """return a random image"""
        image_dir = os.path.join(settings["root_path"], "files/images")
        images = os.listdir(image_dir)
        random_image_path = os.path.join(image_dir, random.choice(images))
        logging.info("return image path: {}".format(random_image_path))

        try:
            with open(random_image_path, "rb") as f:
                random_image = f.read()
        except Exception as e:
            logging.error("read image error: {}".format(e))
            self.write_error(500)
        
        self.set_header("Content-Type", "image/jpeg")
        self.write(random_image)
        self.write_success()


class VideoHandler(BaseHandler):

    def get(self):
        """return a video, not stream media"""
        video_dir = os.path.join(settings["root_path"], "files/videos")
        videos = os.listdir(video_dir)
        random_video_path = os.path.join(video_dir, random.choice(videos))
        logging.info("return video path: {}".format(random_video_path))

        try:
            with open(random_video_path, "rb", buffering=2048) as f:
                random_video = f.read()
        except Exception as e:
            logging.error("read video error: {}".format(e))
            self.write_error(500)
        
        self.set_header("Content-Type", "video/mp4")
        self.write(random_video)
        self.write_success()
