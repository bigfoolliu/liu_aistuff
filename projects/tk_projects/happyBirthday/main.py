#!-*-coding:utf-8-*-
# !@Date: 2018/8/12 9:00
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
tkinter + pygame + 所线程
一个线程用来播放音乐
另一个线程用来接收界面的操作
"""

from tkinter import *
import pygame
import threading
import time


class AppUI(object):
	"""UI"""

	def __init__(self):
		# 定义主窗口
		self.screen = Tk()
		self.screen.title("生日歌播放器(by bigfoolliu)")
		self.screen.resizable(width=False, height=False)

		# 关键代码语句, 关闭程序时执行的语句
		self.screen.protocol('WM_DELETE_WINDOW', self.close_window)

		# 定义上下两个区域
		self.frame_top = Frame(self.screen, width=400, height=80, bg="white")
		self.frame_down = Frame(self.screen, width=400, height=80, bg="white")
		self.frame_top.propagate(0)
		self.frame_down.propagate(0)

		# 配置上下两片区域的大小及位置
		self.frame_top.pack(fill=BOTH, padx=5, pady=2.5)
		self.frame_down.pack(fill=BOTH, padx=5, pady=2.5)

		# 定义按钮以及标签变量
		self.music_name = StringVar()
		self.pause_resume = StringVar()

		# 定义按钮以及标签
		self.label_display = Label(self.frame_top, bg="#2CA3A8", textvariable=self.music_name, font=("arial", 20))
		self.button_start = Button(self.frame_down, text="Start", font=("arial", 15), bg="#91BEFE",
								   command=self.button_play_click)
		self.button_pause = Button(self.frame_down, textvariable=self.pause_resume, font=("arial", 15), bg="#91BEFE",
								   command=self.pause_click)
		# 定义按钮初始状态
		self.pause_resume.set("Pause")
		self.button_pause["state"] = "disabled"

		# 配置按钮以及标签位置
		self.label_display.pack(fill=BOTH, expand=1)
		self.button_pause.pack(fill=BOTH, expand=1, side=LEFT, padx=2)
		self.button_start.pack(fill=BOTH, expand=1, side=LEFT, padx=2)

		self.play_flag = 0

	def button_play_click(self):
		"""按下播放按钮"""
		# 创建线程来播放音乐,主线程用来播放音乐
		self.play_flag = 1
		play_threading = threading.Thread(target=self.play)
		play_threading.setDaemon(0)
		play_threading.start()

		# 该表按钮的状态
		self.button_start["state"] = "disabled"
		self.button_pause["state"] = "normal"

	def play(self):
		"""播放音乐以及显示歌词"""
		pygame.mixer.init()

		while self.play_flag:  # 子线程持续监听播放标志

			if not pygame.mixer.music.get_busy():  # 如果当前没有其他正在播放的音乐
				print("当前正在播放歌曲: It‘s your day.mp3...")
				self.music_name.set("It‘s your day.mp3 playing...")
				pygame.mixer.music.load("res/It‘s your day.mp3")  # 加载音乐
				pygame.mixer.music.play(1)  # 播放一次, 注意这里是流的方式播放, 运行会持续进行,代码块均会执行

			else:
				time.sleep(0.2)

	def pause_click(self):
		"""暂停与重新开始播放"""
		if self.pause_resume.get() == 'Pause':
			pygame.mixer.music.pause()
			self.pause_resume.set('Resume')

		elif self.pause_resume.get() == 'Resume':
			pygame.mixer.music.unpause()
			self.pause_resume.set('Pause')

	def close_window(self):
		"""关闭窗口"""
		self.play_flag = 0
		try:
			# 停止播放，如果已停止，再次停止时会抛出异常，所以放在异常处理结构中
			pygame.mixer.music.stop()
			pygame.mixer.quit()
		except:
			print("结束进程出现错误!")
		self.screen.destroy()


if __name__ == '__main__':
	app_ui = AppUI()  # 界面初始化
	app_ui.screen.mainloop()
