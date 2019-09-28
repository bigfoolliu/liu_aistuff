#!-*-coding:utf-8-*-
# !@Date: 2018/8/5 21:18
# !@Author: Liu Rui
# !@github: bigfoolliu


"""

tkinter模块 初识

"""

from tkinter import *

wiget = Label(None, text="最短的tkinter示例")
wiget.pack()
wiget.mainloop()


# 标签Label
import tkinter

# 建立顶层窗口类,容纳整个GUI程序
top = tkinter.Tk()

label = tkinter.Label(top, text="Hello, world!")  # 创建一个标签
label.pack()  # 打包放置标签
tkinter.mainloop()  # 进入主事件循环,及"服务器式"无限循环


# 按钮Button
import tkinter

top = tkinter.Tk()

quit_button = tkinter.Button(top, text="退出", command=top.quit)  # 需要一个对应的按钮命令
quit_button.pack()

tkinter.mainloop()


# 按钮和标签结合
import tkinter

top = tkinter.Tk()

hello = tkinter.Label(top, text="hello")
hello.pack()

# bg和fg分别设置按钮的背景色和前景色
quit_button = tkinter.Button(top, text="退出", command=top.quit, bg="red", fg="white")
# 水平填充
quit_button.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()


# # 按钮,标签和进度条组件结合
# # 进度条的滑块可以控制标签文字的大小
# import tkinter
#
#
# def resize(ev=None):
# 	"""
# 	控制标签大小
# 	:param ev:
# 	:return:
# 	"""
# 	label.config(font="Helvetica -%d bold" % scale.get())
#
#
# top = tkinter.Tk()
# top.geometry("500x250")  # 设置顶层窗口的大小,此处的乘号为x
#
# label = tkinter.Label(top, text="Hey,you.", font="Helvetica -12 bold")  # 标签文本默认字体大小设置为12
# label.pack(fill=tkinter.Y, expand=1)
#
# scale = tkinter.Scale(top, from_=10, to=100, orient=tkinter.HORIZONTAL, command=resize)
# scale.set(12)
# scale.pack(fill=tkinter.X, expand=1)
#
# quit_button = tkinter.Button(top, text="退出", command=top.quit, activeforeground="white", activebackground="red")
# quit_button.pack()
#
# tkinter.mainloop()


# # # 运用PFA的路灯指示牌GUI程序
# # from functools import partial as pto
# # from tkinter import  Tk, Button, X
# # from tkMessageBox import showinfo, showwarning  # 无tkMessageBox库
#
#
# # 目录树遍历工具
# # 从当前目录开始并提供文件列表,双击列表中的任意其他目录都会让该工具转向这个新的目录,同时
# # 用新目录中的文件列表替换原有的文件列表.
# import os
# from time import sleep
# from tkinter import *
#
#
# class DirList(object):
# 	"""
# 	定义一个列表类
# 	"""
# 	def __init__(self):
# 		"""
# 		初始化函数
# 		"""
# 		self.top = Tk()  # 创建一个TK类实例
#
# 		self.label = Label(self.top, text="Directory List V1.0")  # 定义版本标签
# 		self.label.pack()
#
# 		self.cwd = StringVar(self.top)
# 		self.dir1 = Label(self.top, fg="blue", font=("Helvetica", 12, "bold"))
# 		self.dir1.pack()
#
# 		self.dirfm = Frame(self.top)
# 		self.dirsb = Scrollbar(self.dirfm)
# 		self.dirsb.pack(side=RIGHT, fill=Y)
#
# 		# self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
# 		# self.dirs.bind("<Double-1>", self.setDirAndGo)  # 存在错误
# 		# self.
