#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu

"""
基础界面
"""
import tkinter


class Interface(tkinter.Frame):

    def __init__(self, master=None):
        """默认master设置为None,可以设置为其他顶层窗口的一个组件"""
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.init_widgets()
    
    def init_widgets(self):
        """初始化该frame上的一些GUI组件"""
        start_button = tkinter.Button(self, text="start")
        start_button.pack()
        pause_button = tkinter.Button(self, text="pause")
        pause_button.pack()
        stop_button = tkinter.Button(self, text="stop")
        stop_button.pack()

interface = Interface()
interface.mainloop()
