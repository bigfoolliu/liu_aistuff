# 基于tkinter的小视频播放器

<!-- TOC -->

- [基于tkinter的小视频播放器](#%e5%9f%ba%e4%ba%8etkinter%e7%9a%84%e5%b0%8f%e8%a7%86%e9%a2%91%e6%92%ad%e6%94%be%e5%99%a8)
  - [1.介绍](#1%e4%bb%8b%e7%bb%8d)
  - [2.tkinter使用](#2tkinter%e4%bd%bf%e7%94%a8)
    - [2.1基础概念](#21%e5%9f%ba%e7%a1%80%e6%a6%82%e5%bf%b5)
    - [2.2GUI组件](#22gui%e7%bb%84%e4%bb%b6)
    - [2.3](#23)

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

### 2.3
