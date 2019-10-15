# effiency提高效率的小技巧

<!-- TOC -->

- [effiency提高效率的小技巧](#effiency提高效率的小技巧)
    - [1.为命令设置别名(alias)](#1为命令设置别名alias)
    - [2.dotfiles快速将恢复自身配置](#2dotfiles快速将恢复自身配置)
    - [3.项目里重复的工作写成makefile](#3项目里重复的工作写成makefile)
    - [4.快速为项目选择一个source license](#4快速为项目选择一个source-license)
    - [5.量化工作](#5量化工作)
    - [6.会话以及终端管理tmux](#6会话以及终端管理tmux)
    - [7.windows虚拟桌面(workspace)](#7windows虚拟桌面workspace)
    - [8.必读书籍](#8必读书籍)
    - [9.开发者工具](#9开发者工具)
    - [10.chrome高效使用](#10chrome高效使用)
    - [11.ssh免密以及别名登录](#11ssh免密以及别名登录)
    - [12.python代码](#12python代码)
        - [12.1变量](#121变量)
        - [12.2条件分支](#122条件分支)
        - [12.3使用数字和字符串的技巧](#123使用数字和字符串的技巧)
        - [12.4python的容器操作(列表，元组等)](#124python的容器操作列表元组等)
        - [12.5函数返回结果的技巧](#125函数返回结果的技巧)
        - [12.6异常处理的技巧](#126异常处理的技巧)
        - [12.7编写地道的循环](#127编写地道的循环)
        - [12.8使用装饰器的技巧](#128使用装饰器的技巧)
        - [12.9模块相关](#129模块相关)
        - [12.10利用规则](#1210利用规则)
        - [12.11高效文件操作](#1211高效文件操作)
        - [12.12写好面向对象](#1212写好面向对象)
        - [12.13写好文档](#1213写好文档)
    - [13.HTTP Api设计指南](#13http-api设计指南)

<!-- /TOC -->

[效率指南](https://leohxj.gitbooks.io/a-programmer-prepares/effciency/coder-guide.html)

## 1.为命令设置别名(alias)

[alias为命令设置别名](https://blog.csdn.net/doiido/article/details/43762791)

## 2.dotfiles快速将恢复自身配置

[dotfiles入门](https://luolei.org/dotfiles-tutorial/)
[dotfiles合集](http://dotfiles.github.io/)

## 3.项目里重复的工作写成makefile

[makefile由浅入深](https://zhuanlan.zhihu.com/p/47390641)

## 4.快速为项目选择一个source license

[chooselicense.com](https://choosealicense.com)

## 5.量化工作

[quantify your code](https://blog.newrelic.com/culture/quantify-your-code/)

## 6.会话以及终端管理tmux

[使用tmux加速操作](http://cenalulu.github.io/linux/tmux/)

## 7.windows虚拟桌面(workspace)

[win10虚拟桌面](https://sspai.com/post/45594)

- win + ctrl + d: 创建新的虚拟桌面
- win + ctrl + left/right: 左右切换虚拟桌面
- win + ctrl + f4: 删除当前的虚拟桌面
- win + w: windowslink工作区
- win + e: 打开资源管理器
- win + r, psr.exe：打开步骤计数器

## 8.必读书籍

[程序员必读书单](http://lucida.me/blog/developer-reading-list/)

## 9.开发者工具

[免费开发工具](https://github.com/ripienaar/free-for-dev)

## 10.chrome高效使用

- ctrl + t: 打开新的标签页
- ctrl + n: 打开新的窗口
- ctrl + pgUp/pgDown: 切换标签页
- ctrl + w/f4: 关闭当前标签页
- alt + space + n: 最小化当前窗口
- alt + space + x: 最大化当前窗口

## 11.ssh免密以及别名登录

```shell
# 1.本地生成公钥和私钥,默认放置路径为~/.ssh/id_rsa以及~/.ssh/id_rsassh-keygen.pub
# 需要输入一个密码需要记忆,如果输入为空则为免密登录
ssh-keygen
# 2.将本地的公钥放到远程主机
ssh-copy-id ubuntu@192.168.6.121
# 3.登录时候需要输入自己的密码或者为空
ssh ubuntu@192.168.6.121

# 如果需要将远程主机取别名在~.ssh/config文件中加入
Host 1
    HostName 192.168.1.1
    User ubuntu
    Port 22
```

## 12.python代码

- [如何编写优秀的python代码https://github.com/piglei/one-python-craftsman](https://github.com/piglei/one-python-craftsman)

### 12.1变量

1. bool类型：`is_superuser`,`allow_vip`,`has_error`
2. int/float类型：`user_id`,`age`,`length_of_username`,`users_count`
3. 适当使用[匈牙利命名法](https://blog.csdn.net/z_h_s/article/details/24007249)
4. 尽量不要使用globals()/locals()
5. 变量定义尽量靠近使用
6. `使用namedtuple/dict来返回多个值，这样便于扩展和修改`
7. 控制单个函数内的变量数量
8. 能不用变量就不定义变量，及时删掉没用的变量

### 12.2条件分支

1. `避免多层分支嵌套,使用raise或者return提前结束代码`
2. `封装过于复杂的逻辑判断到函数或者方法`
3. 留意不同的重复代码，消灭之
4. 谨慎只用三元表达式
5. 使用`德摩根定律`
6. 在条件判断中使用`all()/any()`
7. 留意and和or的运算优先级，`and优先级别高于or`

### 12.3使用数字和字符串的技巧

1. 少用数字字面量，即类似`users[0], type==1`等,而是将重复出现的数字字面量定义为`枚举类型`
2. 不要在裸字符串上处理太多，即`不要使用基本的加减乘除配合基本函数等处理字符串，获得结果`,试着`根据字符串是否为结构化的来使用开源的对象化模块来操作或者使用模板引擎来处理`
3. 不必预计算字面量表达式,如`不要替换7*24*3600为604800`
4. 布尔值也是数字
5. 改善超长字符串的可读性
6. python中的无穷大`float("inf")为无穷大；float("-inf")为无穷小`

```python
# 超长字符串的处理

# 1.括号
logging.info(("this is a super super super super super long"
            "logging info"))

# 2.使用\
logging.info("this is a super super super super super long \
                logging info")

# 3.多级缩进出现长字符串
# 可以将其作为变量提取到模块的外层或者使用内置模块textwrap
from textwrap import dedent
def main():
    if user.is_active:
        # dedent 将会缩进掉整段文字最左边的空字符串
        message = dedent("""\
            Welcome, today's movie list:
            - Jaw (1975)
            - The Shining (1980)
            - Saw (2004)""")
```

### 12.4python的容器操作(列表，元组等)

1. 多使用`yield`来返回生成器对象
2. 尽量使用生成器表达式替代列表推导式,即使用`(i for i in range(100))`而不是`[i for i in range(100)]`
3. 尽量使用模块的懒惰对象`re.finditer而不是re.findall`,`for line in fp而不是for line in fp.readlines()`
4. 列表头部操作多的场景使用`deque`模块
5. 使用集合/字典来判断成员是否存在
6. `关注容器的抽象属性，而非容器类型本身，如列表元组的抽象属性为 是否可迭代，是否可修改，是否有长度等`
7. 在更多的地方使用`动态解包`,即用`*或者**`解开可迭代运算对象,合并字典`{**dict1, **dict2}`
8. 尽量省略那些非核心的异常捕获逻辑
   1. 操作字典成员时候，使用`collections.defaultdict`或者使用`dict[key]=dict.setdefault(key, 0)+1`内建函数
   2. 移除字典成员，不要关心是否存在，设置默认值`dict.pop(key, None)`
   3. 字典获取成员时设置默认值`dict.get(key, default_value)`
   4. 列表进行不存在的切片访问不会抛出IndexError`["fool"][100:200]`
9. 使用`next`函数，配合生成器表达式可以高效实现从列表查找第一个满足条件的元素`print(next(i for i in list1 if i % 2 == 0))`
10. 使用`有序字典`去重,即`collections.OrderedDict`,去重的同时保留了顺序
11. 不要在循环体里修改被迭代，可能会导致某些成员不能被遍历到,`使用一个空的可迭代对象来保存结果或者使用yield返回一个生成器`

### 12.5函数返回结果的技巧

1. 单个函数不要返回多种类型的结果
2. 当一个函数完全依赖另外一个函数来工作时，使用`partial`函数来构造函数[partial函数官方文档](https://docs.python.org/3.6/library/functools.html#functools.partial)
3. 函数抛出异常而不是返回和错误
4. 谨慎使用None作为函数返回值,`作为操作类函数的返回值，作为某些意料之中可能没有的值，作为调用失败代表错误结果的值`
5. 合理使用`空对象模式`,即`使用一个符合正常结果的接口的空类型来替代空值返回/抛出异常，从而降低调用方处理结果的成本`
6. 使用生成器函数代替返回列表，即使用`yield item替代append`
7. 限制递归的使用

### 12.6异常处理的技巧

1. `只对可能出错的地方做最精确的异常捕获`
2. 别让异常破坏抽象的一致性，即`让模块只抛出与当前抽象层级一致的异常；在必要的地方进行异常的包装与转换`
3. `异常处理不应该太多，导致扰乱了核心的代码逻辑`可以使用`上下文管理器来改善流程`[python上下文管理器demo](../python/python/context_demo.py)

### 12.7编写地道的循环

1. 使用函数修饰被迭代对象来优化循环
   1. 使用`itertools.product`扁平化多层嵌套循环`for i1, i2, i3 in product(list1, list1, list3)`
   2. 使用`itertools.islice`实现循环内隔行处理
   3. 使用`itertools.takewhile`替代break
   4. 使用生成器编写自定义的修饰函数
2. 按职责拆解循环体内复杂代码块
   1. 使用生成器函数解耦循环体

### 12.8使用装饰器的技巧

1. 尝试使用类来实现装饰器`查看对象是否可以被调用，使用callable()函数，让类可以被调用只需要实现__call__方法`
   1. 更容易维护以及更容器扩充
   2. 更容易实现一个兼顾装饰器以及上下文管理器协议的对象
2. 使用`[wrapt模块](https://pypi.org/project/wrapt/)`实现更扁平的装饰器
3. 使用`functools.wraps()`函数装饰函数，可以不影响其所装饰的函数，仍然可以拿到被装饰函数的名称和文档等内容
4. 修改外层变量时候要使用**nonlocal**

### 12.9模块相关

1. 合理的模块结构与分层
2. 合理的模块结构不是一成不变的，应该随着项目发展而调整
3. 项目内的模块间依赖的流向应该是单向的，不能有环形依赖

### 12.10利用规则

1. `将数据转换为自定义的对象，利用规则来计算`[利用集合计算](../python/python/other/ruler_demo.py)
2. `__hash__`方法解决问题，`__eq__`方法决定对象间逻辑相等

### 12.11高效文件操作

1. 使用`pathlib模块`来使文件处理变得简单
2. `流式读取大文件`[大文件流式操作](../python/python/files/read_big_file.py)
3. 设计接受文件对象的函数

### 12.12写好面向对象

尽量编写符合**SOLID**原则的代码。

1. **S**：单一职责原则，每一个类/函数只有一种职责
2. **O**: 开放-关闭原则，在不修改某个类的前提下，可以通过传入自定义的参数来扩展其行为
3. 使用`数据驱动思想`,将经常变动的东西完全以数据的方式抽离，当需求变动时候只需要改变数据，代码逻辑保持不变

### 12.13写好文档

1. 专注于想法，然后审查和写文本，即`先随便写核心点，然后写完整`
2. 准确定位读者，从的角度来写
3. 使用简短的句子
4. 写符合内容的标题
5. 文档中使用项目中的代码作为示例
6. 文档内容以实用为主
7. 使用模板
8. 使用`python docstring 文档字符串给代码做注释`(控制器中使用help(func)查看)
9. 使用`pydoc在控制台中查看文档`
   1. `python -m pydoc xxx`查看模块注释
   2. `python -m pydoc -w xxx`查看模块注释并输出html文档
   3. `python -m pydoc -p port`启动本地服务器来查看文档信息
   4. `python -m pydoc -k xxx`查找模块

## 13.HTTP Api设计指南

- [http api设计指南中文版](https://github.com/ZhangBohan/http-api-design-ZH_CN)

**要点**:

- 资源名：使用复数形式为命名
- 行为：如`/runs/{id}/actions/stop`
- 最小化嵌套路径，即父子路径的嵌套关系不宜过深
- 响应：
  - `200`: GET请求成功，及DELETE或PATCH同步请求完成，或者PUT同步更新一个已存在的资源
  - `201`: POST 同步请求完成，或者PUT同步创建一个新的资源
  - `202`: POST，PUT，DELETE，或PATCH请求接收，将被异步处理
  - `206`: GET 请求成功，但是只返回一部分
  - `401`: Unauthorized: 用户未认证，请求失败
  - `403`: Forbidden: 用户无权限访问该资源，请求失败
  - `422`: Unprocessable Entity: 请求被服务器正确解析，但是包含无效字段
  - `429`: Too Many Requests: 因为访问频繁，你已经被限制访问，稍后重试
  - `500`: Internal Server Error: 服务器错误，确认状态并报告问题
- 提供资源的(UU)ID：默认给每一个资源id属性，最好uuid
- 提供标准的时间戳：为资源提供默认的创建时间和更新时间
- 使用UTC时间(世界标准时间)，并用ISO8601格式化
- 嵌套外键关系：使用嵌套对象序列化外键关联
- 生成结构化的错误
- 抱枕想用json最小化，多余的空格会增加响应的大小
