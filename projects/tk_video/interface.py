#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu

"""
基础界面
"""
import tkinter
from tkinter import *


class Interface(object):

    def __init__(self):
        self.tk = tkinter.Tk()

        self.video_frame = tkinter.Frame(self.tk, relif=RIDGE, borderwidth=2)
        self.video_frame.pack(fill=BOTH, expand=1)


interface = Interface()
tkinter.mainloop()
