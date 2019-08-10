#coding:utf-8

def judge_sushu(n):
    """判断输入的数是否为素数"""
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True


def input_num(n):
    """输入查找的范围"""
    if n < 2:
        return "输入有误"
    else:
        res = []
        for i in range(2, n):
            if judge_sushu(i):
                res.append(i)
        return res


print(input_num(100))

