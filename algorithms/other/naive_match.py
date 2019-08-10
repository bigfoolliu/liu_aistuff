#coding:utf-8

# 朴素串字符匹配
# 效率极低的一种字符串匹配算法


def naive_matching(target, original):
    """
    target:需要匹配的字符串,比如 efg
    original:字符集合 abcdefghijkl
    """
    len_t = len(target)
    len_o = len(original)

    i, j = 0, 0
    while i < len_t and j < len_o:
        # 找到首字母
        if target[i] == original[j]:
            print(i, j)
            i, j = i+1, j+1
        # 字符不同，考虑original中的下一位置
        else:
            i, j = 0, j-i+1
    if i == len_t:
        return j - i

    return -1


str1 = 'abc'
print(len(str1))
str2 = 'asdnfjasdbfskjdbfsjdbfoasdfoahfowuhfoweuhabcsdfsdhfoehif'
print(len(str2))

ret = naive_matching(str1, str2)

print(ret)

