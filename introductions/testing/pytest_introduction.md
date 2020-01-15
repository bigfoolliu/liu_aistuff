# pytest模块介绍

<!-- TOC -->

- [pytest模块介绍](#pytest%e6%a8%a1%e5%9d%97%e4%bb%8b%e7%bb%8d)
  - [1.基础工具](#1%e5%9f%ba%e7%a1%80%e5%b7%a5%e5%85%b7)
    - [assert](#assert)
    - [pytest.raises()](#pytestraises)
    - [标记函数](#%e6%a0%87%e8%ae%b0%e5%87%bd%e6%95%b0)

<!-- /TOC -->

单元和功能测试模块。

```shell
pytest test.py  # 使用pytest运行测试函数
pytest -v test.py  # 可以显示测试更详细的信息
pytest -h  # 查看pytest的所有选项
```

## 1.基础工具

### assert

断言。

```python
assert a > b
```

### pytest.raises()

测试是否如期抛出预期的异常，进行异常捕获。

```python
with pytest.raises(TypeError) as e:
    pass
```

### 标记函数

默认pytest会递归查找当前目录下的所有以test开始或结尾的python脚本，并执行所有以test开始或结束的函数或方法。
