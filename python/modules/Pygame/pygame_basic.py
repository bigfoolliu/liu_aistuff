#!-*-coding:utf-8-*-
# !@Date: 2018/7/18 23:03
# !@Author: Liu Rui
# !@github: bigfoolliu

"""
pygame模块包含的模块

pygame.cdrom		  访问光驱

pygame.cursors      加载光标

pygame.display      访问显示设备

pygame.draw         绘制形状,线和点

pygame.event        管理事件

pygame.font         使用字体

pygame.image        加载和存储图片

pygame.joystick     使用游戏手柄或者类似的东西

pygame.key          读取键盘按键

pygame.mixer        声音

pygame.mouse        鼠标

pygame.movie        播放视频

pygame.music        播放音频

pygame.overlay      访问高级视频叠加

pygame.rect         管理矩形区域

pygame.sndarray     操作声音数据

pygame.sprite       操作移动图像

pygame.surface      管理图像和屏幕

pygame.surfarray    管理点阵图像数据

pygame.time         管理时间和帧信息

pygame.transform    缩放和移动图像

pygame              本地库
"""
import pygame
from pygame.locals import *  # 导入一些常用的函数和变量
from sys import exit  # 借exit函数退出程序


background_image_filename = "background.jpg"
mouse_image_filename = "follow_mouse.jpg"

# 初始化pygame,为使用硬件做准备
pygame.init()

# 创建一个640*480的窗口,标志位为XX,色深为32
"""
标志位可以指定窗口的特性

0             无任何特性

FULLSCREEN    创建全屏窗口

DOUBLEBUF     创建一个"双缓冲"窗口,建议在HWSURFACE或OPENGL使用

HWSURFACE     创建一个硬件加速窗口,必须和FULLSCREEN同时使用

OPENGL        创建一个OPENGL渲染的窗口

RESIZABLE     创建一个可改变大小的窗口

NOFRAME       创建一个没有边框的窗口
"""
screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)  # set_mode返回的是一个surface对象

# 设置窗口标题
pygame.display.set_caption("LR' first pygame demo.")

# 加载并转换图像
background = pygame.image.load(background_image_filename)
mouse_cursor = pygame.image.load(mouse_image_filename)

screen.blit(background, (0, 0))  # 此句应该删除
# 游戏主循环
while True:
	for event in pygame.event.get():
		if event.type == QUIT:  # 接收到退出事件后退出程序
			exit()

	# 画背景图,尽管背景图不动,但是仍然需要更新,否则鼠标经过的地方不能恢复
	# blit函数,第一个参数代表surface对象,第二个为左上角位置
	# screen.blit(background, (0, 0))
	# 获得鼠标位置
	x, y = pygame.mouse.get_pos()
	# 计算光标左上角的位置
	x -= mouse_cursor.get_width() / 2
	y -= mouse_cursor.get_height() / 2
	# 将光标画上去
	screen.blit(mouse_cursor, (x, y))

	# 刷新画面
	pygame.display.update()


