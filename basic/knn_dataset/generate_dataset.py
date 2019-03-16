#!/usr/bin/env python
#!coding:utf-8


"""
生成用于knn的数据集并写入到csv文件中
- 两种数据(love movie and action movie)
- love movie:
    movie,actions,kisses,type
    (index),(0-20),(10-100),love
- action movie:
    movie,actions,kisses,type
    (index),(10-100),(0-20),action
"""
import random
import pandas as pd
import os
from datetime import datetime


def generate_data(movie_type):
    """生成数据集"""
    if movie_type == "love":
        actions = random.randint(0, 20)
        kisses = random.randint(10, 100)
        return [actions, kisses, "love"]
    elif movie_type == "action":
        actions = random.randint(10, 100)
        kisses = random.randint(0, 20)
        return [actions, kisses, "action"]
    return None


def generate_dataset(action_nums, love_nums):
    """生成指定条数的数据"""
    ret = []
    header = ["actions", "kisses", "type"]
    for index in range(action_nums):
        print("[INFO]{}:Begin to generate action {}".format(datetime.now().isoformat(), index))
        ret.append(generate_data("action"))
    for index in range(love_nums):
        print("[INFO]{}:Begin to generate love {}".format(datetime.now().isoformat(), index))
        ret.append(generate_data("love"))
    return pd.DataFrame(ret, columns=header)


def to_csv(path, df):
    """将DataFrame对象转换为csv文件并保存至指定路径"""
    now = datetime.now()
    save_path = os.path.join(path, str(now.month) + "-" + str(now.day) + ".csv")
    df.to_csv(save_path, encoding="utf-8")
    print("[INFO]{}:Save csv file to path:{} complete".format(datetime.now().isoformat(), save_path))


df_ret = generate_dataset(100, 200)
to_csv("./", df_ret)

