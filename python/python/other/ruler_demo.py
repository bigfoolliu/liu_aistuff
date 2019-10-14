#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
利用python的规则来实现在两份数据中查找不同
"""


# 去过普吉岛旅游的人员数据
users_visited_phuket = [
    {"first_name": "Sirena", "last_name": "Gross", "phone_number": "650-568-0388", "date_visited": "2018-03-14"},
    {"first_name": "James", "last_name": "Ashcraft", "phone_number": "412-334-4380", "date_visited": "2014-09-16"},
    {"first_name": "James2", "last_name": "Ashcraft3", "phone_number": "412-324-4380", "date_visited": "2014-09-16"},
    {"first_name": "James3", "last_name": "Ashcraft4", "phone_number": "412-234-4380", "date_visited": "2014-09-17"},
]

# 去过新西兰的人员数据
users_visited_nz = [
    {"first_name": "Justin", "last_name": "Malcom", "phone_number": "267-282-1964", "date_visited": "2011-03-13"},
    {"first_name": "Albert", "last_name": "Potter", "phone_number": "702-249-3714", "date_visited": "2013-09-11"},
    {"first_name": "Albert2", "last_name": "Potter2", "phone_number": "702-259-3714", "date_visited": "2013-09-12"},
    {"first_name": "James3", "last_name": "Ashcraft4", "phone_number": "412-234-4380", "date_visited": "2014-09-17"},
]


# 方式一：使用集合优化函数
# def find_customer():
#     """找到所有去过普吉岛但是没有去过新西兰的"""
#     # 遍历所有新西兰用户，为去过新西兰的建立索引,即创建集合
#     nz_record_idx = {
#         (rec["first_name"], rec["last_name"], rec["phone_number"])
#         for rec in users_visited_nz
#     }
#     # print(nz_record_idx)
# 
#     for rec in users_visited_phuket:
#         key = (rec["first_name"], rec["last_name"], rec["phone_number"])
#         if key not in nz_record_idx:
#             yield rec
# 
# 
# for i in find_customer():
#     print(i)


  # 利用集合的差集的方式求解，但是必须是可哈希的，即需要实现__hash__方法
class VisitRecord(object):
    """旅游记录对象"""
    def __init__(self, first_name, last_name, phone_number, date_visited):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_visited = date_visited
    
    def __hash__(self):
        """实现该方法让对象可以被hash"""
        return hash(
            (self.first_name, self.last_name, self.phone_number)
        )
    
    def __eq__(self, other):
        """当两条记录的名字和号码相同时，判定两者相等"""
        if isinstance(other, VisitRecord) and hash(other) == hash(self):
            return True
        return False


def find_customer2():
    return set(VisitRecord(**r) for r in users_visited_phuket) - \
        set(VisitRecord(**r) for r in users_visited_nz)


for r in find_customer2():
    print((r.first_name, r.last_name, r.phone_number))
