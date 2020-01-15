#!/usr/bin/env python
#!coding:utf-8


"""
tf使用图来表示计算任务，
图中的节点被称为op(operation),
一个op获得0个或者多个Tensor,执行计算产生0个或多个Tensor,
每个Tensor是一个类型化的多维数组

计算图：
一个图描述了计算的过程，
图必须在会话中被启动，会话将图的op分发到诸如CPU或者GPU上,同时提供执行op的方法，执行后将产生的Tensor返回，python中返回的是numpy的ndarray对象

构建图：
第一步是创建源op，如常量
op构造器的返回值又可以作为其他op传递器的输入
"""
import tensorflow as tf


# 构造一个常量op,产生一个1*2矩阵，构造器的返回值代表该常量的op的返回值
mat1 = tf.constant([[3., 3.]])

# 创建另一个常量op，产生一个2*1矩阵
mat2 = tf.constant([[2.], [2.]])

# 创建一个矩阵乘法op
product = tf.matmul(mat1, mat2)

# 启动默认图
sess = tf.Session()
ret = sess.run(product)
print("[INFO]ret:{}".format(ret))
# 任务完成，关闭会话
sess.close()


"""
当机器上有超过一个可用的GPU

with tf.Session() as sess:
    with tf.device("/gpu:1"):
        mat1 = ...
        mat2 = ...
        product = ...
"""

