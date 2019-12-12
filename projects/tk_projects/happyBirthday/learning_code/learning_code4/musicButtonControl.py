#!-*-coding:utf-8-*-
# !@Date: 2018/8/12 10:47
# !@Author: Liu Rui
# !@github: bigfoolliu


import tkinter
import pygame
import os


# 控制音乐按钮（播放，暂停，停止，上一曲，下一曲）
class MusicButtonControl(tkinter.Frame):
	def __init__(self, master, otherMusicList):
		self.frame = tkinter.Frame(master)
		self.frame.pack(side=tkinter.TOP, fill=tkinter.Y)

		# 加载音乐列表
		self.otherMusicList = otherMusicList
		self.loadMusic()
		print("======音乐加载完成")
		self.buttonPlay = tkinter.Button(self.frame, text="播放",
								 command=self.playMusic,
								 width=8, height=2, bg='#FFEC8B')
		self.buttonPlay.pack(side=tkinter.LEFT, fill=tkinter.X)

		self.buttonPause = tkinter.Button(self.frame, text="暂停",
								  command=self.pauseMusic,
								  width=8, height=2, bg='#FFEC8B')
		self.buttonPause.pack(side=tkinter.LEFT, fill=tkinter.X)

		self.buttonStop = tkinter.Button(self.frame, text="停止",
								 command=self.stopMusic,
								 width=8, height=2, bg='#FFEC8B')
		self.buttonStop.pack(side=tkinter.LEFT, fill=tkinter.X)

		self.buttonPrevious = tkinter.Button(self.frame, text="上一曲",
									 command=self.previousMusic,
									 width=8, height=2, bg='#FFEC8B')
		self.buttonPrevious.pack(side=tkinter.LEFT, fill=tkinter.X)

		self.buttonNext = tkinter.Button(self.frame, text="下一曲",
								 command=self.nextMusic,
								 width=8, height=2, bg='#FFEC8B')
		self.buttonNext.pack(side=tkinter.LEFT, fill=tkinter.X)

	# self.textLyric = tkinter.Text(self.frame, bg="#FFDEAD", width=8,height=50)
	# self.textLyric.pack(side=tkinter.LEFT, fill=tkinter.X)

	def loadMusic(self):
		pygame.mixer.init()
	# self.otherMusicList.listBox.select_set(0)
	# musicFilePath = r"E:\Python-1704\python\day15\homework\播放音乐器\music"
	# print(self.otherMusicList.listBox.size())
	# print("播放：", self.otherMusicList.getMusicPath())

	def playMusic(self):
		pygame.mixer.music.load(self.otherMusicList.getCurrentMusicPath())
		pygame.mixer.music.play()
		print(self.otherMusicList.getCurrentMusicPath())

	def pauseMusic(self):
		pygame.mixer.music.pause()

	def stopMusic(self):
		pygame.mixer.music.stop()

	def	previousMusic(self):
		path = r"E:\Python-1704\python\day15\homework\播放音乐器\music"
		currentMusicPath = self.otherMusicList.getCurrentMusicPath()

		for musicpathIndex in range(self.otherMusicList.listBox.size()):
			ismusic = 0
			musicAbs1Path = path + "\\" + self.otherMusicList.listBox.get(musicpathIndex)
			if currentMusicPath == musicAbs1Path:
				ismusic = musicpathIndex
				ismusic -= 1
				musicAbsPath = path + "\\" + self.otherMusicList.listBox.get(ismusic)
				if ismusic < 0:
					pygame.mixer.music.load(path + "\\" + self.otherMusicList.listBox.get(0))
					pygame.mixer.music.play()
					break
			pygame.mixer.music.load(musicAbsPath)
			# 显示正在播放的歌曲，并取消上一首歌曲的选中
			self.otherMusicList.listBox.select_clear(musicpathIndex)
			self.otherMusicList.listBox.select_set(ismusic)
			pygame.mixer.music.play()
			break

	def nextMusic(self):
		path = r"E:\Python-1704\python\day15\homework\播放音乐器\music"
		currentMusicPath = self.otherMusicList.getCurrentMusicPath()

		for musicpathIndex in range(self.otherMusicList.listBox.size()):
			ismusic = 0
			musicAbs1Path = path + "\\" + self.otherMusicList.listBox.get(musicpathIndex)
			if currentMusicPath == musicAbs1Path:
				ismusic = musicpathIndex
				ismusic += 1
				if ismusic >= self.otherMusicList.listBox.size():
					pygame.mixer.music.load(path + "\\" + self.otherMusicList.listBox.get(self.otherMusicList.listBox.size() - 1))
					pygame.mixer.music.play()
					break
			musicAbsPath = path + "\\" + self.otherMusicList.listBox.get(ismusic)
			pygame.mixer.music.load(musicAbsPath)
			# 显示正在播放的歌曲，并取消上一首歌曲的选中
			self.otherMusicList.listBox.select_clear(musicpathIndex)
			self.otherMusicList.listBox.select_set(ismusic)
			pygame.mixer.music.play()
			break
