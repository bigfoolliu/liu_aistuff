#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pygame的事件

pygame.event.get()     获取事件,相当于打开大门处理所有的事件
pygame.event.wait()    发生一个事件才继续下去

两者在真正的游戏中不太实用

pygame.event.poll()    一旦调用,会根据现在的情形返回一个真实的事件,或者返回"什么都不发生"
常见事件集:
事件                   产生途径                      参数
QUIT                  用户按下关闭按钮                none
ATIVEEVENT            pygame被激活或者隐藏           gain,state
KEYDOWN               键盘被按下                     unicode,key,mod
KEYUP                 键盘被放开                     key,mod
MOUSEMOTION           鼠标移动                       pos,rel,buttons
MOUSEBUTTONDOWN       鼠标按下                       pos,button
MOUSEBUTTONUP         鼠标放开                       pos,button
JOYAXISMOTION         (joystick or pad)移动         joy,axis,value
JOYBALLMOTION         (joy ball)移动                joy,axis,value
JOYHATMOTION          (joy hat)移动                 joy,axis,value
JOYBUTTONDOWN         (joy button)按下              joy,button
JOYBUTTONUP           (joy button)放开              joy,button
VIDEORESIZE           pygame窗口缩放                 size,w,h
VIDEOEXPOSE           pygame窗口(expose)             none
USEREVENT             触发了一个用户事件               code
处理键盘事件

按下键盘的方向键可以移动背景图片
"""

import pygame
from pygame.locals import *
from sys import exit

background_image_filename = "./res/background.jpg"

pygame.init()
screen = pygame.display.set_mode((1000, 640), 0, 32)
background = pygame.image.load(background_image_filename)

# 设置图像的目标位置坐标和单次移动的距离
x, y = 0, 0
move_x, move_y = 0, 0

while True:
    # 持续监测事件
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # 如果有键盘被按下
        if event.type == KEYDOWN:
            if event.key == K_LEFT:  # 按下左方向键
                move_x = -10
            elif event.key == K_RIGHT:  # 按下右方向键
                move_x = 10
            elif event.key == K_UP:  # 按下上方向键
                move_y = -10
            elif event.key == K_DOWN:  # 按下下方向键
                move_y = 10
        # 如果用户放开了键盘,图不动
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0

        x += move_x
        y += move_y

        screen.fill((0, 255, 0))  # 窗口填充绿色
        screen.blit(background, (x, y))

        # 在新的位置画图
        pygame.display.update()
