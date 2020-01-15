#!-*-coding:utf-8-*-
# !@Date: 2018/8/4 9:32
# !@Author: Liu Rui
# !@github: bigfoolliu


import pygame
from pygame.locals import *
import sys
import random


# 游戏常量
BACKGROUND_COLOR = (0, 0, 255)  # 窗口背景颜色
FPS = 30  # 游戏帧率
BRICK_ROW = 5  # 砖块的行数
BRICK_COL = 15  # 砖块的列数


class Ball(object):
	"""球类"""
	def __init__(self, surface):
		self.radis = 10  # 球的半径
		self.color = (255, 0, 0)  # 球的颜色
		# self.pos = [random.randint(self.radis, surface.get_width() - self.radis), surface.get_height() // 2]  # 球的初始位置
		self.pos = [10, 240]  # 球的初始位置
		self.rect = Rect(0, 0, self.radis * 2, self.radis * 2)  # 创建球的空的Rect对象
		print(self.rect)
		self.dx = -5  # 一帧水平移动的分量
		self.dy = -5  # 一帧纵向移动分量

	def display(self, surface):
		"""球显示于窗口"""
		self.rect = pygame.draw.circle(surface, self.color, self.pos, self.radis)
		print(self.rect)

	def move(self, surface, player):
		"""球的移动"""
		# 碰到墙壁
		if self.pos[1] <= self.radis:  # 碰到上部墙壁
			self.dy = -self.dy
		# 碰到左墙壁
		elif self.pos[0] <= self.radis and self.pos[1] <= surface.get_height() - player.height - self.radis:
			self.dx = - self.dx
		# 碰到右墙壁
		elif self.pos[0] >= surface.get_width() - self.radis and \
				self.pos[1] <= surface.get_height() - player.height - self.radis:
			self.dx = - self.dx
		# 玩家接到球
		elif player.pos[0] <= self.pos[0] <= player.pos[0] + player.width and \
				self.pos[1] >= surface.get_height() - player.height - self.radis:
			self.dy = -self.dy
		# 球触底
		elif self.pos[1] >= surface.get_height() - self.radis:
			self.dx = 0
			self.dy = 0
		# 撞到砖块

		self.pos[0] += self.dx
		self.pos[1] += self.dy
		self.rect = Rect(self.pos[0] - self.radis, self.pos[1] - self.radis, self.radis * 2, self.radis * 2)


class Player(object):
	"""玩家类"""
	def __init__(self, surface):
		self.width = surface.get_width() // 6
		self.height = surface.get_height() // 50
		self.pos = [surface.get_width() // 2 - self.width // 2, surface.get_height() - self.height]
		self.color = (0, 255, 0)
		self.dx = 10

	def display(self, surface):
		"""玩家显示于窗口"""
		if self.pos[0] <= 0:
			self.pos[0] = 0
		elif self.pos[0] >= surface.get_width() - self.width:
			self.pos[0] = surface.get_width() - self.width
		pygame.draw.rect(surface, self.color, (tuple(self.pos)[0], tuple(self.pos)[1], self.width, self.height))


class Brick(object):
	"""砖块类"""
	def __init__(self, ball, surface):
		self.color = (255, 162, 38)
		self.gap = ball.radis * 2 + 1  # 砖块之间的横纵方向的间距
		self.width = (surface.get_width() - self.gap * (BRICK_COL - 1)) // BRICK_COL  # 砖块的宽度
		self.height = int(self.width * (surface.get_height() / surface.get_width()))  # 砖块的高度
		self.is_hited = False  # 默认未被击中
		self.rect = Rect(0, 0, self.width, self.height)  # 创建砖块的空的Rect对象

	def display(self, pos_x, pos_y, surface):
		"""显示单个砖块"""
		self.rect = Rect(pos_x, pos_y, self.width, self.height)
		if not self.is_hited:
			pygame.draw.rect(surface, self.color, self.rect)
		elif self.is_hited:
			pass


def create_brick_list(brick):
	"""创建砖块列表"""
	brick_list = []
	for row in range(BRICK_ROW):
		row_list = []
		for col in range(BRICK_COL):
			row_list.append(brick)
		brick_list.append(row_list)
	return brick_list


def display_brick_list(brick, brick_list, surface):
	"""显示砖块列表"""
	for row in range(BRICK_ROW):
		for col in range(BRICK_COL):
			pos_x = col * (brick.width + brick.gap)
			pos_y = row * (brick.gap + brick.height)
			brick_list[row][col].display(pos_x, pos_y, surface)  # 砖块一个显示


def judge_hited(brick_list, ball):
	"""判断是否撞击到砖块"""
	hit_result = False
	for row in range(BRICK_ROW):
		for col in range(BRICK_COL):
			if ball.rect.colliderect(brick_list[row][col].rect):
				hit_result = True
				print("撞击")
			return hit_result


def main():
	pygame.init()

	game_window = pygame.display.set_mode((640, 480), 0, 32)  # 创建一个窗口Surface
	pygame.display.set_caption("打砖块")
	game_clock = pygame.time.Clock()  # 创建一个时钟对象

	ball = Ball(game_window)
	player = Player(game_window)
	brick = Brick(ball, game_window)
	brick_list = create_brick_list(brick)  # 砖块类实例的列表

	while True:

		game_window.fill(BACKGROUND_COLOR)  # 窗口背景填充白色

		display_brick_list(brick, brick_list, game_window)  # 显示砖块

		# 监听退出事件
		for game_event in pygame.event.get():
			if game_event.type == QUIT:
				pygame.quit()
				sys.exit()

		# 玩家的左右移动
		player.display(game_window)  # 显示玩家
		if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]:
			player.pos[0] -= player.dx
		elif pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]:
			player.pos[0] += player.dx

		ball.display(game_window)  # 显示球
		ball.move(game_window, player)  # 球的移动

		judge_hited(brick_list, ball)

		game_clock.tick(FPS)  # 帧率设置
		pygame.display.update()


if __name__ == '__main__':
	main()
