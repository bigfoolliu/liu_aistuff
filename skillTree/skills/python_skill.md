# python相关技巧

<!-- vim-markdown-toc Marked -->

* [1.变量](#1.变量)
* [2.条件分支](#2.条件分支)
* [3.数字和字符串](#3.数字和字符串)
* [4.python的容器操作(列表，元组等)](#4.python的容器操作(列表，元组等))
* [5.函数返回结果的技巧](#5.函数返回结果的技巧)
* [6.异常处理的技巧](#6.异常处理的技巧)
* [7.编写地道的循环](#7.编写地道的循环)
* [8.使用装饰器的技巧](#8.使用装饰器的技巧)
* [9.模块相关](#9.模块相关)
        * [9.1模块基本使用规则](#9.1模块基本使用规则)
        * [9.2模块以及缺失库导入](#9.2模块以及缺失库导入)
* [10.利用规则](#10.利用规则)
* [11.高效文件操作](#11.高效文件操作)
* [12.写好面向对象](#12.写好面向对象)
* [13.写好文档](#13.写好文档)
* [14.python包以及环境管理](#14.python包以及环境管理)
        * [14.1virtualenv](#14.1virtualenv)
        * [14.2pip](#14.2pip)
        * [14.3fabric](#14.3fabric)
        * [14.4python导包](#14.4python导包)
        * [14.5pyenv管理python版本](#14.5pyenv管理python版本)
        * [14.6python分发包步骤](#14.6python分发包步骤)
* [a.其他](#a.其他)

<!-- vim-markdown-toc -->

## 1.变量

- [如何编写优秀的python代码](https://github.com/piglei/one-python-craftsman)
- - bool类型：`is_superuser`,`allow_vip`,`has_error`
- int/float类型：`user_id`,`age`,`length_of_username`,`users_count`
- 适当使用[匈牙利命名法](https://blog.csdn.net/z_h_s/article/details/24007249)
- 尽量不要使用globals()/locals()
- 变量定义尽量靠近使用
- `使用namedtuple/dict来返回多个值，这样便于扩展和修改`
- 控制单个函数内的变量数量
- 能不用变量就不定义变量，及时删掉没用的变量

## 2.条件分支

1. `避免多层分支嵌套,使用raise或者return提前结束代码`
2. `封装过于复杂的逻辑判断到函数或者方法`
3. 留意不同的重复代码，消灭之
4. 谨慎只用三元表达式
5. 使用`德摩根定律`
6. 在条件判断中使用`all()/any()`
7. 留意and和or的运算优先级，`and优先级别高于or`

## 3.数字和字符串

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

## 4.python的容器操作(列表，元组等)

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

## 5.函数返回结果的技巧

1. 单个函数不要返回多种类型的结果
2. 当一个函数完全依赖另外一个函数来工作时，使用`partial`函数来构造函数[partial函数官方文档](https://docs.python.org/3.6/library/functools.html#functools.partial)
3. 函数抛出异常而不是返回和错误
4. 谨慎使用None作为函数返回值,`作为操作类函数的返回值，作为某些意料之中可能没有的值，作为调用失败代表错误结果的值`
5. 合理使用`空对象模式`,即`使用一个符合正常结果的接口的空类型来替代空值返回/抛出异常，从而降低调用方处理结果的成本`
6. 使用生成器函数代替返回列表，即使用`yield item替代append`
7. 限制递归的使用

## 6.异常处理的技巧

1. `只对可能出错的地方做最精确的异常捕获`
2. 别让异常破坏抽象的一致性，即`让模块只抛出与当前抽象层级一致的异常；在必要的地方进行异常的包装与转换`
3. `异常处理不应该太多，导致扰乱了核心的代码逻辑`可以使用`上下文管理器来改善流程`[python上下文管理器demo](../python/python/context_demo.py)

## 7.编写地道的循环

1. 使用函数修饰被迭代对象来优化循环
   1. 使用`itertools.product`扁平化多层嵌套循环`for i1, i2, i3 in product(list1, list1, list3)`
   2. 使用`itertools.islice`实现循环内隔行处理
   3. 使用`itertools.takewhile`替代break
   4. 使用生成器编写自定义的修饰函数
2. 按职责拆解循环体内复杂代码块
   1. 使用生成器函数解耦循环体

## 8.使用装饰器的技巧

1. 尝试使用类来实现装饰器`查看对象是否可以被调用，使用callable()函数，让类可以被调用只需要实现__call__方法`
   1. 更容易维护以及更容器扩充
   2. 更容易实现一个兼顾装饰器以及上下文管理器协议的对象
2. 使用`[wrapt模块](https://pypi.org/project/wrapt/)`实现更扁平的装饰器
3. 使用`functools.wraps()`函数装饰函数，可以不影响其所装饰的函数，仍然可以拿到被装饰函数的名称和文档等内容
4. 修改外层变量时候要使用**nonlocal**

## 9.模块相关

### 9.1模块基本使用规则

1. 合理的模块结构与分层
2. 合理的模块结构不是一成不变的，应该随着项目发展而调整
3. 项目内的模块间依赖的流向应该是单向的，不能有环形依赖

### 9.2模块以及缺失库导入

- [Python 中如何自动导入缺失的库？](https://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=2649642787&idx=1&sn=bda89629cee07aabd7a986001f226a6f&chksm=833db7c5b44a3ed3ae3d5af51d90464de9f46ba2315092ff8c409e22dcb0ea6cbf6478b2be84&mpshare=1&scene=24&srcid=&sharer_sharetime=1573813305411&sharer_shareid=20ab6c09eef32b49dbe03904652b9eb2#rd)

1. 使用try_except
2. 使用requirements.txt
3. 使用sys.meta_path可以自动导入任意缺失的库([autoinstall.py](./autoinstall.py))

## 10.利用规则

1. `将数据转换为自定义的对象，利用规则来计算`[利用集合计算](../python/python/other/ruler_demo.py)
2. `__hash__`方法解决问题，`__eq__`方法决定对象间逻辑相等

## 11.高效文件操作

1. 使用`pathlib模块`来使文件处理变得简单
2. `流式读取大文件`[大文件流式操作](../python/python/files/read_big_file.py)
3. 设计接受文件对象的函数

## 12.写好面向对象

尽量编写符合**SOLID**原则的代码。

1. **S**：单一职责原则，每一个类/函数只有一种职责
2. **O**: 开放-关闭原则，在不修改某个类的前提下，可以通过传入自定义的参数来扩展其行为
3. 使用`数据驱动思想`,将经常变动的东西完全以数据的方式抽离，当需求变动时候只需要改变数据，代码逻辑保持不变

## 13.写好文档

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

## 14.python包以及环境管理

### 14.1virtualenv

```sh
# 安装virtualenv
pip3 install virtualenv

virtualenv <venv>  # 使用默认的python解释器创建虚拟环境
virtualenv -p python3 <venv>  # 指定python解释器版本创建虚拟环境
virtualenv --no-site-packages <venv>  # 添加参数从而系统所有安装的第三方库都不会复制过来

source env/bin/activate  # 激活虚拟环境

deactivate  # 退出虚拟环境
```

### 14.2pip

- [pip常用指令个人总结](https://blog.csdn.net/weixin_40877924/article/details/98658669)

```sh
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple <package>  # 使用清华源下载包
python -m pip install --upgrade pip  # 更新pip

pip show <packge>  # 查看某个包是否安装
pip install --upgrade <package>  # 更新包
pip uninstall <package>  # 卸载包

pip install -r requirements.txt  # 从文件中同时安装多个包
pip freeze > requirements.txt  # 生成一个迁移文件
```

### 14.3fabric

- [python Fabric概览和教程](https://fabric-chs.readthedocs.io/zh_CN/chs/tutorial.html)
- [鼓励构建易于部署的应用-十二要素应用][https://12factor.net/]

使用fabric进行代码的部署:

在目标计算机上安装代码并执行，使用特定版本的应用或服务对最终用户可用的过程叫做部署.

```sh

```

### 14.4python导包

- [可能是python3史上最好的导包技巧](https://blog.csdn.net/weixin_38256474/article/details/81228492)

基础概念介绍：

- 模块(module): 一般情况下，是一个以.py为后缀的文件, 其他可作为module的文件类型还有”.pyo”、”.pyc”、”.pyd”、”.so”、”.dll”
- 包(package): 含有__init__.py的文件夹
- 使用`from p1 import *`则需要在 `__init__.py`文件中指明`__all__ = ['file1.py', 'file2.py']`,指定哪些文件在包导入时候被导入当前作用域
- `__path__`也是一个常用变量，是个列表，默认情况下只有一个元素，即当前包（package）的路径。修改__path__可改变包（package）内的搜索路径
- 导入一个包（package）时（会先加载__init__.py定义的引入模块，然后再运行其他代码），实际上是导入的它的__init__.py文件（导入时，该文件自动运行，助我们一下导入该包中的多个模块）

sys.modules,命名空间介绍：

- 将模块名称（module_name）映射到已加载的模块（modules） 的字典
- 模块内置属性：`__file__`, `__doc__`, `__name__`, `__dict__`, `__package__`, `__path__`

### 14.5pyenv管理python版本

- [简书介绍pyenv详细使用](https://www.jianshu.com/p/60f361822a7e)

```sh
# 1.ubuntu环境下下载pyenv, pyenv-virtualenv和编译python的依赖

# 下载
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

# 添加环境变量
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

# 安装编译python依赖
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev


# 2.安装指定的python版本

# 方式一，下载速度较慢，可能会失败
pyenv install 3.6.8

# 方式二
mkdir ~/.pyenv/cache
# 将提前下载好的指定版本的python安装包放到cache
pyenv install 3.6.8


# 3.创建，激活virtualenv
pyenv virtualenv 3.6.8 py368  # 创建虚拟环境并设置名字

pyenv global py368  # 全局切换
pyenv local py368  # 本地切换


# 当需要找到关联的解释器的时候,找到对应环境的路径
pyenv which python

# 列出所有可以安装的python版本
pyenv install --list

# 卸载某个版本的python
pyenv uninstall --force 3.6.8

# 列出所有已经安装的python
pyenv versions

# 当不再需要本地python的时候，用unset清除或者删除当前目录下的.python-version文件
pyenv local --unset

# 切换和使用虚拟环境
pyenv activate myenv

# 退出虚拟化环境
pyenv deactivate

# 4.删除虚拟环境
pyenv virtualenv-delete py368
```

### 14.6python分发包步骤

- [python配置打包包](https://packaging.python.org/guides/distributing-packages-using-setuptools/)

```sh
# 查看setup.py包含的命令
python setup.py --help-commands

# 分发包
python setup.py sdist

# 安装导出的包
# 方式一
python setup.py install
# 方式二
tar -xzvf a-1.0.1.tar.gz
cd a-1.0.1
python3 setup.py install
```

## a.其他

- [python必备的库](https://www.cnblogs.com/jiangchunsheng/p/9275881.html)
- [知乎：13个python最佳编程技巧](https://zhuanlan.zhihu.com/p/59897541)

