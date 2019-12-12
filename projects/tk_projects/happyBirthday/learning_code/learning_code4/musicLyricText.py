#!-*-coding:utf-8-*-
# !@Date: 2018/8/12 10:55
# !@Author: Liu Rui
# !@github: bigfoolliu


import tkinter
import os
import time


# 歌词文本框
class MusicLyricText(tkinter.Frame):
	def __init__(self, master):
		self.frame = tkinter.Frame(master)
		self.frame.pack(side=tkinter.TOP, fill=tkinter.Y)

		self.textLyric = tkinter.Text(self.frame, bg="#FFDEAD", height=50)
		self.textLyric.pack()
