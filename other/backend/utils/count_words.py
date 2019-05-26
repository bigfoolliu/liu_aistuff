#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
统计词频率
"""
words = """
Here is return'd my Lord of Westmoreland.
Re-enter WESTMORELAND
WESTMORELAND
The prince is here at hand: pleaseth your lordship
To meet his grace just distance 'tween our armies.
MOWBRAY
Your grace of York, in God's name then, set forward.
ARCHBISHOP OF YORK
Before, and greet his grace: my lord, we come.
"""

word_list = words.split()  # 单词列表
word_freq = [word_list.count(w) for w in word_list]  #　单词频率列表

pair_dict = dict(zip(word_list, word_freq))  # 对应字典
print(pair_dict)

