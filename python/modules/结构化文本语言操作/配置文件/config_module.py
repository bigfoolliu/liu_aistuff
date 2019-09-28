#!-*-coding:utf-8-*-
# !@Date: 2018/8/19 10:48
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
许多程序提供多种选项和设置。动态的设置可以通过传入程序参数，但是持久的参数需要
保存下来。因此，尽管你急着想快速定义自己的配置文件格式，但是最好不要这样做。你
定义的格式可能既粗糙也没有节省时间。你需要同时维护写入配置文件的程序以及读取配
置文件的程序（有时被称为解析程序）。其实，在程序中配置文件可以有许多好的选择，
包括之前几节中提到的格式。

我们使用标准configparser 模块处理Windows 风格的初始化.ini 文件。
"""
import configparser

cfg = configparser.ConfigParser()  # 定义一个配置解析类的对象
print(cfg.read("setting.cfg", encoding="utf-8"))  # 读取配置文件

print(cfg["french"]["greeting"])

print(cfg["files"])
print(cfg["files"]["bin"])

