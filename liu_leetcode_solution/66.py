#!coding:utf-8


def plusOne(digits):
    """
    leet code第66题
    """
    # 将数字列表转换为数字
    num = 0
    for i in range(len(digits)):
        num += digits[i] * 10 ** (len(digits) -1 - i)
    
    num = num + 1
    # 将数字转换为列表
    ret = []
    for i in str(num):
        ret.append(int(i))

    return ret


# 执行一些测试
def generate_nums(n):
    """
    产生指定长度的整数列表
    """
    ret = []
    for i in range(n):
        import random
        if i == 0:
            ret.append(random.randint(1, 9))
        else:
            ret.append(random.randint(0, 9))
    return ret


for i in range(10):
    digits = generate_nums(i + 1)
    print("[INFO] digits:", digits)
    ret = plusOne(digits)
    print("[RESULT] ret:", ret)

    print("\n")

