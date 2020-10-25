#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
事件处理->游戏循环->绘制屏幕

"""

import pygame
import pygame.locals
import sys
import time

# 始终需要首先调用
pygame.init()

print(pygame.font.get_fonts())

pygame.display.set_caption('hello. pygame')
pygame.display.set_mode((400, 400))

while True:
    print(f'{time.time()}ready\n')
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()  # 刷新屏幕显示
