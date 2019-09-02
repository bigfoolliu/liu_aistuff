#!-*-coding:utf-8-*-
# !@Date: 2018/8/7 10:02
# !@Author: Liu Rui
# !@github: bigfoolliu


"""简单实例"""
# import tkinter as tk
#
#
# class Application(tk.Frame):
# 	"""自定义的框架类, 继承Frame类"""
# 	def __init__(self):
# 		# super().__init__(master=None)
# 		tk.Frame.__init__(self, master=None)
# 		self.grid()  # 让应用框架显示在屏幕上
# 		self.create_widgets()  # 创建标签
# 		self.quit_button = None
#
# 	def create_widgets(self):
# 		"""创建标签"""
# 		self.quit_button = tk.Button(self, text="Quit", command=self.quit)  # 创建一个按钮
# 		self.quit_button.grid()  # 将按钮放在应用框架上
#
#
# app = Application()
# app.master.title("Sample application")  # 设置窗口标题
# app.mainloop()  # 进入主循环,等待鼠标键盘的事件


"""升级版,退出按钮可以始终处于屏幕的中间位置"""
# import tkinter as tk
#
#
# class Application(tk.Frame):
# 	"""自定义的框架类, 继承Frame类"""
# 	def __init__(self):
# 		# super().__init__(master=None)
# 		tk.Frame.__init__(self, master=None)
# 		# self.grid()  # 让应用框架显示在屏幕上
# 		self.grid(sticky=tk.N+tk.S+tk.E+tk.W)  # 应用框架扩张填充顶级窗口的网格
# 		self.create_widgets()  # 创建标签
# 		self.quit_button = None
#
# 	def create_widgets(self):
# 		"""创建标签"""
# 		top = self.winfo_toplevel()  # 最外面的窗口
# 		top.rowconfigure(0, weight=1)  # 让最外面窗口的0行网格可伸缩
# 		# top.rowconfigure(1, weight=1)  # 让最外面窗口的1行网格可伸缩
# 		top.columnconfigure(0, weight=1)  # 让最外面窗口的0列网格可伸缩
#
# 		self.rowconfigure(0, weight=1)
# 		# self.rowconfigure(1, weight=1)
# 		self.columnconfigure(0, weight=1)
# 		# self.columnconfigure(1, weight=1)
#
# 		self.quit_button = tk.Button(self, text="Quit", command=self.quit)  # 创建一个按钮
# 		self.quit_button.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)  # 将按钮放在应用框架上
#
#
# app = Application()
# app.master.title("Sample application")  # 设置窗口标题
# app.mainloop()  # 进入主循环,等待鼠标键盘的事件


# 快捷键: ctrl + alt + l, 快速对过长的语句换行


"""Button不同的relief"""
# import tkinter as tk
# from tkinter.constants import *
#
# window = tk.Tk()
# tk.Button(window, text="hello", relief=FLAT).pack()
# tk.Button(window, text="hello", relief=GROOVE).pack()
# tk.Button(window, text="hello", relief=RAISED).pack()
# tk.Button(window, text="hello", relief=RIDGE).pack()
# tk.Button(window, text="hello", relief=SOLID).pack()
# tk.Button(window, text="hello", relief=SUNKEN).pack()
#
# window.mainloop()


"""Button和Canvas"""
# import tkinter as tk
# from tkinter.constants import *
#
# window = tk.Tk()
# quit_button = tk.Button(window, text="Quit", command=quit, anchor=NE, bg="red", activebackground="green",
# 						cursor="pirate", width=20, height=10)
# quit_button.pack()
#
# canvas = tk.Canvas(window, bg="blue", width=50, height=20, cursor="heart")
# canvas.pack()
# # canvas.create_oval()
#
# window.mainloop()


"""Checkbutton"""
# import tkinter as tk
# from tkinter.constants import *
#
#
# def check_button_command():
# 	"""命令"""
# 	print("check_button Yes is pressed.")
#
#
# window = tk.Tk()
# check_button = tk.Checkbutton(window, bg="yellow", text="Yes", cursor="dot", command=check_button_command,
# 							  relief=SOLID, state=NORMAL)
#
# check_button.pack()
# window.mainloop()


"""
Entry
绑定变量
var = StringVar()
var.set(), 设定变量的值
var.get(), 获取文本框的值

说明

　　创建单行文本框

用法

　　创建:lb =Entry(根对象, [属性列表])
　　绑定变量 var=StringVar()    lb=Entry(根对象, textvariable = var)
　　获取文本框中的值   var.get()
　　设置文本框中的值   var.set(item1)

"""
# import tkinter as tk
# from tkinter.constants import *
#
# window = tk.Tk()
# window.title("Entry Examples")  # 设置窗口标题
# entry1 = tk.Entry(window, bg="green")
# entry2 = tk.Entry(window, show="*")  # 以*号的形式展现,主要是输入密码时起保护作用
#
# entry1.pack()
# entry2.pack()
#
# window.mainloop()


