#!-*-coding:utf-8-*-
# !@Date: 2018/8/12 20:23
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
音效:pygame.mixer
要在游戏中播放碰撞、爆炸、语音等音效，

这个模块支持同时播放多个音效文件，多个文件在多个不同的通道Channel中播放，一个通道一次只能播放一个音效文件。

pygame.init() 进行全部模块初始化
pygame.mixer.init() 只初始化音频部分
pygame.mixer.get_num_channels() 可以这样查看总共有多少个通道
channel = pygame.mixer.Channel(i) 使用取得第i个通道。
channel = pygame.mixer.find_channel() 自动取得一个空闲的通道（没有音效正在播放的通道）。
sound = pygame.mixer.Sound('/home/liumin/love.wav')使用指定文件名载入一个音频文件，并创建一个Sound对象。 音频文件可以是wav,ogg等格 式。音频文件的内容会被全部载入到内存中。
channel.play(sound) 使用在一个通道中播放一个音效。
sound.play() 自动找一个空闲的通道播放音效。
sound.stop() 停止音效sound的播放。或者用
channel.stop() 停止在通道channel中播放的音效。正在播放音效的通道还可以用
channel.pause() 暂停通道中的音效。
channel.unpause() 继续播放。
channel.fadeout(time) 用来进行淡出，在time毫秒的时间内音量由初始值渐变为0，最后停止播放。 对于一个通道可以用 channel.get_busy() 检查它是否正在播放音效。当一个通道中的音效播放完成时，可以通过事件通知给用户程序。
channel.set_endevent(pygame.USEREVENT + 1) 来设置当音乐播放完成时发送pygame.USEREVENT+1事件给用户程序。
channel.queue(sound) 为正在播放音效的通道指定下一个要播放的音效。当前的音效播放完成后，下一个音效会自动播放。一个通道只能有一个等待播放的音效。
channel.set_volume(value) 来设置通道中播放的音效的音量。
sound.set_volume(value) 来设置单个音效的音量。两者的取值范围都是0.0到1.0。音效播放的实际音量是通道音量和音效音量的乘积，比如通道音量0.5，音效音量0.6，则实际播放的音量为0.3。
NOTE： 音效和音乐的区别是：音效要整个文件载入到Sound对象中才能播放，而音乐不用完全载入，而以流的方式播放。


# Sound主要用来加载.ogg 和 .wav格式文件
import pygame

pygame.mixer.init()
channel = pygame.mixer.Channel(2)
sound = pygame.mixer.Sound('yuelao.wav')
while 1:
	if channel.get_busy() == False:
		#sound.play()
		channel.play(sound)



# music主要用来加载.mp3格式文件
import pygame

pygame.mixer.init()
#加载音乐
pygame.mixer.music.load("006.mp3")
while True:
	#检查音乐流播放，有返回True，没有返回False
	#如果没有音乐流则选择播放
	if pygame.mixer.music.get_busy()==False:
		pygame.mixer.music.play()

"""


"""
pygame 按钮组件的事件
"""
from tkinter import *


# .我通常习惯用 event 来表示，如果我们调用的函数不接受任何参数，
# 则会报错如下： TypeError: myLabel() takes no arguments (1 given)
def my_label(event):
    global root
    s = Label(root, text="好好学习")
    s.pack()


root = Tk()
root.wm_title("按钮点击")
root.geometry("400x300+100+50")

b1 = Button(root, text="点击")
# bind 可以接受三个参数，但是本例中我们只传递了两个参数。
# bind 的第一个参数是事件类型，它采用的描述方式是这样的： <MODIFIER-MODIFIER-TYPE-DETAIL>，
# Control, Mod2,M2, Shift, Mod3, M3, Lock, Mod4, M4, Button1, B1,
# Mod5, M5 Button2, B2, Meta, M, Button3,B3, Alt,
# Button4, B4, Double, Button5, B5 Triple， Mod1, M1。
# 第三个 TYPE 表示类型，它的全部取值如下： Activate,Enter, Map, ButtonPress, Button, Expose, Motion
# ButtonRelease， FocusIn, MouseWheel, Circulate,FocusOut, Property, Colormap, Gravity Reparent
# Configure, KeyPress, Key, Unmap, Deactivate,KeyRelease Visibility, Destroy,Leave。
# 第三个参示细节，其实也就是对第二个参数的一些辅助说明
# 第一个参数可能对刚使用它的人来说有点太复杂了，常见的鼠标左键单击如下:<Button-1>,
# 也就是我上面的代码中用到的
# 第二个参数可以是一个函数名，记住，不要加任何的标点符号，否则运行时会报错的。
# 使用 bind 函数的时候，第二个参数是一个函数名，该函数必须接受一个参数，即表示该事件
b1.bind("<Button-1>", my_label)
b1.pack()

root.mainloop()
