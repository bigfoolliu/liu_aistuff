#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
一。方法

1.forward() | fd():向前移动指定的距离。参数：一个数字（integer or float)）。
turtle.forward(25)

2.backward() | bk() | back():向后移动指定的距离。参数：一个数字（integer or float)）。
turtle.backward(30)

3..right() | rt():以角度单位向右转动。参数：一个数字（integer or float)）。单位默认为度数，可以通过degrees()和radians()进行设置。
turtle.right(45)

4.left() | lt():以角度单位向左转动。参数：一个数字（integer or float)）。单位默认为度数，可以通过degrees()和radians()进行设置。
turtle.left(45)

5.goto() | steps() | setposition()：移动到绝对位置，如果笔落下，画线，不改变方向。参数：x-一个数字或一对数字。y-一个数字或None。
turtle.setpos(60,30)
#60.00，30.00）

6.setx():设置第一个坐标的值即X方向。参数：一个数字（integer or float)）。
turtle.setx(10)
#（10.00，0.00）

7.sety():设置第二个坐标的值即Y方向。参数：一个数字（integer or float)）。
turtle.sety(10)
#（0.00，10.00）

8.setheading() | seth(): 将方向设置为to_angle.就是东西南北方向。具体如下：
标准模式：0 - 东  90 - 北 180 - 西 270 - 南  标志模式 0- 北   90- 东    180- 南    270 - 西
turtle.setheading(90)

9.home() : 移动到原点 - 坐标（0，0）：并将其标题设置为其起始方向（取决于模式）。
turtle.home()
# （0.00，0.00）

10.circle()：绘制一个给定半径的圆。参数：radius-一个数字（半径，如果值为正则逆时针，负数为顺时针），extent-一个数字（）steps- 执行的步数。
turtle.circle(120,180,5)

11.dot() ：用颜色画出一个直径大小的圆点。参数：size-一个大于1的整数，可None。默认用的是pensize+4和2*pensize的最大值，color-颜色值
turtle.dot(20, "blue")

12.stamp():将当前位置上的形状复制到画布上返回stamp_id.可以调用，可以删除。
turtle.stamp()

13.clearstamp():删除stamp()返回来的值。参数：stampid。

14.clearstamps():删除全部stamp()的值。参数：stampid。

15.undo():撤销最后的动作。

16.speed():将速度设置为0..10范围内整数。如果没有参数，则返回当前速度。如果大于10或者小于0.5，则速度设置为0 。
“最快”：0 ：直接成图，没有动画效果
“快”：10：大概一秒
“正常”：6：
“慢”：3
“最慢”：1

17:position() | pos(): 返回当前的位置。
turtle.pos()
# （0.00，0.00）

18.towards(): 返回当前位置同指定位置之间的角度。参数：x-一个数字或一对数字或一个实例的向量,y-如果x是数字，则为数字，否则为None。
turtle.goto(10,10)
tw = turtle.towards(0,0)
print(tw)
# 225

19.xcor():返回x坐标。
	ycor():返回y坐标。

20.heading(): 返回当前的方向值。

21.distance():返回x，y两个点的直线距离

22.degrees():设置一整圈的度数。默认是360度。

23.radians():将角度测量单位设置为弧度。相当于 degrees(2*math.pi)

24.pendown() | pd() | down():放下笔，移动的时候绘图。

25.penup() | pu() | up():将提起笔，移动时无图。

26.pensize():设置线条的粗细。参数：width-一个正数

27.pen():使用键值对设置笔的属性：
“shown”: True/False
“pendown”: True/False
“pencolor”: 颜色字符串或者颜色值
“fillcolor”: 颜色字符串或者颜色值
“pensize”: 正数
“speed”: 速度范围为0..10的数字
“resizemode”: “auto” or “user” or “noresize”
“stretchfactor”: (positive number, positive number)
“outline”: 正数
“tilt”: 正数

28.isdown()：如果笔停止返回True，反之False

29.pencolor():设置笔的颜色。

30.fillcolor():笔的填充色。

31.color():同时设置pencolor和fillcolor

32.filling():返回fillstate状态，如果填充则返回True，反之False。

33.begin_fill():在绘制要填充的形状前调用。当然在调用完还需要end_fill()。

34.reset():重置，将屏幕中的图纸删除，重新居中并将所有变量设置为默认值。

35.clear():删除图纸。对属性不做操作。

36.write():写文本。参数：arg-要写入的对象。move-是否移动。align-对齐方式：left，right，center。font-字体。fontname，fontsize，fonttype。

37.hideturtle() | ht() :删隐藏乌龟的形状，在做复杂绘图的时候隐藏的时候有利于提高绘图速度。

