#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import pygame
from pygame.locals import *
from sys import exit

grid_list = []
grid_state_list = []
"""

game_over_list =
1.   (0, 0), 0      (0, 1), 0      (0, 2), 0
2.   (1, 0), 0      (1, 1), 0      (1, 2), 0
3.   (2, 0), 0      (2, 1), 0      (2, 2), 0

4.   (0, 0), 0      (1, 0), 0      (2, 0), 0
5.   (0, 1), 0      (1, 1), 0      (2, 1), 0
6.   (0, 2), 0      (1, 2), 0      (2, 2), 0

7.   (0, 0), 0      (1, 1), 0      (2, 2), 0
8.   (0, 2), 0      (1, 1), 0      (2, 0), 0

9.
...
16.

"""


def out_put_test(event):
    """输出测试"""
    if event.type == MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        pressed_array = pygame.mouse.get_pressed()

        print(pressed_array, type(pressed_array))  # 鼠标按键测试
        print(mouse_pos)
        print("{}类型事件发生.".format(event.type))
    else:
        print("{}类型事件发生了.".format(event.type))


def out_put_test2(grid):
    print(grid["num"], grid["chess"])
    grid_state = []
    grid_state.append(grid["num"])
    grid_state.append(grid["chess"])
    grid_state_list.append(grid_state)
    print(grid_state_list)


def draw_rect(screen):
    """
    画棋盘
    :param screen:
    :return:
    """
    for i in range(0, 9):
        if 0 <= i < 3:
            pygame.draw.rect(screen, (0, 0, 0), (150 + 100 * i, 150, 100, 100), 10)
        elif 3 <= i < 6:
            pygame.draw.rect(screen, (0, 0, 0), (150 + 100 * (i - 3), 250, 100, 100), 10)
        elif 6 <= i < 9:
            pygame.draw.rect(screen, (0, 0, 0), (150 + 100 * (i - 6), 350, 100, 100), 10)


def font_display(screen):
    """
    显示游戏标题
    :param screen:
    :return:
    """
    my_font = pygame.font.SysFont("arial", 40, bold=True)
    text_surface = my_font.render("Little Game", True, (0, 0, 0), (255, 255, 255))
    screen.blit(text_surface, (220, 50))


def game_over_font_display(screen):
    """

    :param screen:
    :return:
    """
    my_font = pygame.font.SysFont("arial", 60, bold=True)
    text_surface = my_font.render("Game Over!", True, (0, 0, 0), (255, 255, 255))
    screen.blit(text_surface, (160, 500))


def draw_circle(screen, position_x, position_y):
    """
    画圆
    :param screen:
    :param position_x: 所画圆的中心位置横坐标
    :param position_y: 所画圆的中心位置的纵坐标
    :return:
    """
    # pygame.draw.circle(screen, (0, 0, 0), (200, 200), 35, 10)
    pygame.draw.circle(screen, (0, 0, 0), (position_x, position_y), 35, 10)


def draw_line(screen, position_x, position_y):
    """
    画叉
    :param screen:
    :param position_x: 所画叉的左上角横坐标
    :param position_y: 所画叉的左上角纵坐标
    :return:
    """
    # pygame.draw.line(screen, (0, 0, 0), (170, 165), (230, 235), 14)
    # pygame.draw.line(screen, (0, 0, 0), (230, 165), (170, 235), 14)

    pygame.draw.line(screen, (0, 0, 0), (position_x, position_y), (position_x + 60, position_y + 70), 14)
    pygame.draw.line(screen, (0, 0, 0), (position_x + 60, position_y), (position_x, position_y + 70), 14)


def create_grid():
    """
    创建棋盘的位置列表
    :return:
    """
    # grid_list = []  # 记录每个格子的信息,元素为{"num": , "coordinate": , occupy_flag": , "chess"},坐标为左上角坐标,
    for row in range(0, 3):  # 遍历行
        list1 = []
        for col in range(0, 3):  # 遍历列
            grid = {}
            grid["num"] = (row, col)
            grid["coordinate"] = ((150 + 100 * col), (150 + 100 * row))
            grid["occupy_flag"] = 0  # 0表示默认未被占用
            grid["chess"] = None  # 记录每个棋盘放置的是什么棋子0表示o, 1表示叉
            list1.append(grid)
        grid_list.append(list1)


