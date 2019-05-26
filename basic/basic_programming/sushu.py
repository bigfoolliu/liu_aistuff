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


print(judge_sushu(2))
print(judge_sushu(3))
print(judge_sushu(100))
print(judge_sushu(999))

