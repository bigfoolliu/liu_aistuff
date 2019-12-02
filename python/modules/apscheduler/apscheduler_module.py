#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
apscheduler模块
创建定时任务，如定时清理文件，定时计算报表等

定时器种类：

- BlockingScheduler：当调度器是进程中唯一运行的程序时候使用
- BackgroundScheduler: 不适用任何框架时候使用，并希望调度器在应用程序的后台运行
- AsynclOScheduler：使用的程序中必须有asyncio模块
- GeventScheduler: 使用的程序中必须有gevent模块
- TornadoScheduler：应用程序使用的是tornado模块
- TwistedScheduler: 应用程序使用的是twisted模块
- QTScheduler：在QT框架中使用

触发器种类：

- date：一次性任务，即只执行一次任务
- interval：循环任务，即按照时间间隔执行任务
- cron：定时任务，即在每个时间段执行任务

https://blog.csdn.net/somezz/article/details/83104368
"""


from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler


def timed_task():
    """定时输出当前时间"""
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def timed_task2(name):
    """带有参数的定时任务"""
    print("hello, {}, its {} now".format(name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


def blocking_interval_demo():
    """循环任务，且调度器是程序中唯一的程序"""
    scheduler = BlockingScheduler()
    scheduler.add_job(timed_task, trigger="interval", seconds=3)
    scheduler.start()


def blocking_date_demo():
    """一次性任务，在指定的的时间运行"""
    scheduler = BlockingScheduler()
    scheduler.add_job(timed_task2, args=("tony",), trigger="date",
                        next_run_time=datetime.now()+timedelta(seconds=3))  # 当前时间5秒后执行
    scheduler.start()


def blocking_cron_demo():
    """定时任务，在每个时间段执行"""
    scheduler = BlockingScheduler()
    scheduler.add_job(timed_task, trigger="cron", month="1,3,12", day="*", hour="17,18", minute="*")
    scheduler.start()
    

if __name__ == "__main__":
    try:
        # blocking_interval_demo()
        # blocking_date_demo()
        blocking_cron_demo()
    except (KeyboardInterrupt, SystemExit):
        pass
