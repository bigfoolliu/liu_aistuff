#!/usr/bin/env python3
#!coding:utf-8


import jieba
from sklearn.feature_extraction.text import CountVectorizer


def cutword():
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

 
def hanzivec():
    """
    中文特征值化
    :return:None
    """
    c1, c2 = cutword()
    print(c1, '\n', c2)

    cv = CountVectorizer()
    data = cv.fit_transform([c1, c2])

    print(cv.get_feature_names())
    print(data.toarray())


if __name__ == "__main__":
    hanzivec()