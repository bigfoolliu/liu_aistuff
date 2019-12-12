#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import os
import tkinter
from tkinter import *

cur_dir_path = os.path.dirname(os.path.abspath(__file__))


class Interface(object):

    def __init__(self, master):
        self.master = master
        self.img_path = os.path.join(cur_dir_path, "./imgs/test.JPG")
        self.init_widgets()

    def init_widgets(self):
        display_button = Button(self.master, bg="green", image=self.img_path)
        display_button.pack(expand=1, fill=BOTH)

        button = Button(self.master, bg="yellow", text="搜索")
        button.bind("<Button-1>", self.search)  # 绑定单击事件
        button.pack(expand=1, side=BOTTOM, fill=X)

    def search(self, event):
        print("begin to search")


def main():
    tk = Tk()
    tk.title("beauty shower")
    tk.minsize(400, 300)
    tk.maxsize(800, 600)
    interface = Interface(tk)
    tk.mainloop()


if __name__ == '__main__':
    main()

# TODO:not done
