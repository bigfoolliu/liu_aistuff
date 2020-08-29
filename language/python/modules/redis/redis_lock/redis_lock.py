#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用redis实现分布式锁

实现思想：
1. 获取锁的时候，使用setnx加锁，并用expire加一个超时时间，超过时间则自动释放锁，
    锁的value值为随机生成的uuid
2. 获取锁的时候设置一个获取的超时时间，超过时间则放弃获取锁
3. 释放锁的时候，通过uuid判断是不是该锁，是的话则delete进行锁释放

https://www.cnblogs.com/angelyan/p/11523846.html
"""

import time
import uuid
from threading import Thread

import redis


class DistributedLock(object):
    """简单的分布式锁"""

    def __init__(self):
        self.redis_client = redis.Redis(host="localhost", port=6379, db=0)
    
    def acquire_lock(self, lock_name, acquire_time=10, time_out=10):
        """
        获取一个锁
        :param lock_time: 锁的名称
        :param acquire_time: 客户端等待获取锁的时间
        :param time_out: 锁的超时时间
        :return: identifier,标识符
        """
        identifier = str(uuid.uuid4())
        end_time = time.time() + acquire_time
        lock = "string:lock:" + lock_name
        while time.time() < end_time:
            if self.redis_client.setnx(lock, identifier):
                # 给锁设置超时时间，防止进程崩溃导致其他进程无法获取锁
                self.redis_client.expire(lock, time_out)
                return identifier
            elif not self.redis_client.ttl(lock):
                self.redis_client.expire(lock, time_out)
            time.sleep(0.001)
        return False
    
    def release_lock(self, lock_name, identifier):
        """
        释放锁
        :param lock_name: 锁的名称 
        :param identifier: 标识符
        :return: 
        """
        lock = "string:lock:" + lock_name
        pip = self.redis_client.pipeline(True)
        while True:
            try:
                pip.watch(lock)
                lock_value = self.redis_client.get(lock)
                if not lock_value:
                    return True
                
                if lock_value.decode() == identifier:
                    pip.multi()
                    pip.delete(lock)
                    pip.execute()
                    return True
                pip.unwatch()
                break
            except Exception as e:
                print("redis execute error: {}".format(e))
        return False


distributed_lock = DistributedLock()


count = 10


def sec_kill(i):
    """
    测试
    使用50个线程模拟秒杀10张票，使用运算符来实现商品减少
    从结果的有序性就可以看出是否为加锁状态
    """
    identifier = distributed_lock.acquire_lock("resource")
    print("threading {} get the lock".format(i))
    time.sleep(1)
    global count
    if count < 1:
        print("threading {} did not get the ticket".format(i))
        return
    count -= 1
    print("threading {} get the ticket, {} tickets left".format(i, count))
    distributed_lock.release_lock("resource", identifier)


def test_demo():
    for i in range(50):
        t = Thread(target=sec_kill, args=(i,))
        t.start()


if __name__ == '__main__':
    test_demo()
