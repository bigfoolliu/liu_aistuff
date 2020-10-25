#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pygame使用draw画图
"""


import pygame
import pygame.locals
import sys


class Color(object):
    """颜色"""
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)


def init_display():
    """初始化显示"""
    _flags = pygame.RESIZABLE  # 可以随意改变大小
    display_surface = pygame.display.set_mode((400, 400), _flags) 
    pygame.display.set_caption('hello, pygame')
    display_surface.fill(Color.GREEN)
    return display_surface


def draw_line(surface):
    """画一条直线线段"""
    print('begin to draw line')
    pygame.draw.line(surface, Color.RED, (50, 60), (100, 60), 4)  # 线段的起点坐标为(59, 60), 终点坐标为(100, 60), 线宽度为4


def main():
    """主函数"""
    pygame.init()
    DISPLAY_SURFACE = init_display()

    print(Color.WHITE)

    draw_line(DISPLAY_SURFACE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()

