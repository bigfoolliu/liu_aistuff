#!-*-coding:utf-8-*-
# !@Date: 2018/8/23 10:31
# !@Author: Liu Rui
# !@github: bigfoolliu


"""

pyplot画二维图


"""


"""
numpy产生数组

arange(), 指定起始与终止位置以及步长
linespace(), 指定起始与终止位置以及元素个数

"""
# import numpy as np
#
# array1 = np.arange(0, 100, 1)  # 从0到100(0, 1, ..., 99),步长为1的数组
# print(type(array1))
# print(array1)


# import numpy as np
# array2 = np.linspace(0, 100, 20, dtype=int)  # 在0至100之间产生20个整数
# print(type(array2))
# print(array2)


"""
1. 画正弦图像
"""
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 定义横坐标
# x = np.arange(-np.pi * 2, np.pi * 2, 0.02)
#
# # 计算得到纵坐标
# y = np.sin(x)
#
# # 画图
# plt.plot(x, y)
#
# # 显示图像
# plt.show()


"""
2. 坐标区间设置
"""
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# x = np.arange(-np.pi * 2, np.pi * 2, 0.02)
# y = np.sin(x)
#
# # 定义坐标轴,横坐标为-10至10, 纵坐标为-2至2
# plt.axis([-10, 10, -2, 2])
#
# plt.plot(x, y)
# plt.show()


"""
3. 设置网格
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-np.pi * 2, np.pi * 2, 0.02)
y = np.sin(x)

plt.axis([-10, 10, -2, 2])

plt.plot(x, y)

# 增加网格线
plt.grid(True)

plt.show()
