#!-*-coding:utf-8-*-
# !@Date: 2018/8/19 10:16
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
JavaScript Object Notation（JSON，http://www.json.org）是源于JavaScript 的当今很流行的
数据交换格式，它是JavaScript 语言的一个子集，也是Python 合法可支持的语法.
"""

"""
dumps()函数将数据编码为JSON字符串
loads()函数将JSON字符串解码为数据
"""
import json

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

menu_json = json.dumps(menu)
print(type(menu_json), menu_json)

menu2 = json.loads(menu_json)
print(type(menu2), menu2)
