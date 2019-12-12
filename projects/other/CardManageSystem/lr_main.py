#!-*-coding:utf-8-*-
#!@Date: 2018/7/17 18:13
#!@Author: Liu Rui
#!@github: bigfoolliu


"""
重写名片管理系统V4.0
1.引用模块lr_tool.py(包含全部功能)
2.lr_main里只有主循环
3.名片输出时要输出表头
4.查询之后有高级功能(修改,删除)
5.
"""
import lr_tool

while True:
	lr_tool.show_menu()
	cmd_num = input("输入命令:")
	if cmd_num == "1":
		lr_tool.add_card()
	elif cmd_num == "2":
		lr_tool.show_all()
	elif cmd_num == "3":
		lr_tool.search_card()
	elif cmd_num == "4":
		lr_tool.save_cards()
	elif cmd_num == "5":
		lr_tool.import_cards()
	elif cmd_num == "0":
		break
	else:
		print("输入错误!")
