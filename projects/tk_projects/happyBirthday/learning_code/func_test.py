#!-*-coding:utf-8-*-
# !@Date: 2018/8/12 19:34
# !@Author: Liu Rui
# !@github: bigfoolliu


import pygame
from tkinter import *
import os

# 准备tkinter界面
screen = Tk()
screen.title("pygame + tkinter")

frame = Frame(screen, width=300, height=200, bg="white")
frame.pack(fill=BOTH)
button_press = Button(screen, text="start", bg="green")
button_press.pack()

# 核心代码, 将会将告诉pygame的SDL window使用哪一个window id,就是将显示窗口绑定到上面
os.environ["SDL_WINDOWID"] = str(frame.winfo_id())  # pygame界面将会在frame上显示主界面

screen.update()  # 显示一下主界面然后消失

pygame.display.init()
window = pygame.display.set_mode((280, 180))

while True:
	window.fill((255, 0, 0))
	pygame.display.flip()  # 更新整个pygame的显示界面

	screen.update()
