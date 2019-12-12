#!-*-coding:utf-8-*-
#!@Date: 2018/7/17 18:14
#!@Author: Liu Rui
#!@github: bigfoolliu


import os

card_list = []  # 存储所有的名片


def show_menu():
	"""
	菜单显示
	:return:
	"""
	print("*" * 30)
	print("名片管理系统V4.0")
	print("")
	print("1.创建名片")
	print("2.显示名片")
	print("3.查询名片")
	print("4.存储名片")
	print("5.导入名片")
	print("")
	print("0.退出系统")
	print("*" * 30)


def add_card():
	"""
	添加名片
	:return:
	"""
	print("*" * 30)
	print("添加名片")

	# 这种格式会自动创建一个新的字典
	card_info = {"name": input("输入姓名:"),
				 "phone": input("输入电话:"),
				 "qq": input("输入qq号:"),
				 "mail": input("输入邮箱:")}
	print("名片%s添加成功!" % card_info["name"])
	card_list.append(card_info)
	return


def show_all():
	"""
	显示所有名片
	:return:
	"""
	# 名片数为空时
	if len(card_list) == 0:
		print("当前名片列表为空,请先添加名片!")
		return
	# 名片数不为空,显示所有
	else:
		# 显示表头
		show_table_head()
		for card_item in card_list:
			print_card(card_item)


def show_table_head():
	"""
	显示表头
	:return:
	"""
	print("*" * 30)
	print("姓名\t\t电话\t\tqq\t\t邮箱")
	print("-" * 30)


def print_card(card_item):
	"""
	打印目标名片信息
	:return:
	"""
	print(card_item["name"], card_item["phone"], card_item["qq"], card_item["mail"], sep="\t\t")
	print("-" * 30)


def search_card():
	"""
	查询名片,后接高级功能
	:return:
	"""
	target_name = input("输入查询名片姓名:")
	# 遍历card_list
	for card_item in card_list:
		if card_item["name"] == target_name:  # 找到对应名片
			# 展示该名片
			show_table_head()
			print_card(card_item)

			# 高级功能
			change_card(card_item)
			break
	else:
		print("未找到名为%s的名片!" % target_name)


def change_card(card_item):
	"""
	对名片进行修改,删除操作
	:return:
	"""
	print("输入对该名片需要进行的操作(1.修改/2.删除/0.返回上一级):")
	cmd_num = input("")
	if cmd_num == "1":
		update_card(card_item)  # 修改名片
		return
	elif cmd_num == "2":
		delete_card(card_item)  # 删除名片
		return
	elif cmd_num == "0":
		return
	else:
		print("命令输入错误!")


def update_card(card_item):
	"""
	修改更新名片
	:param card_item:
	:return:
	"""
	# card_item = {"name:"......}  # 这种定义是错误的,只会定义一个局部变量,并不是形参
	card_item["name"] = input("姓名:")
	card_item["phone"] = input("电话:")
	card_item["qq"] = input("qq:")
	card_item["mail"] = input("邮箱")
	print("%s名片修改成功!" % card_item["name"])
	return


def delete_card(card_item):
	"""
	删除名片
	:param card_item:
	:return:
	"""
	card_list.remove(card_item)
	print("名片删除成功!")
	return


def save_cards():
	"""
	存储所有的名片
	:return:
	"""
	f = open("cards.data", "w")
	f.write(str(card_list))  # 该写入只能将字符串类型数据写入
	f.close()
	print("名片存储成功!")
	return


def import_cards():
	"""
	导入所有的名片
	:return:
	"""
	# 判断文件是否存在
	if os.path.exists("cards.data"):
		f = open("cards.data", "r")
		global card_list
		card_list = eval(f.read())  # 评估函数,将文件对象中的字典,列表,表达式等还原
		f.close()
		print("文件导入成功.")
		return
	else:
		print("名片文件不存在!")
