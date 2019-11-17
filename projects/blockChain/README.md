# 区块链最最基本演示

<!-- TOC -->

- [区块链最最基本演示](#%e5%8c%ba%e5%9d%97%e9%93%be%e6%9c%80%e6%9c%80%e5%9f%ba%e6%9c%ac%e6%bc%94%e7%a4%ba)
  - [1.区块链介绍](#1%e5%8c%ba%e5%9d%97%e9%93%be%e4%bb%8b%e7%bb%8d)
  - [2.使用flask交互](#2%e4%bd%bf%e7%94%a8flask%e4%ba%a4%e4%ba%92)

<!-- /TOC -->

## 1.区块链介绍

- 是由被称为区块的记录构成，记录可以是交易，文件或者任意想要的数据
- 记录通过hash连接
- 不可变的有序的链式结构

代码参考：

- [用python撸一个区块链](https://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=2649640551&idx=1&sn=cd484fbf5ed206cb27726eddf8dcc132&chksm=833dae81b44a27975de4eae2e560043bcc77ba98a3e37d57def416136413342c98052691ade6&mpshare=1&scene=24&srcid=&sharer_sharetime=1573842290193&sharer_shareid=20ab6c09eef32b49dbe03904652b9eb2#rd)

```python
# 一个新的区块
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
            }
        ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
    }
```

## 2.使用flask交互

三个接口：

1. /transactions/new 创建一笔新的交易
    {
        "sender": "my address",
        "recipient": "someone else's address",
        "amount": 5
    }

2. /mine 告诉服务器去挖掘新的区块
3. /chains 返回整个区块链

保证分布式一致的接口：

保证所有的节点运行在同一条链上。等待实现: TODO:

1. /nodes/register  接收以url的形式表示的新节点的列表
2. /nodes/resolves  用于执行一致性算法，解决冲突，确保节点拥有正确的链
