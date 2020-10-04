#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
github地址： https://github.com/PySimpleGUI/PySimpleGUI
参考文档：https://pysimplegui.readthedocs.io/en/latest/call%20reference/

目前运行方式，只能在终端, python3
"""

import PySimpleGUI as sg

# sg.theme('DarkAmber')  # Add a touch of color
sg.theme('Dark')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')],
          [sg.Combo(values=[1, 2, 3]), sg.Listbox(values=['a', 'b', 'c'])],
          [sg.Checkbox(text='hello'), sg.Spin(values=['a', 'b'])]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
