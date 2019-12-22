#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python 位运算示例

位运算都是从低位到高位的运算顺序

1. & : 按位与运算，与位操作，相应位同为1则返回1
2. | : 按位或运算，只要有1就返回1

3. ^ : 按位异或运算，两位不同就返回1
    - 异或操作两个相同的数为0
    - 0和任何数字异或操作都是其本身

4. << : 左移位运算，所有位左移若干位，高位丢弃，低位补0，结果为原来的2^n方
5. >> : 右移位运算，所有位右移若干位，高位补0，低位丢弃
"""


def basic_demo():
    # 与位操作
    a = 0b1101
    b = 0b1011
    print(a, b)
    print(bin(a&b))  # 0b1001

    # 或位操作
    print(bin(a|b))

    # 异或位操作
    print(bin(a^b))

    # 左移位
    print(bin(a << 2), a << 2)

    # 右移位
    print(bin(a >> 2), a >> 2)


def xor_demo():
    """
    异或操作示例
    1. 可以交换两个整数而不必使用第三个参数
    2. 进行奇偶判断,奇数二进制的最低位一定是1，偶数二进制的最低位一定是0
    3. 格雷码转换
    4. 找出唯一成对的数
    """
    # 1. 可以交换两个整数而不必使用第三个参数
    a = 0b101
    b = 0b110

    a = a^b
    b = a^b
    a = a^b
    print(bin(a), bin(b))

    # 2. 进行奇偶判断
    if a ^ 0b1 == 0:
        print(a, "奇数")
    else:
        print(a, "偶数")

    # 4. 找出唯一成对的数,异或操作两个相同的数为0; 0和任何数字异或操作都是其本身 2^3^2=3
    l = [2, 3, 2]
    print(l[0] ^ l[1] ^ l[2])


if __name__ == "__main__":
    # basic_demo()
    xor_demo()
