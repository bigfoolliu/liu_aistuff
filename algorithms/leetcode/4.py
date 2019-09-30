#!/usr/bin/env python
#!coding:utf-8


"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:

        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5
"""


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    def findKth(A, B, k):
        """
        find the kth smallest number
        :type A: List(int)
        :type B: List(int)
        :rtype: float
        """
        if len(A) == 0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]

        if k == 1:
            return min(A[0], B[0])
        
        a = A[k // 2 - 1] if len(A) >= k // 2 else None
        b = B[k // 2 - 1] if len(B) >= k // 2 else None

        if b is None or (a is not None and a < b):
            return findKth(A[k // 2:], B, k - k // 2)
        return findKth(A, B[k // 2:], k - k // 2)

    n = len(nums1) + len(nums2)
    #　如果两个数组的长度之和为奇数，则两者中间的数，否则取中间两个数的均值
    if n % 2 == 1:
        return findKth(nums1, nums2, n // 2 + 1)
    else:
        smaller = findKth(nums1, nums2, n // 2)
        bigger = findKth(nums1, nums2, n // 2 + 1)
        return (smaller + bigger) / 2.0


from funcs import datas
nums1 = datas._generate_list(10, 0, 9)
nums2 = datas._generate_list(6, 0, 9)

print("[INFO]nums1:{}".format(nums1))
print("[INFO]nums2:{}".format(nums2))

ret = findMedianSortedArrays(nums1, nums2)
print("[INFO]the result is:{}".format(ret))
