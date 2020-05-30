#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


# grid_list = []
#
#
# def create_grid():
# 	"""
# 	创建棋盘的位置列表
# 	:return:
# 	"""
# 	# grid_list = []  # 记录每个格子的信息,元素为{"num": , "coordinate": , occupy_flag": },坐标为左上角坐标,
# 	# for num in range(0, 9):
# 	# 	grid = {}
# 	# 	if 0 <= num < 3:
# 	# 		grid[] = {"num": num, "coordinate": (200 + 100 * num, 200), "occupy_flag": 0}  # 0为未被占据
# 	# 		grid_list.append(grid)
# 	# 	elif 3 <= num < 6:
# 	# 		grid = {"num": num, "coordinate": (200 + 100 * (num - 3), 400), "occupy_flag": 0}
# 	# 		grid_list.append(grid)
# 	# 	elif 6 <= num < 9:
# 	# 		grid = {"num": num, "coordinate": (200 + 100 * (num - 6), 600), "occupy_flag": 0}
# 	# 		grid_list.append(grid)
#
# 	for row in range(0, 3):  # 遍历行
# 		for col in range(0, 3):  # 遍历列
# 			grid = {}
# 			grid["num"] = (row, col)
# 			grid["coordinate"] = ((150 + 100 * row), (150 + 100 * col))
# 			grid["occupy_flag"] = 0
# 			grid_list.append(grid)
#
#
# create_grid()
# print(grid_list)


# game_state_list = []
#
# for row in range(0, 3):
# 	for col in range(0, 3):
# 		state = {}
# 		state["num"] = (row, col)
# 		state["chess"] = None
# 		game_state_list.append(state)
#
#
# print(game_state_list)


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a[0][0])


# a = []
# for row in range(0, 3):
# 	b = []
# 	for col in range(0, 3):
# 		b.append(None)
# 	a.append(b)
#
# print(a)


# grid_list = []
# for row in range(0, 3):  # 遍历行
# 	list1 = []
# 	for col in range(0, 3):  # 遍历列
# 		grid = {}
# 		grid["num"] = (row, col)
# 		grid["coordinate"] = ((150 + 100 * col), (150 + 100 * row))
# 		grid["occupy_flag"] = 0  # 0表示默认未被占用
# 		grid["chess"] = None  # 记录每个棋盘放置的是什么棋子0表示o, 1表示叉
# 		list1.append(grid)
# 	grid_list.append(list1)
#
# print(grid_list)


import pygame

a = pygame.font.FontType()
print(a, type(a))