# """
# pygame的事件
#
# pygame.event.get()     获取事件,相当于打开大门处理所有的事件
# pygame.event.wait()    发生一个事件才继续下去
# 两者在真正的游戏中不太实用
#
# pygame.event.poll()    一旦调用,会根据现在的情形返回一个真实的事件,或者返回"什么都不发生"
#
# 常见事件集:
#
# 事件                   产生途径                      参数
#
# QUIT                  用户按下关闭按钮                none
#
# ATIVEEVENT            pygame被激活或者隐藏           gain,state
#
# KEYDOWN               键盘被按下                     unicode,key,mod
#
# KEYUP                 键盘被放开                     key,mod
#
# MOUSEMOTION           鼠标移动                       pos,rel,buttons
#
# MOUSEBUTTONDOWN       鼠标按下                       pos,button
#
# MOUSEBUTTONUP         鼠标放开                       pos,button
#
# JOYAXISMOTION         (joystick or pad)移动         joy,axis,value
#
# JOYBALLMOTION         (joy ball)移动                joy,axis,value
#
# JOYHATMOTION          (joy hat)移动                 joy,axis,value
#
# JOYBUTTONDOWN         (joy button)按下              joy,button
#
# JOYBUTTONUP           (joy button)放开              joy,button
#
# VIDEORESIZE           pygame窗口缩放                 size,w,h
#
# VIDEOEXPOSE           pygame窗口(expose)             none
#
# USEREVENT             触发了一个用户事件               code
# """
# # 程序功能:
# # 当鼠标在窗口里移动时,将触发的事件显示在窗口里
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
# SCREEN_SIZE = (640, 480)
# screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
#
# # 设置字体样式和字体大小
# font = pygame.font.SysFont("arial", 16)
# font_height = font.get_linesize()
# event_text = []
#
# while True:
# 	event = pygame.event.wait()
# 	event_text.append(str(event))  # 获得时间的名称
# 	# print(event_text)
# 	# 该操作应保证event_text里只保留一个屏幕的文字,但报错
# 	event_text = event_text[-SCREEN_SIZE[1]/font_height:]
#
# 	if event.type == QUIT:
# 		exit()
#
# 	screen.fill((255, 255, 255))
#
# 	y = SCREEN_SIZE[1] - font_height
# 	for text in reversed(event_text):
# 		screen.blit(font.render(text, True, (0, 0, 0)), (0, 0))
# 		y -= font_height
#
# 	pygame.display.update()


# """
# 处理键盘事件
#
# 按下键盘的方向键可以移动背景图片
# """
# import pygame
# from pygame.locals import *
# from sys import exit
#
# background_image_filename = "background.jpg"
#
# pygame.init()
# screen = pygame.display.set_mode((1000, 640), 0, 32)
# background = pygame.image.load(background_image_filename)
#
# # 设置图像的目标位置坐标和单次移动的距离
# x, y = 0, 0
# move_x, move_y = 0, 0
#
# while True:
# 	# 持续监测事件
# 	for event in pygame.event.get():
# 		if event.type == QUIT:
# 			exit()
# 		# 如果有键盘被按下
# 		if event.type == KEYDOWN:
# 			if event.key == K_LEFT:  # 按下左方向键
# 				move_x = -10
# 			elif event.key == K_RIGHT:  # 按下右方向键
# 				move_x = 10
# 			elif event.key == K_UP:  # 按下上方向键
# 				move_y = -10
# 			elif event.key == K_DOWN:  # 按下下方向键
# 				move_y = 10
# 		# 如果用户放开了键盘,图不动
# 		elif event.type == KEYUP:
# 			move_x = 0
# 			move_y = 0
#
# 		x += move_x
# 		y += move_y
#
# 		screen.fill((0, 255, 0))  # 窗口填充绿色
# 		screen.blit(background, (x, y))
#
# 		# 在新的位置画图
# 		pygame.display.update()


"""
窗口的大小可调整,背景图片可根据窗口的大小调整数量
铺满整个窗口
"""
# import pygame
# from pygame.locals import *
# import sys
#
# # 设置窗口的背景图片名
# background_image_filename = "background.jpg"
#
# # 设置默认的窗口尺寸
# SCREEN_SIZE = (640, 480)
#
# # pygame初始化
# pygame.init()
# # 设置窗口
# screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
# # 设置背景
# background = pygame.image.load(background_image_filename)
#
# while True:
# 	event = pygame.event.wait()  # 等待事件触发
# 	if event == QUIT:
# 		sys.exit()
# 	# 如果为设置尺寸事件,即点击窗口右下角拖动
# 	if event.type == VIDEORESIZE:
# 		SCREEN_SIZE = event.size
# 		screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
# 		pygame.display.set_caption("windows resized to" + str(event.size))
#
# 	screen_width, screen_height = SCREEN_SIZE
#
# 	# 根据窗口大小,将背景图片铺满整个窗口
# 	for y in range(0, screen_height, background.get_height()):
# 		for x in range(0, screen_width, background.get_width()):
# 			screen.blit(background, (x, y))
#
# 	pygame.display.update()
