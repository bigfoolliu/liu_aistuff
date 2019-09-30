#!-*-coding:utf-8-*-
# !@Date: 2018/8/7 9:04
# !@Author: Liu Rui
# !@github: bigfoolliu


"""

"""

# import tkinter
# from tkinter.constants import *
#
#
# tk = tkinter.Tk()  # 建立一个顶层窗口
#
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH, expand=1)
#
# tk.mainloop()


"""
tkinter.messagebox
"""
# import tkinter.messagebox
#
# message = tkinter.messagebox.showinfo("Hello", "hello, tkinter.messagebox")  # 直接显示提示消息
# print(message)
#
# tkinter.messagebox.showerror("error", "input error")  # 显示错误消息
# tkinter.messagebox.showwarning("warning", "password too short")  # 显示警告消息


# import tkinter
# from tkinter.constants import *
# tk = tkinter.Tk()
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2, bg="green")
# frame.pack(fill=BOTH, expand=1)
# label = tkinter.Label(frame, text="Hello, World", bg="red")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame, text="Exit", bg="yellow", command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()


"""tkinter.Variable()"""
# import tkinter
# from tkinter import *
#
# tk = Tk()
# var = tkinter.Variable(tk)
# print(type(var))
# var.set("hello, world!")
# print(var.get())
# tk.mainloop()


"""tkinter的按钮命令以及事件event"""
# import tkinter
# from tkinter import *
# import time
# import threading
#
#
# def press_button():
# 	"""按钮函数"""
# 	print("press_button pressed.")
# 	if var.get() == "press":
# 		var.set("haha")
# 	else:
# 		var.set("press")
#
#
# def press_button2(event):
# 	"""事件函数"""
# 	print("press_button pressed.")
# 	if var.get() == "press":
# 		var.set("haha")
# 	else:
# 		var.set("press")
#
#
# tk = Tk()
# var = tkinter.Variable()
# var.set("press")
# button = Button(tk, text=var.get(), bg="green", command=press_button, textvariable=var)
# button.pack(fill=BOTH, expand=1)
#
# label = Label(tk, text=var.get(), bg="red", textvariable=var)
# label.bind("<ButtonPress-1>", press_button2)
# label.pack(fill=BOTH, expand=1)
#
# tk.mainloop()


from tkinter import *


def key(event):
    print("pressed", repr(event.char))


def call_back(event):
    print("clicked at", event.x, event.y)


tk = Tk("Test")
frame = Frame(tk, width=200, height=200, bg="green")
frame.bind("<Key>", key)
frame.bind("<Button-1>", call_back)
frame.pack()

menu = Menu(tk)

tk.mainloop()
