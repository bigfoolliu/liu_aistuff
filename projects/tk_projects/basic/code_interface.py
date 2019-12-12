#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu

"""
基础界面
"""
import tkinter


class SearchInterface(object):

    def __init__(self, master):
        """默认master设置为None,可以设置为其他顶层窗口的一个组件"""
        self.master = master
        self.init_widgets()
    
    def init_widgets(self):
        """初始化该frame上的一些GUI组件"""
        frame = tkinter.Frame(self.master, width=320, height=240, bg="green")
        frame.pack_propagate(0)  # 设置Frame的大小不改变
        frame.pack(expand=1)

        frame1 = tkinter.Frame(self.master, width=320, height=20, bg="yellow")
        frame1.pack_propagate(0)  # 设置Frame的大小不改变
        frame1.pack(expand=1)

        button = tkinter.Button(frame1, width=30, height=18, text="查询")
        button.bind("<Button-1>", self.search)  # 绑定单击事件
        button.bind("<Double-l>", self.double_click)  # 绑定双击事件
        button.pack(expand=1)
    
    def search(self, event):
        print("begin search...")
    
    def double_click(self, event):
        print("double click...")


tk = tkinter.Tk()
tk.title("code counter")
tk.geometry("400x300")  # 设置主窗口的大小
tk.resizable(0, 0)  # 设置主窗口的大小不可改变
search_interface = SearchInterface(tk)
tk.mainloop()
