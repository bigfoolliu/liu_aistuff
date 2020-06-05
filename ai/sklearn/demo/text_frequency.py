#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
TfidfVectorizer(stop_words=None,...)
    返回词的权重矩阵
    TfidfVectorizer.fit_transform(x)
        x:文本或者包含文本字符串的可迭代对象
        返回值:返回sparse矩阵
    TfidfVectorizer.inverse_transform(x)
        x:array数组或者sparse矩阵
        返回值:转换之前的格式
    TfidfVectorizer.get_feature_names()
        返回值:单词列表
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import jieba


def cut_word():
    """
    中文分词
    """
    con1 = jieba.cut('今天很残酷，明天更残酷，后天很美好，但绝大部分人都死在明天的晚上，见不到后天的太阳')
    con2 = jieba.cut('我们看到的从遥远星系发出的光是几百万年以前发出的，因此当我们看到宇宙时，我们是在看他的过去')
    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    # 列表转换为字符串，以空格隔开
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    return c1, c2


def tfidfvec():
    """
    返回词的权重矩阵
    """
    c1, c2 = cut_word()
    print(c1, '\n', c2)

    tf = TfidfVectorizer()
    data = tf.fit_transform([c1, c2])

    print(tf.get_feature_names())
    print(data.toarray())


if __name__ == "__main__":
    tfidfvec()
