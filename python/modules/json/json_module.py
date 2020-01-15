#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
json模块示例

JavaScript Object Notation（JSON，http://www.json.org）是源于JavaScript 的当今很流行的
数据交换格式，它是JavaScript 语言的一个子集，也是Python 合法可支持的语法.

dumps()函数将数据编码为JSON字符串
loads()函数将JSON字符串解码为数据
"""


import json


def basic_demo():
    menu = {
        "breakfast": {
            "time": "7-11",
            "pancake": "$12.2"
        },
        "lunch": {
            "time": "12-0",
            "items": {
                "humburger": "$3.2"
            }
        },
        "dinner": {
            "time": "18-0",
            "items": {
                "spaghetti": "$5.4"
            }
        }
    }

    # 将dict转换为json str
    menu_json = json.dumps(menu)
    print("menu_json:", type(menu_json), menu_json)

    # 将json str转换为dict
    menu2 = json.loads(menu_json)
    print("menu2:", type(menu2), menu2)


def loads_demo():
    """
    1. 读取JSON
    loads()方法将JSON文本字符串转为JSON对象
    """
    # 从文本文件中读取并转换为
    with open("./json_test.json", "r") as f:
    	json_str = f.read()
    	ret = json.loads(json_str)
    print(ret, type(ret))


def dumps_demo():
    """
    2. 输出JSON
    dumps()方法将JSON对象转为文本字符串
    """
    data = [
    	{
    		"name": "tony",
    		"gender": "male",
    		"birthday": "1990-1-1",
    		"爱好": "编程"
    	}
    ]
    
    with open("./json_test2.json", "a", encoding="utf-8") as f:  # 包含中文字符，因此规定输出编码
    	f.write(json.dumps(data))
    	f.write(json.dumps(data, indent=2))  # indent代表缩进字符个数
    	f.write(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    # basic_demo()
    # loads_demo()
    dumps_demo()
