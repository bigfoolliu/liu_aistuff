#!/usr/bin/env python
#!coding:utf-8


"""
利用装饰器实现python的内存缓存
"""
import time
import pickle
import hashlib
from functools import wraps


_cache = {}


def _is_absolete(entry, duration):
    """
    判断缓存内容是否过期
    :param entry: 输入的内容
    :param duration: 持续时间
    """
    if duration == -1:  # 永远不过期
        return False
    return time.time() - entry["time"] > duration


def _compute_key(function, *args, **kargs):
    """
    序列化并求其哈希值
    """
    key = pickle.dumps((function.__name__, args, kargs))  # 将函数名及其参数进行序列化处理
    return hashlib.sha1(key).hexdigest()  # 将摘要值作为十六进制数字字符串返回


def momorize(duration=-1):
    """自动缓存"""
    def _memorize(function):
        @wraps(function)  # 自动复制函数信息
        def __memorize(*args, **kargs):
            key = _compute_key(function, args, kargs)
            # 是否缓存
            if key in _cache:
                if _is_absolete(_cache[key], duration) is False:  # 在缓存里且未过期
                    return _cache[key]["value"]
            # 运行函数
            result = function(*args, **kargs)
            # 保存结果
            _cache[key] = {
                    "value": result,
                    "time": time.time()
                    }
            return result
        return __memorize
    return _memorize


# 具体使用
@momorize(3)  # 设定3秒的过期时间
def test_func(n):
    """需要测试的函数"""
    print("[INFO]Test function starts.")
    print("[INFO]Test functions running...")
    time.sleep(n)
    print("[INFO]Test function ends.")
    return n


for i in range(5):
    test_func(i)
    print("[INFO]_cache: {}".format(_cache))

# 再次写入同样的内容查看是否会过滤
test_func(2)
print("[INFO]_cache: {}".format(_cache))
