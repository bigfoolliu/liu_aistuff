#!-*-coding:utf-8-*-
# !@Date: 2018/8/19 8:42
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
逗号分隔符结构化文本文件(.csv)

将已存在的结构化的文本写入至本地并保存为csv格式文件
"""
# import csv
#
# # 自定义一个带有标题的csv格式的文件
# villains = [
# 	{"first": "doctor", "last": "no"},
# 	{"first": "rosa", "last": "klebb"},
# 	{"first": "mister", "last": "big"},
# 	{"first": "auric", "last": "goldfinge"},
# 	{"first": "ernst", "last": "blofeld"}
# ]
#
# """将已存在的结构化的文本写入至本地并保存为csv格式文件"""
# with open("villains", "wt") as fout:
# 	cout = csv.DictWriter(fout, ["first", "last"])  # 创建一个DictWriter对象
# 	cout.writeheader()  # 将头("first", "last")写入
# 	cout.writerows(villains)  # 将其他行写入
#
# """读取已经存在的csv格式文件"""
# with open("villains", "rt") as fin:
# 	cin = csv.DictReader(fin)
# 	villains = [row for row in cin]
#
# for item in villains:
# 	print(item)
# # print(villains)


"""无标题的csv"""
# import csv
#
# villains = [
# 	["doctor", "no"],
# 	["rosa", "klebb"],
# 	["mister", "big"],
# 	["auric", "goldfinger"],
# 	["sophia", "blod"]
# ]
#
# """写入"""
# with open("villains2", "wt") as fout:
# 	csvout = csv.writer(fout)
# 	csvout.writerows(villains)
#
# """读取"""
# with open("villains2", "rt") as fin:
# 	cin = csv.reader(fin)
# 	villains = [row for row in cin]
#
# for item in villains:
# 	print(item)


"""编码或解析JSON格式数据时遇到的异常"""
# import datetime
# import json
#
# current_time = datetime.datetime.utcnow()  # 返回一个格式化的utctime
# print(type(current_time), current_time)
#
# try:
# 	time_json = json.dumps(current_time)
# 	print(time_json)
# except:
# 	print("时间对象不能直接编码为json对象")
# 	# raise TypeError()
#
# """将时间对象转换为字符串的形式然后再编码"""
# try:
# 	time_json = json.dumps(str(current_time))
# 	print(time_json)
# except:
# 	print("时间对象不能直接编码为json对象")


"""
存储数据结构到一个文件中也称为序列化（serializing）。像JSON 这样的格式需要定制
的序列化数据的转换器。

Python 提供了pickle 模块以特殊的二进制格式保存和恢复数据对象。

作用:
1. 比如将任意对象(自定义类对象, 整型, 一般类对象)等序列化为二进制文件便于数据传输
"""
import datetime
import pickle

current_time = datetime.datetime.utcnow()  # 返回一个格式化的utctime
print(type(current_time), current_time)

pickled_time = pickle.dumps(current_time)  # 将时间对象pickle序列化为特殊为二进制格式文件
print(type(pickled_time), pickled_time)

current_time2 = pickle.loads(pickled_time)  # 将序列化的二进制文件恢复
print(type(current_time2), current_time2)


