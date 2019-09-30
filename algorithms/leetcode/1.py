#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 牺牲空间来换取时间
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return [dic[target - num], i]
        else:
            dic[num] = i


def _generate(n):
    # 产生一些测试的数组
    ret = []
    for i in range(n):
        import random
        num = random.randint(0, 20)
        ret.append(num)
    return ret


print("[INFO]Begin test")
import time
start_time = time.time()
print("[INFO]Start time is ", start_time)


# 进行100次测试
for i in range(100):
    nums = _generate(10)
    target = 15

    print("[INFO]Test {}, the test nums is:{}".format(i + 1, nums))
    ret = twoSum(nums, target)
    print("[INFO]The result is:", ret)

    print("\n")

end_time = time.time()
print("[INFO]Spend time:", end_time - start_time)
