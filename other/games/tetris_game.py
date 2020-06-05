#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
基于tkinter的俄罗斯方块
后续希望用AI来自动完成游戏
"""
import tkinter as tf
from tkinter import Canvas, Label, Tk, StringVar, messagebox
import random
import collections

WIDTH = 300
HEIGHT = 500

BOX_SIZE = 20
START_POINT = WIDTH / 2 / BOX_SIZE * BOX_SIZE - BOX_SIZE
# 参考直角坐标系画出各种形状
SHAPES = (
    ("yellow", (0, 0), (1, 0), (0, 1), (1, 1)),  # square
    ("lightblue", (0, 0), (1, 0), (2, 0), (3, 0)),  # line
    ("orange", (2, 0), (0, 1), (1, 1), (2, 1)),  # right el
    ("blue", (0, 0), (0, 1), (1, 1), (2, 1)),  # left el
    ("green", (0, 1), (1, 1), (1, 0), (2, 0)),  # right wedge
    ("red", (0, 0), (1, 0), (1, 1), (2, 1)),  # left wedge
    ("purple", (1, 0), (0, 1), (1, 1), (2, 1))  # symmetrical wedge
)


class Shape(object):
    """游戏界面类"""

    def __init__(self, canvas):
        self.boxes = []
        self.shape = random.choice(SHAPES)
        self.color = self.shape[0]
        self.canvas = canvas

        for point in self.shape[1:]:
            box = canvas.create_rectangle(
                point[0] * BOX_SIZE + START_POINT,
                point[1] * BOX_SIZE,
                point[0] * BOX_SIZE + BOX_SIZE + START_POINT,
                point[1] * BOX_SIZE + BOX_SIZE,
                fill=self.color
            )
            self.boxes.append(box)

    def move(self, x, y):
        """移动位置在(x, y)位置的box"""
        if not self.can_move_shape(x, y):
            return False
        else:
            for box in self.boxes:
                self.canvas.move(box, x * BOX_SIZE, y * BOX_SIZE)
            return True

    def fall(self):
        """下落"""
        if not self.can_move_shape(0, 1):
            return False
        else:
            for box in self.boxes:
                self.canvas.move(box, 0 * BOX_SIZE, 1 * BOX_SIZE)
            return True

    def rotate(self):
        """翻转"""
        boxes = self.boxes[:]
        pivot = boxes.pop(2)

        def get_move_coords(box):
            box_coords = self.canvas.coords(box)
            pivot_coords = self.canvas.coords(pivot)
            x_diff = box_coords[0] - pivot_coords[0]
            y_diff = box_coords[1] - pivot_coords[1]
            x_move = (- x_diff - y_diff) / BOX_SIZE
            y_move = (x_diff - y_diff) / BOX_SIZE
            return x_move, y_move

        for box in boxes:
            x_move, y_move = get_move_coords(box)
            if not self.can_move_box(box, x_move, y_move):
                return False

        for box in boxes:
            x_move, y_move = get_move_coords(box)
            self.canvas.move(box, x_move * BOX_SIZE, y_move * BOX_SIZE)

        return True

    def can_move_box(self, box, x, y):
        """判断(x, y)位置的box是否可以移动"""
        x = x * BOX_SIZE
        y = y * BOX_SIZE
        coords = self.canvas.coords(box)

        if coords[3] + y > HEIGHT:
            return False
        if coords[0] + x < 0:
            return False
        if coords[2] + x > WIDTH:
            return False

        overlap = set(self.canvas.find_overlapping(
            (coords[0] + coords[2] / 2 + x),
            (coords[1] + coords[3] / 2 + y),
            (coords[0] + coords[2] / 2 + x),
            (coords[1] + coords[3] / 2 + y)
        ))
        other_items = set(self.canvas.find_all()) - set(self.boxes)
        if overlap & other_items:  # 重叠
            return False

        return True

    def can_move_shape(self, x, y):
        """判断方块是否会移动"""
        for box in self.boxes:
            if not self.can_move_box(box, x, y):
                return False
        return True


class Game():
    """游戏类"""

    def start(self):
        self.level = 1
        self.score = 0
        self.speed = 500
        self.counter = 0
        self.create_new_game = True

        self.root = Tk()
        self.root.title("Tetris")

        self.status_var = StringVar()
        self.status_var.set("Level: 1, Score: 0")
        self.font = ("Helvetica", 10, "bold")
        self.status = Label(self.root, textvariable=self.status_var, font=self.font)
        self.status.pack()

        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.root.bind("<Key>", self.handle_events)
        self.timer()
        self.root.mainloop()

    def timer(self):
        """"""
        if self.create_new_game == True:
            self.current_shape = Shape(self.canvas)
            self.create_new_game = False

        if not self.current_shape.fall():
            lines = self.remove_complete_lines()
            if lines:
                self.score += 10 * self.level ** 2 * lines ** 2  # 得分计算公式
                self.status_var.set("Level: {}, Score: {}".format(self.level, self.score))

            self.current_shape = GameGrid(self.canvas)
            if self.is_game_over():
                self.create_new_game = True
                self.game_over()

            self.counter += 1
            if self.counter == 5:
                self.level += 1
                self.speed -= 20
                self.counter = 0
                self.status_var.set("Level: {}, Score: {}".format(self.level, self.score))
        self.root.after(self.speed, self.timer)

    def handle_events(self, event):
        """控制用户事件"""
        if event.keysym == "Left":
            self.current_shape.move(-1, 0)
        if event.keysym == "Right":
            self.current_shape.move(1, 0)
        if event.keysym == "Down":
            self.current_shape.move(0, 1)
        if event.keysym == "Up":
            self.current_shape.rotate()

    def is_game_over(self):
        """判断游戏是否结束"""
        for box in self.current_shape.boxes:
            if not self.current_shape.can_move_box(box, 0, 1):
                return True
        return False

    def remove_complete_lines(self):
        """删除完成的行"""
        shape_boxes_coords = [self.canvas.coords(box)[3] for box in self.current_shape.boxes]
        all_boxes = self.canvas.find_all()
        all_boxes_coords = {k: v for k, v in zip(all_boxes, [self.canvas.coords(box)[3] for box in all_boxes])}

        lines_to_check = set(shape_boxes_coords)
        boxes_to_check = dict(
            (k, v) for k, v in all_boxes_coords.iteritems() if any(v == line for line in lines_to_check))

        counter = collections.Counter()
        for box in boxes_to_check.values():
            counter[box] += 1
        complete_lines = [k for k, v in counter.iteritems() if v == WIDTH / BOX_SIZE]

        if not complete_lines:
            return False

        for k, v in boxes_to_check.iteritems():
            if v in complete_lines:
                self.canvas.delete(k)
                del all_boxes_coords[k]

        for (box, coords) in all_boxes_coords.iteritems():
            for line in complete_lines:
                if coords < line:
                    self.canvas.move(box, 0, BOX_SIZE)

        return len(complete_lines)

    def game_over(self):
        """游戏结束"""
        self.canvas.delete(tf.ALL)
        messagebox.showinfo("Game Over", "You scored {} points.".format(self.score))


game = Game()
game.start()
