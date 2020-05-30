#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
基于pygame模块做的贪吃蛇小游戏
"""
import pygame
import numpy as np
import time
from pygame.locals import *

BOARDWIDTH = 48
BOARDHEIGHT = 28
score = 0


class Food(object):

    def __init__(self):
        self.item = (4, 5)
        self.color = 255, 0, 255
        self.radius = 10
        self.width = 10

    def _draw(self, screen, i, j):
        """画出食物"""
        position = 10 + 20 * i, 10 + 20 * j
        pygame.draw.circle(screen, self.color, position, self.radius, self.width)

    def update(self, screen, enlarge, snake):
        """随机产生食物"""
        if enlarge:
            self.item = np.random.randint(1, BOARDWIDTH - 2), np.random.randint(1, BOARDHEIGHT - 2)
            while self.item in snake.item:
                self.item = np.random.randint(1, BOARDWIDTH - 2), np.random.randint(1, BOARDHEIGHT - 2)
        self._draw(screen, self.item[0], self.item[1])


class Snake(object):

    def __init__(self):
        self.item = [[3, 25], [2, 25], [1, 25], [1, 24], ]
        self.x = 0
        self.y = -1
        self.speed = 1  # 蛇的速度

    def move(self, enlarge):
        """移动"""
        if not enlarge:
            self.item.pop()

        head = (self.item[0][0] + self.x, self.item[0][1] + self.y)
        self.item.insert(0, head)

    def eat(self, food):
        """吃到食物"""
        global score
        snake_x, snake_y = self.item[0]
        food_x, food_y = food.item
        if (food_x == snake_x) and (food_y == snake_y):
            score += 1
            return 1
        else:
            return 0

    def toward(self, x, y):
        """改变蛇的朝向"""
        if self.x * x >= 0 and self.y * y >= 0:
            self.x = x
            self.y = y

    def get_head(self):
        """获取蛇头坐标"""
        return self.item[0]

    def draw(self, screen):
        """画出蛇"""
        radius = 15
        width = 15
        color = 255, 0, 0
        position = 10 + 20 * self.item[0][0], 10 + 20 * self.item[0][1]
        pygame.draw.circle(screen, color, position, radius, width)

        radius = 10
        width = 10
        color = 255, 255, 0
        for i, j in self.item[1:]:
            position = 10 + 20 * i, 10 + 20 * j
            pygame.draw.circle(screen, color, position, radius, width)


class Board(object):

    def __init__(self):
        self.board_width = BOARDWIDTH
        self.board_height = BOARDHEIGHT

    def draw_board(self, screen):
        """画出游戏区域"""
        color = 10, 255, 255
        width = 0

        for i in range(self.board_width):
            pos = i * 20, 0, 20, 20
            pygame.draw.rect(screen, color, pos, width)
            pos = i * 20, (self.board_height - 1) * 20, 20, 20
            pygame.draw.rect(screen, color, pos, width)

        for i in range(self.board_height - 1):
            pos = 0, 20 + i * 20, 20, 20
            pygame.draw.rect(screen, color, pos, width)
            pos = (self.board_width - 1) * 20, 20 + i * 20, 20, 20
            pygame.draw.rect(screen, color, pos, width)

    def print_text(self, screen, font, x, y, text, color=(255, 0, 0)):
        """屏幕打印字符"""
        img_text = font.render(text, True, color)
        screen.blit(img_text, (x, y))


class Game():

    def __init__(self):
        """游戏初始化"""
        pygame.init()
        self.screen = pygame.display.set_mode((BOARDWIDTH * 20, BOARDHEIGHT * 20))
        pygame.display.set_caption("snake_game")

    def game_start(self, screen):
        """开始游戏"""
        snake = Snake()
        food = Food()
        board = Board()
        player = Player()
        font = pygame.font.SysFont("SimHei", 30)
        is_fail = 0

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            screen.fill((0, 0, 100))
            board.draw_board(screen=screen)

            keys = pygame.key.get_pressed()
            player.press(keys, snake)

            if is_fail:
                font2 = pygame.font.Font(None, 40)
                board.print_text(screen, font, 0, 0, text)
                board.print_text(screen, font2, 400, 200, "GAME OVER")

            if not is_fail:
                enlarge = snake.eat(food)
                global score
                text = "score: {}".format(score)
                board.print_text(screen, font, 0, 0, text)
                food.update(screen, enlarge, snake)
                snake.move(enlarge)
                is_fail = self.game_over(snake=snake)
                snake.draw(screen)

            pygame.display.update()
            time.sleep(0.05)

    def game_over(self, snake):
        """判断游戏是否结束"""
        board_x, board_y = snake.get_head()
        flag = 0
        old = len(snake.item)
        # 多重列表去重
        tmp_list = []
        for i in snake.item:
            if i not in tmp_list:
                tmp_list.append(i)
        new = len(tmp_list)

        if new < old:
            flag = 1
        if board_x == 0 or board_x == BOARDWIDTH - 1:
            flag = 1
        if board_y == 0 or board_y == BOARDHEIGHT - 1:
            flag = 1

        if flag:
            return True
        else:
            return False


class Player(object):

    def __init__(self):
        pass

    def press(self, keys, snake):
        """按键控制"""
        global score
        if keys[K_w] or keys[K_UP]:
            snake.toward(0, -1)
        elif keys[K_s] or keys[K_DOWN]:
            snake.toward(0, 1)
        elif keys[K_a] or keys[K_LEFT]:
            snake.toward(-1, 0)
        elif keys[K_d] or keys[K_RIGHT]:
            snake.toward(1, 0)
        elif keys[K_r]:  # 重置游戏
            score = 0
            main()


def main():
    game = Game()
    game.game_start(game.screen)


main()