chess_num = 0  # 棋盘上的棋子数量,默认为0,最多为9


def put_chess(screen, grid, position_x, position_y):
    """
    落子
    :param grid:
    :param screen:
    :param position_x: 默认落子的横坐标
    :param position_y: 默认落子的纵坐标
    :return:
    """
    global chess_num
    # 首先判断落什么棋子
    if chess_num % 2 == 0:
        draw_circle(screen, position_x + 31, position_y + 35)
        grid["chess"] = 0
    else:
        draw_line(screen, position_x, position_y)
        grid["chess"] = 1

    chess_num += 1


def judge_game(_grid_list):
    """
    判断赛果
    :param _grid_list: 全局棋盘信息
    :return:
    """
    # 判断横着的是否有胜利的
    for row in range(0, 3):
        if (_grid_list[row][0]["chess"] == _grid_list[row][1]["chess"] == _grid_list[row][2]["chess"] == 0) or \
                (_grid_list[row][0]["chess"] == _grid_list[row][1]["chess"] == _grid_list[row][2]["chess"] == 1):
            return True

    # 判断竖着的是否有胜利的
    for col in range(0, 3):
        if (_grid_list[0][col]["chess"] == _grid_list[1][col]["chess"] == _grid_list[2][col]["chess"] == 0) or \
                (_grid_list[0][col]["chess"] == _grid_list[1][col]["chess"] == _grid_list[2][col]["chess"] == 1):
            return True

    # 判断斜的是否有胜利的
    if (_grid_list[0][0]["chess"] == _grid_list[1][1]["chess"] == _grid_list[2][2]["chess"] == 0) or \
            (_grid_list[0][2]["chess"] == _grid_list[1][1]["chess"] == _grid_list[2][0]["chess"] == 0) or \
            (_grid_list[0][0]["chess"] == _grid_list[1][1]["chess"] == _grid_list[2][2]["chess"] == 1) or \
            (_grid_list[0][2]["chess"] == _grid_list[1][1]["chess"] == _grid_list[2][0]["chess"] == 1):
        return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))

    screen.fill((255, 255, 255))

    draw_rect(screen)
    font_display(screen)

    pygame.display.update()  # 这里更新,已显示背景,即不变得部分

    create_grid()

    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            exit()

        # out_put_test(event)
        if event.type == MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()

            if pressed_array[0] == 1:  # 鼠标左键按下
                mouse_pos = pygame.mouse.get_pos()

                for row in range(0, 3):
                    for col in range(0, 3):

                        if (0 < mouse_pos[0] - grid_list[row][col]["coordinate"][0] < 100) and \
                                (0 < mouse_pos[1] - grid_list[row][col]["coordinate"][1] < 100):  # 获取鼠标当前在棋盘的位置
                            if grid_list[row][col]["occupy_flag"] == 0:  # 格子未放置棋子
                                put_x = grid_list[row][col]["coordinate"][0] + 20
                                put_y = grid_list[row][col]["coordinate"][1] + 15

                                put_chess(screen, grid_list[row][col], put_x, put_y)  # 放置棋子
                                grid_list[row][col]["occupy_flag"] = 1  # 放置棋子之后应更改该格的放置标志

                                # out_put_test2(grid)

                                game_result = judge_game(grid_list)
                                print(game_result)
                                if game_result is True:
                                    pygame.event.set_blocked(MOUSEBUTTONDOWN)  # 此时不再响应鼠标的按键按下
                                    game_over_font_display(screen)

                # 放完棋子需要判断当前的游戏状态,是否有胜负
                # judge_game(grid_list)

                pygame.display.update()


# pygame.display.update((150, 150, 300, 300))  # 可以只更新一个矩形区域或者整个窗口


if __name__ == "__main__":
    main()
