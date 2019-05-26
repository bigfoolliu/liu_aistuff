#coding:utf-8


def jiecheng(n):
    """利用递归求阶乘"""
    ji = 0
    if n == 0:
        ji = 1
    else:
        ji = n * jiecheng(n-1)
    return ji


print(jiecheng(3))
print(jiecheng(4))

