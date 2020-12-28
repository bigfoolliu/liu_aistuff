#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
pybloom_live 模块

布隆过滤器实现使用，以应对redis的缓存穿透, 参考: https://www.cnblogs.com/yscl/p/12003359.html
redis使用布隆过滤器：https://redislabs.com/blog/rebloom-bloom-filter-datatype-redis/

应用：

1. 网页爬虫对URL的去重，避免爬取相同的URL地址
2. 反垃圾邮件，从数十亿个垃圾邮件列表中判断某邮箱是否垃圾邮箱（同理，垃圾短信）
3. 缓存穿透，将所有可能存在的数据缓存放到布隆过滤器中，当黑客访问不存在的缓存时迅速返回避免缓存及DB挂掉
4. 黑名单过滤
"""


from pybloom_live import ScalableBloomFilter, BloomFilter


def ScalableBloomFilter_demo():
    # 可自动扩容的布隆过滤器
    s_bloomer = ScalableBloomFilter(initial_capacity=100, error_rate=0.001)
    url1 = 'http://www.baidu.com'
    url2 = 'http://www.tencent.com'

    s_bloomer.add(url1)
    # 判断key是否在该过滤器中
    print(url1 in s_bloomer) 
    print(url2 in s_bloomer)


def BloomFilter_demo():
    # BloomFilter是定长的
    bloomer = BloomFilter(capacity=100, error_rate=0.01)
    
    url1 = 'http://www.baidu.com'
    url2 = 'http://www.tencent.com'

    bloomer.add(url1)
    # 判断key是否在该过滤器中
    print(url1 in bloomer) 
    print(url2 in bloomer)


if __name__ == "__main__":
    # ScalableBloomFilter_demo()
    BloomFilter_demo()
