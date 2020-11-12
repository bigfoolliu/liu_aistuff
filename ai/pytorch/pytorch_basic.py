#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import torch
import torch.nn as nn
import torch.nn.functional as F


def basic_demo():
    """
    基本概念
    :return:
    """
    # 构造一个矩阵
    x = torch.empty(5, 3)
    print(x)
    x1 = torch.rand(5, 3)
    print(x1)

    # 矩阵的加法的两种形式
    print(x + x1)
    print(x.add(x1))

    # 构造一个张量,直接使用数据
    x2 = torch.tensor([1.1, 2])
    print(x2)
    print(x2.size())  # 维度


def auto_differential_demo():
    """
    自动微分示例
    - Tensor 是包的核心类
    - requires_grad 为 True 来跟踪对其的所有操作，完成计算之后，使用 .backward() 方法来自动计算所有梯度
    - 停止 tensor 历史记录的跟踪，使用 .detach() 方法，将其计算历史记录分离，防止未来的计算被跟踪
    - grad_fn 保存张量被创建时候的函数引用,如果自己创建张量，则为 None
    :return: 
    """
    x = torch.ones(2, 2, requires_grad=True)
    print(f'x: {x}')
    y = x + 2
    print(f'y: {y}')
    print(f'y.grad_fn: {y.grad_fn}')

    z = y * y * 3
    out = z.mean()
    print(f'z: {z}\nout: {out}')

    # 向后传播
    out.backward()

    # 输出梯度, d(out)/d(x)
    print(f'x.grad: {x.grad}')

    # 改变张量的 requires_grad 标记,默认为 False
    print(f'x.requires_grad: {x.requires_grad}')
    x.requires_grad_(False)
    print(f'x.requires_grad: {x.requires_grad}')


class NeuralNet(nn.Module):
    """
    定义一个神经网络
    """

    def __init__(self):
        super(NeuralNet, self).__init__()
        # 1个输入图像通道, 6个输出通道, 5 * 5的卷积内核
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 一元线性 y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 最大池化为2*2
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


def nn_demo():
    """
    神经网络基本示例
    典型神经网络训练过程：
    1. 定义一个包含可训练参数的神经网络
    2. 迭代整个输入
    3. 通过神经网络处理输入
    4. 计算损失(loss)
    5. 反向传播梯度到神经网络的参数
    6. 更新神经网络的参数
    :return:
    """
    net = NeuralNet()
    print('net:', net)

    # 查看模型可训练的参数
    params = list(net.parameters())
    print('len params: ', len(params))
    print('params[0].size(): ', params[0].size())

    # 32*32的输入，和 MNIST 数据集一样
    input1 = torch.randn(1, 1, 32, 32)
    print('input1:', input1)
    out = net(input1)
    print('out: ', out)

    # 将所有的参数梯度值缓存器置零，用随机的梯度来反向传播
    net.zero_grad()
    out.backward(torch.randn(1, 10))
    print('new net: ', net)

    # 计算损失
    output = net(input1)
    target = torch.randn(10)  # 假使期望值
    target = target.view(1, -1)
    criterion = nn.MSELoss()  # 损失函数
    loss = criterion(output, target)
    print('loss:', loss)

    # 查看损失的部分反向传播路径
    print('loss.grad_n: ', loss.grad_fn)
    print('loss.grad_fn_next_functions[0][0]: ', loss.grad_fn.next_functions[0][0])
    print('loss.grad_fn_next_functions[0][0].next_functions[0][0]: ',
          loss.grad_fn.next_functions[0][0].next_functions[0][0])

    # 反向传播,对比之前和之后的conv1的偏置项
    net.zero_grad()
    print('conv1.bias.grad before backward', net.conv1.bias.grad)
    loss.backward()
    print('conv1.bias.grad after backward', net.conv1.bias.grad)

    # 更新神经网络参数，此处使用随机梯度下降, weight = weight - learning_rate * gradient
    import torch.optim as optim
    optimizer = optim.SGD(net.parameters(), lr=0.01)  # lr, learning_rate
    optimizer.zero_grad()
    output = net(input1)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

    print('trained net: ', net)


if __name__ == "__main__":
    # basic_demo()
    # auto_differential_demo()
    nn_demo()

