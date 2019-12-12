#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
简单的文本情感分析
"""


import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas
from snownlp import SnowNLP


def read_comments(file_path=None):
    """
    读取文件中的追加评论
    :param file_path: str,文件加文件名完整路径
    :return: DataFrame
    """
    data = pandas.read_csv(file_path)
    append_comments = list(data["追加评论"])
    return append_comments


def emotion_analysis(comments):
    """
    单句情感分析
    :param comments: list
    :return: list
    """
    sentiments = []
    for comment in comments:
        print("分析语句：", comment)
        s = SnowNLP(comment)
        s_sentiment = s.sentiments
        print("其情感度为: ", s_sentiment)
        print("\n")
        sentiments.append(s_sentiment)
    return sentiments


def filter_sentiments(sentiments):
    """
    过滤情感度大于1的假数据
    :return list
    """
    return list(filter(lambda x: float(x) <= 1.0, sentiments))


def save_graph(sentiments, fig_path):
    """
    保存直方图
    :param sentimens: list，情感度列表
    :fig_path: str,保存图像的路径
    :return:
    """
    plt.hist(sentiments)
    plt.xlabel("emotions")
    plt.ylabel("comments")
    plt.savefig(fig_path)


def pickle_dump(obj, file_path):
    """将python列表序列化为文件"""
    with open(file_path, "wb") as f:
        pickle.dump(obj, f)


def pickle_load(file_path):
    """
    将文件内容反序列化为python列表
    :return: list
    """
    with open(file_path, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":

    # for csv_dir in os.listdir("./csvs"):
    #     item_dir = os.path.join("./csvs", csv_dir)
    #     csv_full_path = os.path.join(item_dir, csv_dir+".csv")
        
    #     print("处理文件:", csv_full_path)
    #     append_comments = read_comments(csv_full_path)

    #     append_sentiments = emotion_analysis(append_comments)
    #     append_sentiments = filter_sentiments(append_sentiments)
    #     dump_file_path = os.path.join(item_dir, csv_dir+".txt")
    #     print("序列评论至: ", dump_file_path)
    #     pickle_dump(append_sentiments, dump_file_path)

    #     print("\n")
    

    for csv_dir in os.listdir("./csvs"):
        item_dir = os.path.join("./csvs", csv_dir)

        load_file_path = os.path.join(item_dir, csv_dir+".txt")
        print("反序列化文件：", load_file_path)

        sentiments = pickle_load(load_file_path)
        fig_save_path = os.path.join(item_dir, csv_dir+".jpg")

        print("保存图像至：", fig_save_path)
        save_graph(sentiments, fig_save_path)
        print("\n")
