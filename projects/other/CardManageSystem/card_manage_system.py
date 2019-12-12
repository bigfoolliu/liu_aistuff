#!-*-coding:utf-8-*-
#!@Date: 2018/7/8 14:34
#!@Author: Liu Rui
#!@github: bigfoolliu

"""
名片管理系统
v1.0
"""
card_list = []  # 名片列表，包含用户信息（列表），全局变量
target_card = {}  # 记录查询到的用户信息（字典），全局变量

def display_menu():
	"""
	菜单显示
	:return:
	"""
	print("*" * 50)
	print("欢迎使用【菜单管理系统】")
	print("")
	print("1.新建名片")
	print("2.显示全部")
	print("3.查询名片")
	print("0.退出系统")
	print("")
	print("*" * 50)


def new_card():
	"""
	新建名片
	:return:
	"""
	print("-" * 50)
	print("功能：新建名片")

	name = input("输入姓名:")
	phone = input("输入电话:")

	card_info = {"name": name, "phone": phone}
	card_list.append(card_info)
	print("添加%s的名片成功。" % name)


def show_all():
	"""
	显示全部
	:return:
	"""
	print("-" * 50)
	print("功能：显示全部")
	# 判断是否有名片信息
	if len(card_list) == 0:
		print("提示：没有任何名片记录！")
	show_table_head()
	for card_info in card_list:
		print("%s\t\t%s\t\t" % (card_info["name"], card_info["phone"]))
		print("-" * 30)


def search_card():
	"""
	搜索名片
	:return:
	"""
	target_name = input("请输入查询的姓名：")
	# 遍历全局列表，取出每个学生的姓名信息进行对比
	for card_info in card_list:
		if target_name == card_info["name"]:
			# 使用全局变量记录该字典
			global target_card
			target_card = card_info

			show_table_head()
			print("%s\t\t%s\t\t" % (card_info["name"], card_info["phone"]))
			print("-" * 30)
			# 对名片进行高级处理
			deal_card()
			break
	else:
		print("找不到%s" % target_name)


def deal_card():
	"""
	处理名片
	包含更新，删除操作
	:return:
	"""
	while True:
		cmd_num = input("输入操作：更新名片/1，删除名片/2，返回上一级/0")
		if cmd_num == "1":
			update_card()
		elif cmd_num == "2":
			delete_card()
		elif cmd_num == "0":
			break
		else:
			print("输入有误!")
			break


def update_card():
	"""
	更新名片：更改信息
	:return:
	"""
	target_card["name"] = input("输入新的用户名：")
	target_card["phone"] = input("输入新的电话：")
	print("%s名片更新成功..." % target_card["name"])


def delete_card():
	"""
	删除名片
	:return:
	"""
	card_list.remove(target_card)
	print("%s名片删除成功" % target_card["name"])


def show_table_head():
	"""
	显示表头
	:return:
	"""
	print("-" * 30)
	print("姓名\t\t电话\t\t")
	print("-" * 30)


while True:
	display_menu()

	action = input("请选择操作功能：")
	print("您选择的操作是：%s" % action)

	if action in ["1", "2", "3", "4"]:  # 使用in针对列表判断，避免使用or拼接复杂的逻辑条件，不适用int强制转化类型，可避免一旦用户输入的不是数字，产生错误
		if action == "1":
			new_card()
		elif action == "2":
			show_all()
		elif action == "3":
			search_card()
		elif action == "4":
			deal_card()
	elif action == "0":
		print("欢迎再次使用【名片管理系统】")
		break
	else:
		print("输入错误，重新输入")
		break
