#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
subprocess模块的使用

执行系统命令


subprocess模块:

1、subprocess.run()
2、subprocess.call()
3、subprocess.check_call()
4、subprocess.getstatusoutput()
5、subprocess.getoutput()
6、subprocess.check_output()


subprocess.Popen():

- 上述subprocess方法都是Popen的封装
- 创建Popen对象，对一个系统命令有更好的控制
- 如果只是简单的命令执行可以直接执行上面的subprocess的方法，如果有较为复杂的操作则使用Popen对象来操作

1、stdout
2、stderr
4、poll()
5、wait()
6、terminate()
7、pid
"""


import subprocess


def run_demo():
    """
    run直接执行命令
    """
    # 用python解析命令则需要传入命令的每个参数的列表
    subprocess.run(["df", "-h"])

    # 用shell解析则直接传入字符串
    subprocess.run("df -h", shell=True)


def call_demo():
    """
    call执行命令并返回命令的结果和执行状态（0或非0）
    0表示正常
    """
    ret = subprocess.call("ls -al", shell=True)
    print("ret:", ret)


def check_call_demo():
    """
    执行命令，返回结果和状态，正常为0，执行错误则抛出异常
    """
    ret = subprocess.check_call(["lm", "l"])
    print(ret)


def getstatusoutput_demo():
    """
    接收字符串形式的命令，返回一个元组形式的列表
    第一个元素是命令执行状态，第二个是执行结果
    """
    ret1 = subprocess.getstatusoutput("pwd")
    print("ret1:", ret1)

    ret2 = subprocess.getstatusoutput("pdd")
    print("ret2:", ret2)


def getoutput_demo():
    """
    接收字符串形式的命令，返回执行结果
    是对getstatusoutput命令返回结果的简化
    """
    ret1 = subprocess.getoutput("pwd")
    print("ret1:", ret1)
    ret2 = subprocess.getoutput("pdd")
    print("ret2:", ret2)


def check_output_demo():
    """
    执行命令，返回执行的结果（可能为字节形式），而不是打印
    """
    ret = subprocess.check_output("pwd")
    print("ret:", ret)


def popen_stdout_demo():
    """
    标准输出示例
    """
    ret = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE)
    print("ret:", ret)
    print(ret.stdout.read())
    ret.stdout.read()


if __name__ == "__main__":
    # run_demo()
    # call_demo()
    # check_call_demo()
    # getstatusoutput_demo()
    # getoutput_demo()
    # check_output_demo()

    popen_stdout_demo()