"""Label"""
# import tkinter as tk
# from tkinter.constants import *
#
# window = tk.Tk()
#
# tk.Label(window, bg="red", text="red", width=10, height=3).pack()
# tk.Label(window, bg="green", text="green", width=10, height=3).pack()
# tk.Label(window, bg="blue", text="blue", width=10, height=3).pack()
# tk.Label(window, bg="yellow", text="welcome to use this tkinter module.", width=10, height=5, wraplength=80,
# 		 justify="left").pack()
#
# window.mainloop()

"""
Listbox

说明

　　列表控件,可以含有一个或多个文本想,可单选也可多选

用法

　　创建:lb = ListBox(根对象, [属性列表])
　　绑定变量 var=StringVar()    lb=ListBox(根对象, listvariable = var)
　　得到列表中的所有值   var.get()
　　设置列表中的所有值   var.set((item1, item2, .....))
　　添加:lb.insert(item)
　　删除:lb.delete(item,...)
　　绑定事件 lb.bind('<ButtonRelease-1>', 函数)
　　获得所选中的选项 lbl.get(lb.curselection())
属性

　　selectmode可以为BROWSE MULTIPL SINGLE

"""
# import tkinter as tk
# from tkinter.constants import *
#
# window = tk.Tk()
# list_box1 = tk.Listbox(window, bg="yellow", relief=SOLID)
#
# list_box1.pack()
# window.mainloop()

"""listbox2"""
# from tkinter import *
#
# root = Tk()
# root.title("hello world")
# root.geometry()
#
#
# def print_item(event):
# 	print(lb.get(lb.curselection()))
#
#
# var = StringVar()
# lb = Listbox(root, listvariable=var)
# list_item = [1, 2, 3, 4]  # 控件的内容为1 2 3 4
# for item in list_item:
# 	lb.insert(END, item)
# lb.delete(2, 4)  # 此时控件的内容为1 3
#
# var.set(('a', 'ab', 'c', 'd'))  # 重新设置了，这时控件的内容就编程var的内容了
# print(var.get())
# lb.bind('<ButtonRelease-1>', print_item)
# lb.pack()
#
# root.mainloop()


"""Menu"""
# import tkinter as tk
# from tkinter.constants import *
#
#
# class Menu(object):
# 	def __init__(self, window_para):
# 		self.mb = tk.Menubutton(window_para, text='condiments', relief=RAISED)
# 		self.mb.grid()
# 		self.mb.menu = tk.Menu(self.mb, tearoff=0)
# 		self.mb['menu'] = self.mb.menu
# 		self.mayoVar = tk.IntVar()
# 		self.ketchVar = tk.IntVar()
# 		self.mb.menu.add_checkbutton(label='mayo', variable=self.mayoVar)
# 		self.mb.menu.add_checkbutton(label='ketchup', variable=self.ketchVar)
#
#
# window = tk.Tk()
#
# menu1 = Menu(window)
#
# window.mainloop()


"""
Text
文本框

向该空间内输入文本
用法
　　t = Text(根对象)
　　插入:t.insert(mark, 内容)
　　删除:t.delete(mark1, mark2)
　　其中,mark可以是行号,或者特殊标识,例如

INSERT:光标的插入点CURRENT:鼠标的当前位置所对应的字符位置
END:这个Textbuffer的最后一个字符
SEL_FIRST:选中文本域的第一个字符，如果没有选中区域则会引发异常
SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发 异常

"""
from tkinter import *

root = Tk()
root.title("hello world")
root.geometry('300x200')

t = Text(root)
t.insert(1.0, 'hello\n')
t.insert(END, 'hello000000\n')
t.insert(END, 'nono')
t.pack()

root.mainloop()


"""
Frame
在屏幕上创建一块矩形区域,多作为容器来布局窗体
用法
　　Frame(根对象, [属性列表])
举例
     要在控件中出现这样的四个词语

                校训

          厚德        敬业

          博学        乐群     
"""
# from tkinter import *
#
# root = Tk()
# root.title("hello world")
# root.geometry('300x200')
#
# Label(root, text="校训", font=('Arial', 20)).pack()
#
# frm = Frame(root)
# # left
# frm_L = Frame(frm)
# Label(frm_L, text="厚德", font=('Arial', 15)).pack(side=TOP)
# Label(frm_L, text='博学', font=('Arial', 15)).pack(side=TOP)
# frm_L.pack(side=LEFT)
#
# # right
# frm_R = Frame(frm)
# Label(frm_R, text="崇实", font=('Arial', 15)).pack(side=TOP)
# Label(frm_R, text="去浮", font=('Arial', 15)).pack(side=TOP)
# frm_R.pack(side=RIGHT)
#
# frm.pack()
#
# root.mainloop()


"""
Scrollbar
"""
# from tkinter import *
#
# root = Tk()
# root.title("hello world")
# root.geometry()
#
#
# def print_item(event):
# 	print(lb.get(lb.curselection()))
#
#
# var = StringVar()
# lb = Listbox(root, height=5, selectmode=BROWSE, listvariable=var)
# lb.bind('<ButtonRelease-1>', print_item)
# list_item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for item in list_item:
# 	lb.insert(END, item)
#
# scrl = Scrollbar(root)
# scrl.pack(side=RIGHT, fill=Y)
# lb.configure(yscrollcommand=scrl.set)
# lb.pack(side=LEFT, fill=BOTH)
# scrl['command'] = lb.yview
#
# root.mainloop()
