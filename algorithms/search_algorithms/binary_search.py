"""
二分搜索
"""
import sys
import bisect


def binary_search(sorted_collection, item):
    """
    使用纯python实现二分搜索
    Pure implementation of binary search algorithm in Python"""
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None


def binary_search_std_lib(sorted_collection, item):
    """
    通过python自带的库实现二分搜索
    Pure implementation of binary search algorithm in Python using stdlib"""
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None


def binary_search_by_recursion(sorted_collection, item, left, right):
    """
    通过迭代实现二分搜索
    Pure implementation of binary search algorithm in Python by recursion"""
    if (right < left):
        return None
    
    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint-1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint+1, right)


def __assert_sorted(collection):
    """判断输入的数组是否为有序的数组"""
    if collection != sorted(collection):
        raise ValueError('Collection must be ascending sorted')
    return True


if __name__ == '__main__':
    # 使用逗号分隔输入有序数字
    user_input = input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be ascending sorted to apply binary search')

    target_input = input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    result = binary_search(collection, target)

    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')
