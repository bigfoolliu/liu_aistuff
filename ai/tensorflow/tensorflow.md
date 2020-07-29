# tensorflow介绍使用

<!-- TOC -->

- [tensorflow介绍使用](#tensorflow介绍使用)
  - [计算模型－计算图](#计算模型计算图)
  - [运算模型－会话](#运算模型会话)

<!-- /TOC -->

## 1.计算模型－计算图

## 2.运算模型－会话

Kye words:

- learning rate(学习率)
- activation(激活函数)
- relularization(正则化)
- batch_size: 每批数据量的大小
- iteration: 1个iteration即迭代一次，即用batch_size个样本训练一次
- epoch: 1个epoch指用训练集中的全部样本训练一次

使用神经网络解决分类问题的主要步骤:

1. 提取问题中的实体的特征向量作为神经网络的输入
2. 定义神经网络的结构，并定义如何从神经网络的输入得到输出
3. 通过训练数据来调整神经网络中的参数
4. 使用训练好的神经网络来进行预测工作

Tensorflow:

- 使用图(graph)来表示计算任务
- 在被称之为会话(session)和上下文(context)中执行图
- 使用tensor来表示数据
- 通过变量(Variable)维护状态
- 使用feed和feth可以为任意的操作(arbitrary operation)赋值或者从中获取数据
