#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
执行外部的命令并以python字符串的形式获取结果
"""
import subprocess

# 最简单的方式
out_bytes = subprocess.check_output(["ls", "-a"], timeout=1)
print("out_bytes:\n", out_bytes)
out_text = out_bytes.decode("utf-8")
print("out_text:\n", out_text)


# 执行的命令以非零码返回，捕获异常
# try:
#     out_bytes = subprocess.check_output(["cmd", "arg1"], stderr=subprocess.STDOUT)
# except subprocess.CalledProcessError as e:
#     out_bytes = e.output
#     code = e.returncode
#     print(out_bytes, code)


# 执行较复杂的命令，要使用底层的shell命令
# 需要注意的是在 shell 中执行命令会存在一定的安全风险，特别是当参数来自于用
# 户输入时。这时候可以使用 shlex.quote() 函数来将参数正确的用双引用引起来。
# out_bytes = subprocess.check_output('grep python | wc > out', shell=True)


# 涉及到对子进程更复杂的操作，比如输入参数的时候，用popen
text = b'''
hello world
this is a test
goodbye
'''
# Launch a command with pipes
p = subprocess.Popen(['wc'], stdout = subprocess.PIPE, stdin = subprocess.PIPE)
# Send the data and get the output
stdout, stderr = p.communicate(text)
# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
print(out, "\n", err)