#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
检查九子棋的解法以及必胜策略
"""

import numpy as np


class Chess(object):
    
	def __init__(self, owner=None):
		"""owner为x或者o"""
		self.owner = owner


class OneChoice(object):

	"""单例,用于选择选手，且保证每次选择的和上一次不同"""

	_instance = {}

	def __new__(cls, *args, **kwargs):
		if cls not in cls._instance:
			cls._instance[cls] = super().__new__(cls)
		return cls._instance[cls]

	def __init__(self, player=None):
		"""初始化选择一个作为第一个选手"""
		self.players = ["x", "o"]
		if player and player not in self.players:
			raise Exception("player {} does not exist".format(player))
		self.cur_player = player

	def pick_player(self):
		"""选择一个选手，且需要确保这一次和上一次的不同"""
		if not self.cur_player:
			pick_player = self.players[0]
			self.cur_player = pick_player
			return pick_player

		if self.cur_player == "o":
			pick_player = "x"
			self.cur_player = pick_player
		elif self.cur_player == "x":
			pick_player = "o"
			self.cur_player = pick_player
		return pick_player


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


def generate_chess(player=None):
	"""根据传入的player返回棋子对象"""
	if player not in ("x", "o"):
		raise Exception("player {} does not exist}".format(player))
	return Chess(player)


def trans_array(array):
	"""将棋盘向右翻转90"""
	new_array = array.reshape(array.size)
	new_array = new_array[::-1]
	new_array = new_array.reshape(array.shape)
	new_array = np.transpose(new_array)[::-1]
	return new_array


def get_winner(array):
	"""获取当前的赢家"""
	# 行,列产生赢家
	new_lst = []
	for index, row in enumerate(array):
		owners = [c.owner for c in row]
		if len(set(owners)) == 1 and (None not in set(owners)):
			return owners[0]
		new_lst.append(array[index][index].owner)
	
	# 斜向产生赢家,仅两种情况
	if len(set(new_lst)) == 1 and (None not in set(new_lst)):
		return new_lst[0]

	new_lst = []
	transed_array = trans_array(array)
	for index, row in enumerate(transed_array):
		owners = [c.owner for c in row]
		if len(set(owners)) == 1 and (None not in set(owners)):
			return owners[0]
		new_lst.append(transed_array[index][index].owner)

	if len(set(new_lst)) == 1 and (None not in set(new_lst)):
		return new_lst[0]
	return None


def check_all_possibilities(array):
	"""检查所有下棋的方案"""
	player = None
	chess = generate_chess(player)

	put_chess()


if __name__ == "__main__":
	"""
	    o
	x o x
	o x  
	"""
	pass

