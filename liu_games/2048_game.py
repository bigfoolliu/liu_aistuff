#!/usr/bin/env python
#!coding:utf-8


"""
基于python和tkinter做的一个2048小游戏
"""


import random
import numpy as np
from tkinter import Frame, Label, CENTER
import datetime

WIDTH = 400
HEIGHT = 400
LABEL_WIDTH = 5
LABEL_HEIGHT = 2
BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"

GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_DICT = {
        2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
        32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
        512: "#edc850", 1024: "#edc53f", 2048: "#edc22e", 4096: "#eee4da",
        8192: "#edc22e", 16384: "#f2b179", 32768: "#f59563", 65536: "#f67c5f"
        }

CELL_COLOR_DICT = {
        2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
        32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
        512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2", 4096: "#776e65",
        8192: "#f9f6f2", 16384: "776e65", 32768: "#776e65", 65536: "#f9f6f2"
        }

FONT = ("Verdana", 40, "bold")

KEY_UP_ALT = "\'\\uf700\'"
KEY_DOWN_ALT = "\'\\uf701\'"
KEY_LEFT_ALT = "\'\\uf702\'"
KEY_RIGHT_ALT = "\'\\uf703\'"

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"
KEY_BACK = "'b'"


def show_time():
    """显示当前时间"""
    return datetime.datetime.now().isoformat()

def new_game(n):
    """创建一个新的游戏"""
    print("[INFO]{}:Begin to create a new game.".format(show_time()))
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    print("[INFO]{}:Create the game mat complete, the mat:{}".format(show_time(), matrix))
    return matrix

def add_two(mat):
    """在一个空的格子里产生一个2"""
    print("[INFO]{}:To generate a new 2 in empty cell.".format(show_time()))
    a = random.randint(0, len(mat) - 1)
    b = random.randint(0, len(mat) - 1)
    while (mat[a][b] != 0):
        a = random.randint(0, len(mat) - 1)
        b = random.randint(0, len(mat) - 1)
    mat[a][b] = 2
    print("[INFO]{}:Generate 2 complete, the mat:{}".format(show_time(), mat))
    return mat

def game_state(mat):
    """当前游戏的状态"""
    print("[INFO]{}:To show the state of the game.".format(show_time()))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return "Win"
    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j + 1] == mat[i][j]:
                return "Not over"
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return "Not over"
    for k in range(len(mat) - 1):
        if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
            return "Not over"
    for j in range(len(mat) - 1):
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return "Not over"
    return "Lose"

def reverse(mat):
    """将整个矩阵反转，[[1, 2], [3, 4]]--->[[2, 1], [4, 3]]"""
    print("[INFO]{}:To reverse the mat vertically.".format(show_time()))
    tmp = np.array([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
    new = np.dot(mat, tmp).tolist()
    print("[INFO]{}:Reverse the mat complete.".format(show_time()))
    return new

def transpose(mat):
    """将整个矩阵转置，[[1, 2], [3, 4]]--->[[1, 3], [2, 4]]"""
    print("[INFO]{}:To reverse the mat horizontally.".format(show_time()))
    new = np.array(mat).T.tolist()  # 使用numpy将列表转换为矩阵求转置再转换为列表
    print("[INFO]{}:Transpose the mat complete.".format(show_time()))
    return new

def cover_up(mat):
    """朝左侧覆盖空格"""
    print("[INFO]{}:To cover up the frame.".format(show_time()))
    new = [[0, 0, 0, 0] for i in range(4)]
    done = False
    for i in range(4):
        count = 0
        for j in range(4):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    print("[INFO]{}:Cover up the frame complete.".format(show_time()))
    return (new, done)

def merge(mat):
    """合并可翻倍的网格"""
    print("[INFO]{}:Begin to merge.".format(show_time()))
    done = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    print("[INFO]{}:Merge complete.".format(show_time()))
    return (mat, done)

def up(game):
    print("[INFO]{}:Up pressed".format(show_time()))
    game = transpose(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(game)
    return (game, done)

def down(game):
    print("[INFO]{}:Down pressed".format(show_time()))
    game = reverse(transpose(game))
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return (game, done)

def left(game):
    print("[INFO]{}:Left pressed".format(show_time()))
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    return (game, done)

def right(game):
    print("[INFO]{}:Right pressed".format(show_time()))
    game = reverse(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = reverse(game)
    return (game, done)


class GameGrid(Frame):
    """游戏界面类"""
    def __init__(self):
        """游戏界面初始化"""
        print("[INFO]{}:Initialize the frame.".format(show_time()))
        Frame.__init__(self)

        self.grid()
        self.master.title("2048")
        self.master.bind("<Key>", self.key_down)

        self.commands = {
                KEY_UP: up,
                KEY_DOWN: down,
                KEY_LEFT: left,
                KEY_RIGHT: right,
                KEY_UP_ALT: up,
                KEY_DOWN_ALT: down,
                KEY_LEFT_ALT: left,
                KEY_RIGHT_ALT: right
                }
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()

    def init_grid(self):
        """初始化网格"""
        print("[INFO]{}:Initialize the grid.".format(show_time()))
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=WIDTH, height=HEIGHT)
        background.grid()

        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=WIDTH / GRID_LEN, height=HEIGHT / GRID_LEN)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=LABEL_WIDTH, height=LABEL_HEIGHT)
                t.grid()
                grid_row.append(t)
            
            self.grid_cells.append(grid_row)
        print("[INFO]{}:Initialize the grid complete.".format(show_time()))

    def gen(self):
        """随机生成数字"""
        return random.randint(0, GRID_LEN - 1)

    def init_matrix(self):
        """初始化矩阵"""
        print("[INFO]{}:Initialize the matrix".format(show_time()))
        self.matrix = new_game(4)
        self.history_matrix = list()
        self.matrix = add_two(self.matrix)
        self.matrix = add_two(self.matrix)
        print("[INFO]{}:Initialize the mattrix complete.".format(show_time()))

    def update_grid_cells(self):
        """更新网格"""
        print("[INFO]{}:Update the grid cells".format(show_time()))
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0 :
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_DICT[new_number], fg=CELL_COLOR_DICT[new_number])
        self.update_idletasks()
        print("[INFO]{}:Update the gride cells complete.".format(show_time()))

    def key_down(self, event):
        """按下键盘"""
        print("[INFO]{}:Key pressed".format(show_time()))
        key = repr(event.char)
        if key == KEY_BACK and len(self.history_matrix) > 1:
            self.matrix = self.history_matrix.pop()
            self.update_grid_cells()
            print("[INFO]{}:Back on step totall step:{}".format(show_time(), len(self.history_matrix)))
        elif key in self.commands:
            self.matrix, done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = add_two(self.matrix)
                self.history_matrix.append(self.matrix)
                self.update_grid_cells()
                done = False
                if game_state(self.matrix) == "Win":
                    self.grid_cells[1][1].configure(text="You", bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win", bg=BACKGROUND_COLOR_CELL_EMPTY)
                if game_state(self.matrix) == "Lose":
                    self.grid_cells[1][1].congigure(text="You", bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose", bg=BACKGROUND_COLOR_CELL_EMPTY)

    def generate_text(self):
        """生成文本"""
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2


game_grid = GameGrid()
