#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu

"""
基础界面
"""
import tkinter


class PlayBottonInterface(object):

    def __init__(self, master):
        """默认master设置为None,可以设置为其他顶层窗口的一个组件"""
        self.master = master
        self.init_widgets()
    
    def init_widgets(self):
        """初始化该frame上的一些GUI组件"""
        frame = tkinter.Frame(self.master, height=400, width=300, background="yellow")
        frame.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)  # frame放置在底部

        start_button = tkinter.Button(frame, text="start")
        start_button.pack(side=tkinter.LEFT, expand=1, fill=tkinter.BOTH, padx=2)
        pause_button = tkinter.Button(frame, text="pause")
        pause_button.pack(side=tkinter.LEFT, expand=1, fill=tkinter.BOTH, padx=2)
        stop_button = tkinter.Button(frame, text="stop")
        stop_button.pack(side=tkinter.LEFT, expand=1, fill=tkinter.BOTH, padx=2)


class PlayScreenInterface(object):

    def __init__(self, master):
        self.master = master
        self.init_widgets()
    
    def init_widgets(self):
        frame = tkinter.Frame(self.master, background="green")
        frame.pack(side=tkinter.TOP, fill=tkinter.BOTH)


tk = tkinter.Tk()
tk.title("video player")
play_button_interface = PlayBottonInterface(tk)
play_screen_interface = PlayScreenInterface(tk)
tk.mainloop()
