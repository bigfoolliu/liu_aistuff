#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
multiprocessing Pool使用

- 可以提供指定数量的进程供用户调用
- 当有新的请求提交到Pool中时，如果池还没有满，就会创建一个新的进程来执行请求
- 如果池满，请求就会告知先等待，直到池中有进程结束，才会创建新的进程来执行这些请求

Pool对象常用方法：

- apply() — 该函数用于传递不定参数，主进程会被阻塞直到函数执行结束（不建议使用，并且3.x以后不在出现）
- apply_async() 与apply用法一致，但它是非阻塞的且支持结果返回后进行回调
- map(): 会使进程阻塞直到结果返回
- map_async() — 与map用法一致，但是它是非阻塞的
- close() — 关闭进程池（pool），使其不在接受新的任务
- terminal() — 结束工作进程，不在处理未处理的任务
- join() — 主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用
"""


import time
import multiprocessing
from multiprocessing import Pool
from language.python.modules.multiprocessing.multiprocessing_module import time_counter


def task(n):
    if not isinstance(n, int):
        raise ValueError
    time.sleep(n)
    ret = n * n
    print(f'{n}*{n}: {ret}')
    return ret


@time_counter
def basic_demo():
    cores = multiprocessing.cpu_count()  # 统计cpu核心数量
    pool = Pool(processes=cores)
    # ret = pool.map(func=task, iterable=range(3))  # map直接返回列表
    # print(ret)

    cnt = 0
    for _ in pool.imap_unordered(task, range(8)):  # imap_unordered返回的是迭代器
        print('done %d/%d\r' % (cnt, len(range(8))))
        cnt += 1


@time_counter
def join_demo():
    cores = multiprocessing.cpu_count()  # 统计cpu核心数量
    pool = Pool(processes=cores)

    for i in range(10):
        pool.apply_async(func=task, args=(i,))

    pool.close()  # 不在接受新的任务
    pool.join()  # 阻塞直至所有的任务完成


if __name__ == '__main__':
    # basic_demo()
    join_demo()
