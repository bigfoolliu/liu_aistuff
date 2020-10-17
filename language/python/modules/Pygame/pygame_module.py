#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pygame模块包含的模块

pygame.cdrom		  访问光驱

pygame.cursors      加载光标

pygame.display      访问显示设备

pygame.draw         绘制形状,线和点

pygame.event        管理事件

pygame.font         使用字体

pygame.image        加载和存储图片

pygame.joystick     使用游戏手柄或者类似的东西

pygame.key          读取键盘按键

pygame.mixer        声音

pygame.mouse        鼠标

pygame.movie        播放视频

pygame.music        播放音频

pygame.overlay      访问高级视频叠加

pygame.rect         管理矩形区域

pygame.sndarray     操作声音数据

pygame.sprite       操作移动图像

pygame.surface      管理图像和屏幕

pygame.surfarray    管理点阵图像数据

pygame.time         管理时间和帧信息

pygame.transform    缩放和移动图像

pygame              本地库
"""
import pygame
from pygame.locals import *  # 导入一些常用的函数和变量
from sys import exit  # 借exit函数退出程序

background_image_filename = "background.jpg"
mouse_image_filename = "follow_mouse.jpg"

# 初始化pygame,为使用硬件做准备
pygame.init()

# 创建一个640*480的窗口,标志位为XX,色深为32
# """
# 标志位可以指定窗口的特性
#
# 0             无任何特性
#
# FULLSCREEN    创建全屏窗口
#
# DOUBLEBUF     创建一个"双缓冲"窗口,建议在HWSURFACE或OPENGL使用
#
# HWSURFACE     创建一个硬件加速窗口,必须和FULLSCREEN同时使用
#
# OPENGL        创建一个OPENGL渲染的窗口
#
# RESIZABLE     创建一个可改变大小的窗口
#
# NOFRAME       创建一个没有边框的窗口
# """
screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)  # set_mode返回的是一个surface对象

# 设置窗口标题
pygame.display.set_caption("LR' first pygame demo.")

# 加载并转换图像
background = pygame.image.load(background_image_filename)
mouse_cursor = pygame.image.load(mouse_image_filename)

screen.blit(background, (0, 0))  # 此句应该删除
# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            exit()

    # 画背景图,尽管背景图不动,但是仍然需要更新,否则鼠标经过的地方不能恢复
    # blit函数,第一个参数代表surface对象,第二个为左上角位置
    # screen.blit(background, (0, 0))
    # 获得鼠标位置
    x, y = pygame.mouse.get_pos()
    # 计算光标左上角的位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 将光标画上去
    screen.blit(mouse_cursor, (x, y))

    # 刷新画面
    pygame.display.update()
