#!-*-coding:utf-8-*-
# !@Date: 2018/8/12 10:31
# !@Author: Liu Rui
# !@github: bigfoolliu


import tkinter as tk
import os
import pygame as pg

w, h = 500, 200

# Add a couple widgets. We're going to put pygame in `embed`.
root = tk.Tk()
embed = tk.Frame(root, width=w, height=h)
embed.pack()
text = tk.Button(root, text='Blah.')
text.pack()

# Tell pygame's SDL window which window ID to use
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

# The wxPython wiki says you might need the following line on Windows
# (http://wiki.wxpython.org/IntegratingPyGame).
# os.environ['SDL_VIDEODRIVER'] = 'windib'

# Show the window so it's assigned an ID.
root.update()

# Usual pygame initialization
pg.display.init()
screen = pg.display.set_mode((w, h))

pos = 0
while 1:
    # Do some pygame stuff
    screen.fill((0, 0, 0))
    pos = (pos + 1) % screen.get_width()
    pg.draw.circle(screen, (255, 255, 255), (pos, 100), 30)

    # Update the pygame display
    pg.display.flip()

    # Update the Tk display
    root.update()
