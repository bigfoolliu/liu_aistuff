#!-*-coding:utf-8-*-
# !@Date: 2018/8/8 9:01
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
.grid()网格化构件位置



grid布局
grid布局又被称作网格布局，是最被推荐使用的布局。程序大多数都是矩形的界面，我们可以很容易把它划分为一个几行几列的网格，然后根据行号和列号，将组件放置于网格之中。使用grid 布局时，需要在里面指定两个参数，分别用row 表示行，column 表示列。需要注意的是 row 和 column 的序号都从0 开始。

grid属性设置
属性名	属性简析	取值	取值说明
row、column	row为行号，column为列号，设置将组件放置于第几行第几列	取值为行、列的序号，不是行数与列数	row 和 column 的序号都从0 开始
sticky	设置组件在网格中的对齐方式	N、E、S、W、NW、NE、SW、SE、CENTER	类似于pack布局中的锚选项
rowspan	组件所跨越的行数	跨越的行数	取值为跨越占用的行数，而不是序号
columnspan	组件所跨越的列数	跨越的列数	取值为跨越占用的列数，而不是序号
ipadx、ipady、padx、pady	组件的内部、外部间隔距离，与pack的该属性用法相同	同pack	同pack
grid类提供了下列函数（使用组件实例对象调用）：
函数名	描述
grid_slaves()	以列表方式返回本组件的所有子组件对象。
grid_configure(option=value)	给pack布局管理器设置属性，使用属性（option）= 取值（value）方式设置
grid_propagate(boolean)	设置为True表示父组件的几何大小由子组件决定（默认值），反之则无关。
grid_info()	返回pack提供的选项所对应得值。
grid_forget()	Unpack组件，将组件隐藏并且忽略原有设置，对象依旧存在，可以用pack(option, …)，将其显示。
grid_location(x, y)	x, y为以像素为单位的点，函数返回此点是否在单元格中，在哪个单元格中。返回单元格行列坐标，(-1, -1)表示不在其中
size()	返回组件所包含的单元格，揭示组件大小。
"""
from tkinter import *

tk = Tk()
tk.resizable(width=False, height=False)

frame = Frame(tk)
frame.grid()  # 在tk的(0行0列)
Label(frame, text="标签1").grid(row=0, sticky=W)  # 在tk的0行(0列),靠左
Label(frame, text="标签2").grid(row=1, sticky=E)  # 在tk的1行(0列),靠右

e1 = Entry(frame)
e2 = Entry(frame)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

frame2 = Frame(tk)
frame2.grid(row=1)
Button(frame2, text="按钮1", relief=SOLID).grid(row=0, padx=10, pady=10)
Button(frame2, text="按钮2", relief=SOLID).grid(row=0, column=1, columnspan=2, rowspan=2, padx=20, pady=20,
											  sticky=N + W + E + S)
Button(frame2, text="按钮3", relief=SOLID).grid(row=1, sticky=N + W + E + S)

tk.mainloop()

"""
pack打包构件位置


pack布局

pack常用属性:
属性名	属性简析	取值	取值说明
fill	设置组件是否向水平或垂直方向填充	X、Y、BOTH 和NONE	fill = X（水平方向填充）fill = Y（垂直方向填充）fill = BOTH（水平和垂直）NONE 不填充
expand	设置组件是否展开，当值为YES时，side选项无效。组件显示在父容器中心位置；若fill选项为BOTH,则填充父组件的剩余空间。默认为不展开	YES 、NO（1、0）	expand=YES expand=NO
side	设置组件的对齐方式	LEFT、TOP、RIGHT、BOTTOM	值为左、上、右、下
ipadx、ipady	设置x方向（或者y方向）内部间隙（子组件之间的间隔）	可设置数值，默认是0	非负整数，单位为像素
padx、pady	设置x方向（或者y方向）外部间隙（与之并列的组件之间的间隔）	可设置数值，默认是0	非负整数，单位为像素
anchor	锚选项，当可用空间大于所需求的尺寸时，决定组件被放置于容器的何处	N、E、S、W、NW、NE、SW、SE、CENTER（默认值为CENTER）	表示八个方向以及中心
注意：上表中取值都是常量，YES等价于”yes”，亦可以直接传入字符串值。另外当界面复杂度增加时，要实现某种布局效果，需要分层来实现。

pack类提供了下列函数（使用组件实例对象调用）：
函数名	描述
pack_slaves()	以列表方式返回本组件的所有子组件对象。
pack_configure(option=value)	给pack布局管理器设置属性，使用属性（option）= 取值（value）方式设置
propagate(boolean)	设置为True表示父组件的几何大小由子组件决定（默认值），反之则无关。
pack_info()	返回pack提供的选项所对应得值。
pack_forget()	Unpack组件，将组件隐藏并且忽略原有设置，对象依旧存在，可以用pack(option, …)，将其显示。
location(x, y)	x, y为以像素为单位的点，函数返回此点是否在单元格中，在哪个单元格中。返回单元格行列坐标，(-1, -1)表示不在其中
size()	返回组件所包含的单元格，揭示组件大小。
"""



"""
place布局,
直接定义元素的位置


place属性设置

属性名	属性简析	取值	取值说明
anchor	锚选项，同pack布局	默认值为 NW	同pack布局
x、y	组件左上角的x、y坐标	整数，默认值0	绝对位置坐标，单位像素
relx、rely	组件相对于父容器的x、y坐标	0~1之间浮点数	相对位置，0.0表示左边缘（或上边缘），1.0表示右边缘（或下边缘）
width、height	组件的宽度、高度	非负整数	单位像素
relwidth、relheight	组件相对于父容器的宽度、高度	0~1之间浮点数	与relx（rely）取值相似
bordermode	如果设置为INSIDE，组件内部的大小和位置是相对的，不包括边框；如果是OUTSIDE，组件的外部大小是相对的，包括边框	INSIDE、OUTSIDE(默认值INSIDE)	可以使用常量INSIDE、OUTSIDE，也可以使用字符串形式”inside”、”outside”
place类提供了下列函数（使用组件实例对象调用）：
函数名	描述
place_slaves()	以列表方式返回本组件的所有子组件对象。
place_configure(option=value)	给pack布局管理器设置属性，使用属性（option）= 取值（value）方式设置
propagate(boolean)	设置为True表示父组件的几何大小由子组件决定（默认值），反之则无关。
place_info()	返回pack提供的选项所对应得值。
grid_forget()	Unpack组件，将组件隐藏并且忽略原有设置，对象依旧存在，可以用pack(option, …)，将其显示。
location(x, y)	x, y为以像素为单位的点，函数返回此点是否在单元格中，在哪个单元格中。返回单元格行列坐标，(-1, -1)表示不在其中
size()	返回组件所包含的单元格，揭示组件大小。"""