#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
检查九子棋的解法以及必胜策略
"""

import numpy as np


class Chess:
    
	def __init__(self, owner=None):
		"""owner为x或者o"""
		self.owner = owner


def board_init(rows=3, cols=3):
	"""初始化棋盘"""
	board_array = []
	rows = rows
	cols = cols
	for row in range(rows):
		board_array.append([Chess() for col in range(cols)])
	return np.array(board_array)


def put_chess(pos_x, pos_y, chess, array):
	"""在棋盘指定放置棋子"""
	if array[pos_x][pos_y].owner:
		raise Exception("positon ({}, {}) already has chess".format(pos_x, pos_y))
	array[pos_x][pos_y].owner = chess.owner
	return array


def draw_board(array):
	"""画出当前棋盘"""
	print("--------------------------")
	for row in array:
		print([c.owner for c in row])
	print("--------------------------")


def check_all_possibilities(array):
	"""检查所有下棋的方案"""
	return


def trans_array(array):
	"""将棋盘向右翻转90"""
	new_array = array.reshape(array.size)
	new_array = new_array[::-1]
	new_array = new_array.reshape(array.shape)
	new_array = np.transpose(new_array)[::-1]
	return new_array


def get_winner(array):
	"""获取当前的赢家"""
	# 行,列产生赢家, TODO:
	new_lst = []
	for index, row in enumerate(array):
		if len(set(row)) == 1 and (None not in set(row)):
			return row[0].owner
		new_lst.append(array[index][index])
	
	# 斜向产生赢家,仅两种情况
	if len(set(new_lst)) == 1 and (None not in set(new_lst)):
		return new_lst[0].owner

	new_lst = []
	for index, row in enumerate(trans_array(array)):
		if len(set(row)) == 1 and (None not in set(row)):
			return row[0].owner
		new_lst.append(array[index][index])
	if len(set(new_lst)) == 1 and (None not in set(new_lst)):
		return new_lst[0].owner
	return None


if __name__ == "__main__":
	board_array = board_init()
	print("棋盘初始化:")
	draw_board(board_array)

	new_chess = Chess("x")
	board_array = put_chess(0, 1, new_chess, board_array)
	
	new_chess = Chess("o")
	board_array = put_chess(1, 0, new_chess, board_array)

	new_chess = Chess("x")
	board_array = put_chess(1, 1, new_chess, board_array)


	new_chess = Chess("o")
	board_array = put_chess(0, 0, new_chess, board_array)

	new_chess = Chess("x")
	board_array = put_chess(2, 1, new_chess, board_array)
	print("下完棋")
	draw_board(board_array)

	print("棋盘向右翻转90度")
	board_array = trans_array(board_array)
	draw_board(board_array)
	print(get_winner(board_array))