38.showturtle() | st():显示乌龟的形状。

39.isvisible():乌龟是否可见。如果可见返回True，反之则False。

40.shape():设置乌龟的图形形状，取值:“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”

41.isvisible():乌龟是否可见。如果可见返回True，反之则False。

42.resizemode():参数：rmode取值："auto"，"user","noresize".

43.shapesize() | turtlesize() : 返回笔的属性。

44.shearfactor(): 设置或者返回但钱的剪切因子。

45.tilt():旋转由turtle shape角度从当前的倾斜角度。

46.settiltangle():无论当前的倾斜角度如何，旋转乌龟指向 angle 指定的方向。参数：angle -数字。已弃用

47.tiltangle():设置或者返回当前的倾斜角度。参数：angle - 数字

48.shapetransform():设置或返回乌龟的形状的当前转换矩阵。

49.get_shapepoly():返回当前形状的坐标。

50.onclick():鼠标点击事件。参数：fun-一个带有两个参数的函数，这些参数将与画布上单击点的坐标一个调用。num-鼠标按钮的数量，默认为1(左键)。add- True的时候将添加新的绑定。否则替换以前的绑定。

51.onrelease():鼠标释放事件。参数同点击事件。

52.ondrag():鼠标移动事件。参数同点击事件。

53.begin_poly(): 开始记录多边形的顶点。

54.end_poly():停止记录多边形的顶点。

55.get_poly():返回最后记录的多边形。

56.clone():创建并返回具有相同位置等等属性的乌龟克隆。

57.getturtle() | getpen() :获取trutle对象本身。

58.getscreen()：返回正在绘制的对象。

59.setundobuffer(): 设置或禁用中断器。参数： size-整数。如果大小是None，则禁用缓冲区。

60.undobufferentries():返回undobuffer中的条目数。

61.bgcolor():设置或者返回当前的TurtleScreen的背景颜色。

62.bgpic():设置背景图片。参数： picname-文件名。

62.delay(): 设置或返回以毫秒为单位的绘制延迟，延迟越大，绘图越慢。

63.ontimer():定时器。

64.mainloop() | done() :开始循环 。

65.textinput() | numinput():弹出一个输入字符串和数字的窗口。

66.mode(): 三种方式：“standard”, “logo” or “world”
"""


"""
(1)什么是turtle
Turtle是python内嵌的绘制线、圆以及其他形状（包括文本）的图形模块。

(2)turtle函数的使用
turtle.pendown() # 放下画笔 
turtle.penup() # 抬起画笔 
turtle.pensize(int) # 设置画笔宽度，值为整数型 
turtle.forward(float) # 讲话比向前移动一定的角度 
turtle.backward(float) # 将画笔向后移动一定的角度 
turtle.right(angle) # 将画笔右转一定的角度 
turtle.left(angle) # #将画笔左转一定的角度 
turtle.goto(x,y) # 将画笔移动到一个指定的绝对坐标 
turtle.setx(x) # 设置画笔向x方向移动的距离，值为实数 
turtle.sety(y) # 设置画笔向y方向移动的距离，值为实数 
turtle.setheading(angle) # 设定turtle箭头的方向为指定方向，0–东 90—北 
turtle.home() # 将画笔返回到原点 
turtle.circle(r,ext,steps=int) # 绘制一个设置半径和阶数的圆(设置之后会绘制多边形) 
turtle.dot(d,color) # 绘制一个指定直径的圆点，颜色为字符串类型 
turtle.undo() #取消最后一个图操作 
turtle.speed(s) # 设置画笔颜色，为整数类型，且取值在1-10之间 
turtle.color(‘str’) # 设置画笔颜色，为字符串类型 
turtle.fillcolor(‘str’) # 设置填充颜色，为字符串类型 
turtle.begin_fill() # 结束填充 
turtle.end_fill() # 开始填充 
turtle.filling() # 返回填充状态，True表示填充，False表示没有填充 
turtle.clear() # 清除窗口所有内容 
turtle.reset() # 清除窗口，将状态和位置复位为初始值 
turtle.screensize(w,h) # 设置turtle显示的大小，并设置宽度和高度 
turtle.hideturtle() # 隐藏turtle箭头 
turtle.showturtle() # 显示turtle窗口 
turtle.done() # 使turtle窗口不会自动消失 
turtle.isvisible() # 如果turtle可见，返回turtle 
turtle.write(‘str’,font=(“Arial”,8,”normal”)) # 在turtle位置编写字符串s，字体由字体名、字体大小、字体类型三部分组成 
turtle.position() # 获取画笔的坐标，返回一个元组，值为浮点型
"""