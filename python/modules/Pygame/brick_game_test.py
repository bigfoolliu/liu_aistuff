#!-*-coding:utf-8-*-
# !@Date: 2018/7/25 8:51
# !@Author: Liu Rui
# !@github: bigfoolliu


import pygame
import sys
from pygame.locals import *
"""
数组记录砖块是否已经被打掉
"""
# NUM_BLOCK_COLS = 10  # 砖块的列数
# NUM_BLOCK_ROWS = 5  # 砖块的行数
# # 初始化二维数组的另一种方式
# blocks = [[1] * NUM_BLOCK_COLS] * NUM_BLOCK_ROWS  # 记录砖块是否已经被打掉


# NUM_BLOCK_ROWS = 8
# NUM_BLOCK_COLUMNS = 6
# blocks = []
# for i in range(NUM_BLOCK_ROWS):
# 	blocks.append([i + 1] * NUM_BLOCK_COLUMNS)
#
# print(blocks)


# 退出游戏
def terminate():
	pygame.quit()  # 让pygame的模块取消初始化
	sys.exit()


TEXT_COLOR = (255, 255, 255)


# 显示文字
def draw_text(text, font, surface, x, y):
	text_obj = font.render(text, 1, TEXT_COLOR)  # 文字转换为surface对象
	text_rect = text_obj.get_rect()  # 获得surface对象的矩形区域
	text_rect.topleft = (x, y)
	surface.blit(text_obj, text_rect)


# 等待用户输入
def wait_for_player_to_press_key():
	while True:
		for input_event in pygame.event.get():
			if input_event.type == QUIT:
				terminate()
			if input_event.type == KEYDOWN:
				if input_event.key == K_ESCAPE:
					terminate()
				return


FPS = 24
mainClock = pygame.time.Clock()  # 创造一个追踪时间的对象
...  # 中间写运行的代码
mainClock.tick(FPS)  # 每一帧调用一次来计算上一次调用至今的时间,增加参数可以确保每秒不超过FPS帧,以此限定游戏的速率

# 加载音效
game_over_sound = pygame.mixer.Sound('gameover.wav')  # 创建一个声音对象
game_hit_sound = pygame.mixer.Sound('hit.wav')

pygame.mixer.music.load('background.mp3')  # 加载一首歌曲文件做重放用
pygame.mixer.music.play(-1, 0.0)  # 播放背景音乐
