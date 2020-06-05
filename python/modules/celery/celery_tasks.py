#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用celery:

1. 创建一个Celery实例，我们一般叫做celery应用，或者更简单直接叫做一个app。
2. app应用是我们使用celery所有功能的入口，比如创建任务，管理任务等
3. 在使用celery的时候，app必须能够被其他的模块导入

4. 现在我们在创建一个worker，等待处理队列中的任务.打开终端，cd到tasks.py同级目录中，执行命令:
    celery -A celery_tasks worker --loglevel=info

5. 任务加入到broker队列中，以便刚才我们创建的celery workder服务器能够从队列中取出任务并执行，可使用delay()，进入python终端, 执行如下代码:
    from tasks import my_task
    my_task.delay()

    返回结果为：AsyncResult对象，可以通过AsyncResult.result查看结果或者从broker中查看结果：
    "{
        \"status\": \"SUCCESS\",
        \"result\": \"5\",
        \"traceback\": null,
        \"children\": [],
        \"task_id\": \"56e8d5c9-15ca-4ff3-8be5-452484877b6d\",
        \"date_done\": \"2019-12-11T08:52:05.156266\"
    }"
"""


import os
from celery import Celery


# 指定celery实例的名称和broker,backend用来指定存储结果
celery_app = Celery("celery_demo", broker="redis://127.0.0.1:6379/14", backend="redis://127.0.0.1:6379/13")


@celery_app.task
def celery_task_add(x, y):
    """
    定义一个耗时的celery任务
    任务函数，通过加上装饰器app.task, 将其注册到broker的队列中
    :param x: int
    :param y: int
    :return: str
    """
    print("celery task running...")
    return str(x+y)


if __name__ == "__main__":
    pass
