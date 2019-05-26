#!/usr/bin/env python3
#!coding:utf-8


from sklearn.feature_extraction.text import CountVectorizer

def countvec():
    """
    对文本进行特征值化
    """
    # 实例化
    cv = CountVectorizer()
    # fit_transform导入数据
    data = cv.fit_transform(['life is short, i like python', 'life is too long, i dislike python'])
    print(cv.get_feature_names())
    print(data.toarray())
    return None


if __name__ == "__main__":
    countvec()