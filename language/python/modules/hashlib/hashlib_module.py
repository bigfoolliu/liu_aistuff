#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
hashlib模块的使用

python内置的hash函数：
返回一个对象(包括数字，字符串，对象等，不能是列表，字典和集合)的hash值，
可以用来校验数据传输过程中是否被篡改；
无论对象多长，返回的hash值长度固定


1、什么叫hash:hash是一种算法（不同的hash算法只是复杂度不一样）（3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384,
    SHA512 ，MD5 算法），该算法接受传入的内容，经过运算得到一串hash值
2、hash值的特点是(hash值/产品有三大特性：)：
    2.1 只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
    2.2 不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码（只能有内容返回hash值）
    2.3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的(如从网上下载文件要进行hash校验，保证网络传输没有丢包)

基于2.1和2.3可以做 文件下载一致性的校验
基于2.1和2.2可以 对用户密码进行加密

hash算法就像一座工厂，工厂接收你送来的原材料（可以用m.update()为工厂运送原材料），经过加工返回的产品就是hash值
"""

import hashlib


def md5_demo(_str=None):
    """md5示例"""
    if not _str:
        _str = 'pwd:123456'

    # 1.造出hash工厂
    _md5 = hashlib.md5()
    # 2.运送原材料, bytes类型
    _md5.update(_str.encode('utf-8'))
    # 3.产出hash值, bytes类型或者str
    print(_md5.digest())
    print(_md5.hexdigest())


def sha256_demo():
    """sha256示例"""
    # 1.造出hash工厂, sha256需要密钥
    _sha256 = hashlib.sha256('key'.encode('utf-8'))
    # 2.加密
    _sha256.update('pwd:123456'.encode('utf-8'))
    # 3.输出
    print(_sha256.digest())
    print(_sha256.hexdigest())


def verify_demo(file_a_path=None, file_b_path=None):
    """
    校验文件的一致性示例.可以将文件放到不同的两个盘，判断两个文件的hash值是否相等
    当两个文件的文件名不一致时候，不影响计算的hash值
    """
    _md5_a = hashlib.md5()
    if not file_a_path:
        file_a_path = './temp/a/a.txt'
    with open(file_a_path, 'rb') as f:
        for line in f:
            _md5_a.update(line)
    _hash_a = _md5_a.hexdigest()
    print(f'_hash_a: {_hash_a}')

    # 需要使用新的md5对象
    _md5_b = hashlib.md5()
    if not file_b_path:
        file_b_path = './temp/b/a.txt'
    with open(file_b_path, 'rb') as f:
        for line in f:
            _md5_b.update(line)
    _hash_b = _md5_b.hexdigest()
    print(f'_hash_b: {_hash_b}')

    if _hash_a == _hash_b:
        print(True)
    print(False)


if __name__ == '__main__':
    # md5_demo()
    # md5_demo('hello')
    # sha256_demo()
    verify_demo(file_b_path='./temp/b/b.txt')
