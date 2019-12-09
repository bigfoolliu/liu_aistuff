#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
snownlp库，一个中文文本处理的类库

所有的中文都是处理的Unicode编码

功能：

中文分词（Character-Based Generative Model）
词性标注（TnT 3-gram 隐马）
情感分析（现在训练数据主要是买卖东西时的评价，所以对其他的一些可能效果不是很好，待解决）
文本分类（Naive Bayes）
转换成拼音（Trie树实现的最大匹配）
繁体转简体（Trie树实现的最大匹配）
提取文本关键词（TextRank算法）
提取文本摘要（TextRank算法）
tf，idf
Tokenization（分割成句子）
文本相似（BM25）
支持python3（感谢erning）
"""


from snownlp import SnowNLP


def basic_demo():
    """基本展示"""
    s = SnowNLP(u"我很喜欢这个，讨厌那个")
    print(s.words)  # 分词
    print(s.tags, list(s.tags))  # 显示每个词语的语义
    print(s.sentiments)  # 语义为positive的概率
    print(s.pinyin)  # 显示文字的拼音


def long_text_demo():
    """长文本分析展示"""
    text = u'''
            自然语言处理是计算机科学领域与人工智能领域中的一个重要方向,
            它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
            自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
            因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
            所以它与语言学的研究有着密切的联系，但又有重要的区别。
            自然语言处理并不是一般地研究自然语言，
            而在于研制能有效地实现自然语言通信的计算机系统，
            特别是其中的软件系统。因而它是计算机科学的一部分。
            '''
    s = SnowNLP(text)
    print(s.keywords(3))  # 展示三个关键字
    print(s.summary(3))  # 显示三个总结语句
    print(s.sentences)  # 显示句子的列表


if __name__ == "__main__":
    # basic_demo()
    long_text_demo()
