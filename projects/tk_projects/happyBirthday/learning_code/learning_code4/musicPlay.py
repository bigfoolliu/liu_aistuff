#!-*-coding:utf-8-*-
# !@Date: 2018/8/12 10:41
# !@Author: Liu Rui
# !@github: bigfoolliu


import tkinter

from musicList import MusicList
from musicButtonControl import MusicButtonControl
from musicLyricText import MusicLyricText

win = tkinter.Tk()
win.title("音乐播放器")
win.geometry("700x500+200+100")

musicList = MusicList(win)
musicButton = MusicButtonControl(win, musicList)
musicLyric = MusicLyricText(win)

win.mainloop()
