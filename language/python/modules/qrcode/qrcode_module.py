#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
qrcode模块使用

生成不同类型的二维码

参考:

- 二维码介绍: https://zhuanlan.zhihu.com/p/136748834
- qrcode库： https://github.com/sylnsfar/qrcode/blob/master/README-cn.md

二维码知识:

1.二维码就是将数据通过某种编码转化为黑白点阵,识别则是数据的还原
2.二维码的复杂度取决于：输入数据编码类型，版本，以及纠错级别
    - 版本有40个等级，版本越高，能存储的数据就越多，公式来表示：v * 4+17
    - 纠错级别又分为 L、M、Q、H, 纠错级别越高，则容错率越高; 级别越低，纠错能力越低，但是能存储更多的数据

"""


def main():
    pass


if __name__ == "__main__":
    main()
