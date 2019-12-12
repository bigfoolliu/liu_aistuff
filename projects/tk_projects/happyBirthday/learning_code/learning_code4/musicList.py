#!-*-coding:utf-8-*-
# !@Date: 2018/8/12 10:42
# !@Author: Liu Rui
# !@github: bigfoolliu


import tkinter
import os
import pygame


# 书写音乐列表，插入本地音乐歌名
class MusicList(tkinter.Frame):
	def __init__(self, master):
		self.frame = tkinter.Frame(master)
		self.frame.pack(side=tkinter.LEFT, fill=tkinter.Y)

		self.lv = tkinter.StringVar()
		self.listBox = tkinter.Listbox(self.frame, selectmode=tkinter.BROWSE, width=30, height=30, bg="#FFFACD",
									   listvariable=self.lv)
		self.listBox.pack()

		self.addMusicName()

		self.listBox.bind("<Double-Button-1>", self.playMusic)

	def playMusic(self, event):
		pygame.mixer.init()
		pygame.mixer.music.load(self.getCurrentMusicPath())
		pygame.mixer.music.play()

	def getCurrentMusicPath(self):
		path = r"E:\Python-1704\python\day15\homework\播放音乐器\music"
		# self.listBox.select_set(0)
		for item in range(self.listBox.size()):
			musicAbsPath = path + "\\" + self.listBox.get(item)
			if self.listBox.selection_includes(item):
				path = musicAbsPath
				# print("-----", path)
				return path

	# 添加音乐曲目
	def addMusicName(self):
		path = r"E:\Python-1704\python\day15\homework\播放音乐器\music"
		musicNameList = os.listdir(path)
		for musicName in musicNameList:
			path1 = os.path.join(path, musicName)
			path1list = os.path.splitext(path1)
			if path1list[-1] == ".mp3":
				self.listBox.insert(tkinter.END, musicName)
