#coding:utf-8


def sanjiao():
    """三角形的九九乘法表"""
    for i in range(9):
        for j in range(i+1):
            print("{} * {} = {}".format(j+1, i+1, (j+1) * (i+1)), end="\t")
        print("\n")


sanjiao()
