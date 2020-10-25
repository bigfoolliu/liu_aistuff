#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pygame React对象
"""


import pygame
import pygame.locals
import sys
import time

pygame.init()

pygame.display.set_mode((400, 400))
pygame.display.set_caption('hello, pygame')


def create_rect():
    """创建矩形区域"""
    _rect = pygame.Rect(10, 20, 30, 40)  # 左上角坐标为(10, 20), 长度为30像素，宽度为40像素
    # React对象的几个常用的属性
    print(_rect.left)  # 左边的X坐标
    print(_rect.right)  # 右边的X坐标
    print(_rect.top)  # 上边的Y坐标
    print(_rect.bottom)  # 下边的Y坐标
    print(_rect.size)  # 一个元祖(width, height)


while True:
    time.sleep(0.5)

    create_rect()

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

