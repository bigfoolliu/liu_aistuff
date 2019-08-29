#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
threading lock 多线程中的线程锁使用
"""
import threading
import time

lock = threading.Lock()

l = []


def test1(n):
    """使用线程锁的情况"""
    lock.acquire()
    l.append(n)
    time.sleep(0.001)
    print(l)
    lock.release()

def test(n):
    """不使用线程锁的情况"""
    l.append(n)
    time.sleep(0.001)
    print(l)


def main():
    for i in range(0, 30):
        """多个线程操作同一个资源，容易导致混乱"""
        th = threading.Thread(target=test, args=(i, ))
        # th = threading.Thread(target=test1, args=(i, ))
        th.start()


if __name__ == '__main__':
    main()
