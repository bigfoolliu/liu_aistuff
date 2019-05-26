#!/usr/bin/env python
#!coding:utf-8


"""
单元测试模块的简单使用
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
