#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
检查九子棋的解法以及必胜策略
"""

from itertools import combinations, permutations
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
	"""在棋盘指定放置棋子
	pos_x: int, 0, 1, 2
	pos_y: int, 0, 1, 2
	"""
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
	"""获取当前的赢家
	return: str
	"""
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


def check_all_possibilities():
	"""检查所有下棋的方案
	1. 产生棋盘
	2. 依次下棋子
		从位置1至位置9依次下棋,且要保证每次下的位置不同
	3. 每次下完检查是否有胜者
	4. 有胜者则结束比赛
	
	从位置中选取数字，每个数字只能选择一次，路径规划;
	如果前几个数字的组合中产生了胜者，则后面就没必要继续下去;

	"""
	posibilities = 0
	positions = {0, 1, 2, 3, 4, 5, 6, 7, 8}
	for permution in permutations(positions, len(positions)):
		one_choice = OneChoice()
		board_array = board_init()
		# 根据每一种的组合获得其位置，然后一次下棋
		print(permution)
		for i in permution:
			pos_x, pos_y = get_pos(i)
			chess = Chess(one_choice.pick_player())
			board_array = put_chess(pos_x, pos_y, chess, board_array)
			winner = get_winner(board_array)
			if winner:
				print("winner is {}".format(winner))
				draw_board(board_array)
				posibilities += 1
				break
	print("all posibilities: {}".format(posibilities))


def get_pos(num):
	"""根据数字返回坐标位置"""
	if num == 0:
		return (0, 0)
	elif num == 1:
		return (0, 1)
	elif num == 2:
		return (0, 2)
	elif num == 3:
		return (1, 0)
	elif num == 4:
		return (1, 1)
	elif num == 5:
		return (1, 2)
	elif num == 6:
		return (2, 0)
	elif num == 7:
		return (2, 1)
	elif num == 8:
		return (2, 2)


if __name__ == "__main__":
	"""
	    o
	x o x
	o x  
	"""
	check_all_possibilities()

