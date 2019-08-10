#coding:utf-8

# kmp算法
# 一种无回溯的更高效的字符串匹配算法

# 比如字符集为 abcdabcdefabcdefg
# 需要匹配的为 abcdefg

# 1. 首先匹配到第一个a-e不匹配
# 2. 将abcdefg直接移动至不匹配的a位置
# 3. 匹配到第一个g-a不匹配
# 4. 将abcdeg直接移动到第二个a
# 5. 匹配成功


def kmp_matching(target, original, pnext):
    """
    kmp匹配算法 Main Function
    """
    i, j = len(target), len(original)
    m, n = 0, 0

    while i < m and j < n:
    	if i == -1 or target[i] == original[j]:
    		i, j = i+1, j+1
    	else:
    		i = pnext[i]

    if i == m:
    	return j - i

    return -1


def gen_pnext(original):
    """
    产生构造表
    """
    i, k, m = 0, -1, len(original)
    pnext = [-1] * m  # 初始元素全部为-1

    while i < m-1:
        if k == -1 or original[i] == original[k]:
            i, k = i+1, k+1
            pnext[i] = k
        else:
            pnext[k] = k

    return pnext


str1 = 'absdfsfsdfsdfsdfdjhjhhlhl'
pnext = gen_pnext(str1)
print(pnext)

