# 基于tkinter的小视频播放器

<!-- TOC -->

- [基于tkinter的小视频播放器](#%e5%9f%ba%e4%ba%8etkinter%e7%9a%84%e5%b0%8f%e8%a7%86%e9%a2%91%e6%92%ad%e6%94%be%e5%99%a8)
  - [1.介绍](#1%e4%bb%8b%e7%bb%8d)
  - [2.tkinter使用](#2tkinter%e4%bd%bf%e7%94%a8)
    - [2.1基础概念](#21%e5%9f%ba%e7%a1%80%e6%a6%82%e5%bf%b5)
    - [2.2GUI组件](#22gui%e7%bb%84%e4%bb%b6)
    - [2.3GUI组件常见选项](#23gui%e7%bb%84%e4%bb%b6%e5%b8%b8%e8%a7%81%e9%80%89%e9%a1%b9)
    - [2.3pack选项](#23pack%e9%80%89%e9%a1%b9)

<!-- /TOC -->

## 1.介绍

基于python tkinter的最基本的视频播放器。

## 2.tkinter使用

[学习资源](http://c.biancheng.net/view/2451.html)

### 2.1基础概念

Misc：它是所有组件的根父类。
Wm：它主要提供了一些与窗口管理器通信的功能函数。

Tk: 代表应用程序的主窗口。因此所有 Tkinter GUI 编程通常都需要直接或间接使用该窗口类。
BaseWidget: 所有组件的基类，它还派生了一个子类 Widget,Widget 代表一个通用的GUI组件，Tkinter所有的GUI组件都是Widget的子类。

### 2.2GUI组件

| Tkinter类 | 名称 | 简介 |
| ------ | ------ | ------ |
| Toplevel | 顶层 | 容器类，可用于为其他组件提供单独的容器；Toplevel 有点类似于窗口 |
| Button | 按钮 | 代表按钮组件 |
| Canvas | 画布 | 提供绘图功能，包括绘制直线、矩形、椭圆、多边形、位图等 |
| Checkbutton | 复选框 | 可供用户勾选的复选框 |
| Entry | 单行输入框 | 用户可输入内容 |
| Frame | 容器 | 用于装载其它 GUI 组件 |
| Label | 标签 | 用于显示不可编辑的文本或图标 |
| LabelFrame | 容器 | 也是容器组件，类似于Frame，但它支持添加标题 |
| Listbox | 列表框 | 列出多个选项，供用户选择 |
| Menu | 菜单 | 菜单组件 |
| Menubutton | 菜单按钮 | 用来包含菜单的按钮（包括下拉式、层叠式等） |
|OptionMenu | 菜单按钮 | Menubutton 的子类，也代表菜单按钮，可通过按钮打开一个菜单 |
| Message | 消息框 | 类似于标签，但可以显示多行文本；后来当Label也能显示多行文本之后，该组件基本处于废弃状态 |
| PanedWindow | 分区窗口 | 该容器会被划分成多个区域，每添加一个组件占一个区域，用户可通过拖动分隔线来改变各区域的大小 |
| Radiobutton | 单选钮可供用户点边的单选钮 |
| Scale | 滑动条 | 拖动滑块可设定起始值和结束值，可显示当前位置的精确值 |
| Spinbox | 微调选择器 | 用户可通过该组件的向上、向下箭头选择不同的值 |
| Scrollbar | 滚动条 | 用于为组件（文本域、画布、列表框、文本框）提供滚动功能 |
| Text | 多行文本框 | 显示多行文本 |

### 2.3GUI组件常见选项

| 选项名（别名） | 含义 | 单位 | 典型值 |
| ------ | ------ | ------ | ------ |
| activebackground | 指定组件处于激活状态时的背景色 | color | 'gray25'或'#ff4400' |
| activeforeground | 指定组件处于激活状态时的前景色 | color | 'gray25'或'#ff4400' |
| anchor | 指定组件内的信息（比如文本或图片）在组件中如何显示。必须为下面的值之一：N、NE、E、SE、S、SW、W、NW或CENTER。比如NW（NorthWest）指定将信息显示在组件的左上角 |  | CENTER |
| background(bg) | 指定组件正常显示时的背景色 | color | 'gray25'或'#ff4400' |
| bitmap | 指定在组件上显示该选项指定的位图，该选项值可以是Tk_GetBitmap接收的任何形式的位图。位图的显示方式受anchor、justify选项的影响。如果同时指定了bitmap和text，那么bitmap 覆盖文本；如果同时指定了bitmap 和image，那么image 覆盖bitmap |  |  |
| borderwidth | 指定组件正常显示时的3D边框的宽度，该值可以是Tk_GetPixels接收的任何格式 | pixel | 2 |
| cursor | 指定光标在组件上的样式。该值可以是Tk_GetCursors 接受的任何格式 | cursor | gumby |
| disabledforeground | 指定组件处于禁用状态时的前景色 | color | 'gray25'或'#ff4400' |
| font | 指定组件上显示的文本字体 | font | 'Helvetica'或('Verdana', 8) |
| foreground(fg) | 指定组件正常显示时的前景色 | color | 'gray'或'#ff4400' |
| highlightbackground | 指定组件在高亮状态下的背景色 | color | 'gray'或'#ff4400' |
| highlightcolor | 指定组件在高亮状态下的前景色 | color | 'gray'或'#ff4400' |
| highlightthickness | 指定组件在高亮状态下的周围方形区域的宽度，该值可以是Tk_GetPixels接收的任何格式 | pixel | 2 |
| height | 指定组件的高度，以font选项指定的字体的字符高度为单位，至少为1 | integer | 14 |
| image | 指定组件中显示的图像，如果设置了image 选项，它将会覆盖text、bitmap选项 | image |  |
| justify | 指定组件内部内容的对齐方式，该选项支持LEFT（左对齐）、CENTER（居中对齐）或RIGHT（右对齐）这三个值 | constant | RIGHT |
| padx | 指定组件内部在水平方向上两边的空白，该值可以是Tk_GctPixels接收的任何格式 | pixel | 12 |
| pady | 指定组件内部在垂直方向上两地的空白，该值可以是Tk_GctPixels接收的任何格式 | pixel | 12 |
| relief | 指定组件的3D 效果，该选项支持的值包括RAISED、SUNKEN、FLAT、RIDGE、SOLID、GROOVE。该值指出组件内部相对于外部的外观样式，比如RAISED表示组件内部相对于外部凸起 | constant | GROOVE RAISED |
| selectbackground | 指定组件在选中状态下的背景色 | color | 'gray'或'#ff4400' |
| selectborderwidth | 指定组件在选中状态下的3D边框的宽度，该值可以是Tk_GetPixels接收的任何格式 | pixel | 2 |
| selectforeground | 指定组在选中状态下的前景色 | color | 'gray'或'#ff4400' |
| state | 指定组件的当前状态。该选项支持NORMAL（正常）、DISABLE（禁用）这两个值 | constant | NORMAL |
| takefocus | 指定组件在键盘遍历（Tab 或 Shift+Tab）时是否接收焦点，将该选项设为 1 表示接收焦点；设为 0 表示不接收焦点 | boolean | 1或YES |
| text | 指定组件上显示的文本，文本显示格式由组件本身、anchor 及 justify 选项决定 | str | '确定' |
| textvariable | 指定一个变量名，GUI 组件负责显示该变量值转换得到的字符串，文本显示格式由组件本身、anchor 及 justify 选项决定 | variable | bnText |
| underline | 指定为组件文本的第几个字符添加下画线，该选项就相当于为组件绑定了快捷键 | integer | 2 |
| width | 指定组件的宽度，以font 选项指定的字体的字符高度为单位，至少为 1 | integer | 14 |
| wraplength | 对于能支持字符换行的组件，该选项指定每行显示的最大字符数，超过该数量的字符将会转到下行显示 | integer | 20 |
| xscrollcommand | 通常用于将组件的水平滚动改变（包括内容滚动或宽度发生改变）与水平滚动条的set方法关联，从而让组件的水平滚动改变传递到水平滚动条 | function | scroll.set |
| yscrollcommand | 通常用于将组件的垂直滚动改变（包括内容滚动或高度发生改变）与垂直滚动条的set 方法关联，从而让组件的垂直滚动改变传递到垂直滚动条 | function | scroll.set |

### 2.3pack选项

| 常用选项 | 功能 |
| ------ | ------ |
| anchor | 当可用空间大于组件所需求的大小时，该选项决定组件被放置在容器的何处。该选项支持 N（北，代表上）、E（东，代表右）、S（南，代表下）、W（西，代表左）、NW（西北，代表左上）、NE（东北，代表右上）、SW（西南，代表左下）、SE（东南，代表右下）、CENTER（中，默认值）这些值。 |
| expand | 该 bool 值指定当父容器增大时才是否拉伸组件。 |
| fill | 设置组件是否沿水平或垂直方向填充。该选项支持 NONE、X、Y、BOTH 四个值，其中 NONE 表示不填充，BOTH 表示沿着两个方向填充。 |
| ipadx | 指定组件在 x 方向（水平）上的内部留白（padding）。 |
| ipady | 指定组件在 y 方向（水平）上的内部留白（padding）。 |
| padx | 指定组件在 x 方向（水平）上与其他组件的间距。 |
| pady | 指定组件在 y 方向（水平）上与其他组件的间距。 |
| side | 设置组件的添加位置，可以设置为 TOP、BOTTOM、LEFT 或 RIGHT 这四个值的其中之一。 |
