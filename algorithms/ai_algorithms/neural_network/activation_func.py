#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
神经网络常用的激励函数(激活函数)：

如果不用激励函数那么每一层节点的输入都是上层输出的线性函数，无论层数，与没有隐藏层效果相当，
引入非线性函数作为激励函数，可以使输入逼近任意函数，神经网络的表达能力就更加强大

如何选择激活函数：
1. 深度学习往往需要大量时间来处理大量数据，因此总体上尽量选择具有zero-cntered特点的激活函数，可以加快模型的收敛速度；
2. 使用relu需要小心设置learning rate,否则易出现'dead'神经元；
3. 尽量不用sigmoid，可以试试tanh,预期效果不如relu和maxout
"""
import math
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(z):
    """
    常用非线性激活函数之一
    数学形式：f(z)=1/(1+e ** (-z))
    特点：能够将输入的连续实值变换为0和1之间的输出，如果是非常大的负数，则输出为0，如果是非常大的正数则输出为1
    缺点：深度神经网络中梯度反向传播时导致梯度爆炸(概率较小)和梯度消失(概率较大);输出(output)不是0均值(0-centered);解析式中含有幂运算，
    规模大的深度网络会较大增加训练时间
    :param z:
    :return:
    """
    ret = 1 / (1 + math.e ** (-z))
    return ret


def tanh(x):
    """
    数学形式：tanh(x)=(e ** x - e ** (-x)) / (e ** x + e ** (-x))
    """
    ret = (math.e ** x - math.e ** (-x)) / (math.e ** x + math.e ** (-x))
    return ret


def relu(x):
    """
    数学形式：relu=max(0, x)
    :param x: array
    """
    ret = []
    for i in x:
        ret.append(max(0, i))
    return np.array(ret)


def leaky_relu(x, a=0.01):
    """
    数学形式：f(x)=max(ax, x), a通常为0.01
    :param x: array
    :param a: float
    """
    ret = []
    for i in x:
        ret.append(max(a * i, i))
    return np.array(ret)


def elu(x, a=0.01):
    """
    Exponential Liner Units
    数学形式：f(x)=x (x>0); a(e ** x - 1) (x<=0)
    """
    ret = []
    for i in x:
        if i > 0:
            ret.append(i)
        else:
            ret.append(a * (math.e ** i - 1))
    return np.array(ret)


def max_out():
    """
    是深度学习网络中的一层网络，就像池化层，卷积层一样
    """
    pass


# 测试用
# z = float(input("输入z:"))
# print("[INFO]sigmoid ret:{}".format(sigmoid(z)))


fig = plt.figure()
ax = plt.Axes(fig, [-10, 10, 1, 1])
z = np.linspace(-10, 10, num=500)

plt.subplot(231)
# sigmoid
sigmoid_ret = sigmoid(z)
plt.plot(z, sigmoid_ret, color="r", label="sigmoid")
# tanh
tanh_ret = tanh(z)
plt.plot(z, tanh_ret, color="g", label="tanh")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# relu
plt.subplot(232)
relu_ret = relu(z)
plt.plot(z, relu_ret, color="b", label="relu")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# leaky_relu
plt.subplot(233)
leaky_relu_ret = leaky_relu(z, 0.02)
plt.plot(z, leaky_relu_ret, color="r", label="leaky_relu")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# elu
plt.subplot(234, xlabel="x", ylabel="y")
elu_ret = elu(z, 0.02)
plt.plot(z, elu_ret, color="g", label="elu")
plt.legend()
plt.show()
