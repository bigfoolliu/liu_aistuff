#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
单元测试模块的简单使用

重要概念：

1. TestCase:
    一个TestCase的实例就是一个测试用例, 即一个完整的测试流程，包括测试前准备环境的搭建(setUp)，执行测试代码 (run)，
    以及测试后环境的还原(tearDown)。元测试(unit test)的本质也就在这里，
    一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。
2. Test suite：
    多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。


使用unittest编写python的单元测试代码，包括如下几个步骤：

    1. 编写一个python类，继承 unittest模块中的TestCase类，这就是一个测试类
    2. 在上面编写的测试类中定义测试方法（这个就是指的测试用例），每个方法的方法名要求以 test 打头，没有额外的参数。
        在该测试方法中 调用被测试代码，校验测试结果，TestCase类中提供了很多标准的校验方法，如 最常见的assertEqual。
    3. 执行 unittest.main() ，该函数会负责运行测试，它会实例化所有TestCase的子类，并运行其中所有以test打头的方法。

"""
import unittest


class TestDemo(unittest.TestCase):
    """全都需要继承于TestCase"""

    def setUp(self):
        """每个测试用例执行之前的操作"""
        print("[INFO]Before the single test.")

    def tearDown(self):
        """每个测试用例执行之后的操作"""
        print("[INFO]After the single test.")

    @classmethod
    def setUpClass(self):
        """所有测试用例执行之前的操作."""
        print("[INFO]Before all tests.")

    @classmethod
    def tearDowmClass(self):
        """所有测试用例执行之后的操作"""
        print("[INFO]After all tests.")

    def testA(self):
        """具体的测试用例，命名需要以 test 开头"""
        print("[INFO]Begin test A")
        self.assertEqual(1, 1)
        print("[INFO]Finish test A")

    def testB(self):
        print("[INFO]Begin test B")
        self.assertEqual(1, 0)
        print("[INFO]Finish test B")


# 运行所有的测试用例
unittest.main()
