# liu_aistuff
stuff about ai

2019/3/6
- install tf
- add some demos

2019/3/8
- finish fashion_mnist.py
- add forward_propagation.py
- add binary_classification.py


Basic Introduction

**计算模型－计算图**

```python
# Define constant and calcilate

import tensoflow as tf
a = tf.constant([1.0, 2.0], name="a")
ret = tf.add(a, a, name="ret")  # 或ret = a + a


# Define variable
weights = tf.Variable(tf.random_normal([2, 3], stddev=2))  # 声明一个2*3的矩阵变量,矩阵中的元素是均值为0，标准差为2的随机数
```

**运算模型－会话**

```python
sess = tf.Session()
sess.run(result)
sess.close()
```

Kye words:

- learning rate(学习率)
- activation(激活函数)
- relularization(正则化)


使用神经网络解决分类问题的主要步骤:

1. 提取问题中的实体的特征向量作为神经网络的输入
2. 定义神经网络的结构，并定义如何从神经网络的输入得到输出
3. 通过训练数据来调整神经网络中的参数
4. 使用训练好的神经网络来进行预测工作


