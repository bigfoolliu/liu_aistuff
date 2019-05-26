# liu_aistuff

stuff about ai

## 计算模型－计算图

```python
# Define constant and calcilate

import tensoflow as tf
a = tf.constant([1.0, 2.0], name="a")
ret = tf.add(a, a, name="ret")  # 或ret = a + a


# Define variable
weights = tf.Variable(tf.random_normal([2, 3], stddev=2))  # 声明一个2*3的矩阵变量,矩阵中的元素是均值为0，标准差为2的随机数
```

## 运算模型－会话

Kye words:

- learning rate(学习率)
- activation(激活函数)
- relularization(正则化)
- batch_size: 每批数据量的大小
- iteration: 1个iteration即迭代一次，即用batch_size个样本训练一次
- epoch: 1个epoch指用训练集中的全部样本训练一次

使用神经网络解决分类问题的主要步骤:

1. 提取问题中的实体的特征向量作为神经网络的输入
2. 定义神经网络的结构，并定义如何从神经网络的输入得到输出
3. 通过训练数据来调整神经网络中的参数
4. 使用训练好的神经网络来进行预测工作

Tensorflow:

- 使用图(graph)来表示计算任务
- 在被称之为会话(session)和上下文(context)中执行图
- 使用tensor来表示数据
- 通过变量(Variable)维护状态
- 使用feed和feth可以为任意的操作(arbitrary operation)赋值或者从中获取数据

## MachineLearning

热门领域：
1.人脸识别
2.自动驾驶
3.医疗健康

训练数据-->训练程序-->生成模型<-->预测程序<-->应用环境

推荐书籍：
《机器学习》，周志华，清华大学出版社
《机器学习实战》
《python数据分析与挖掘实战》
《机器学习系统设计》
《面向机器智能TensorFlow实践》
《TensorFlow技术解析与实战》

实际应用：
深度学习(TensorFlow, Caffe)
分布式计算(Hadoop, Spark)
分布式存储(HDFS, MongoDB, Redis)

## 1. 机器学习概述

视频介绍：[机器学习简述](D:/桌面文件/机器学习入门视频/第一节/1.机器学习简介.mp4)

### 1.1 目前应用场景

- 图像识别
- 医疗方面的CT图识别
- 图片艺术化
- 新闻机器人
- 自然语言处理
- 信贷需要预测
- 店铺需求预测

### 1.2 机器学习库和框架

- scikit-learn
- tensorflow
- caffe
- chainer

### 1.3 基本目标

- 熟悉机器学习各类算法的原理
- 掌握算法的使用，结合具体场景解决实际问题
- 掌握使用机器学习算法库和框架的技能

### 1.4 数据集

可用数据集：

- kaggle(大数据竞赛平台，数据量大，真实，科学家使用)
- UCI(专业，覆盖各个领域)
- scikit-learn(数据量小便于学习)

常用数据集数据的结构组成：

- 特征值+目标值

注：有些数据集可以没有目标值

数据集中对于数据的处理：

- pandas库：对数据进行简单处理
- 缺失值要数据转换
- 重复值不需要去重
- 针对不同的特征值是需要不同的转换，然后计算处理
- skikit-learn库：对于特征的处理提供了强大的接口

### 1.5 特征工程

#### 1.5.1 特征抽取：

```python
import sklearn.feature_extraction
```

- 特征抽取对文本进行特征值化
- 对字典数据进行特征值化(类：`sklearn.feature_extraction.DictVectorizer`)

```python
'''
字典特征提取:
把字典中一些类型数据分别转换成特征，数值特征（int, float等）不必要转换
'''

from sklearn.feature_extraction import DictVectorizer

def dectvec():
    """
    字典数据抽取函数
    """
    # 实例化
    dict = DictVectorizer()
    # 调用fit_transform
    data = dict.fit_transform([{'city':'北京','temperature':'100'},
                                {'city':'上海','temperature':'90'},
                                {'city':'深圳','temperature':'70'},
                                {'city':'广州','temperature':'80'}])
    print(dict.get_feature_names())
    print(data)
    return None


if __name__ == "__main__":
    dectvec()
```

运行结果为：

```.
['city=上海', 'city=北京', 'city=广州', 'city=深圳', 'temperature=100', 'temperature=70', 'temperature=80', 'temperature=90']
  (0, 1)        1.0
  (0, 4)        1.0
  (1, 0)        1.0
  (1, 7)        1.0
  (2, 3)        1.0
  (2, 5)        1.0
  (3, 2)        1.0
  (3, 6)        1.0
```

返回的格式为：sparse矩阵格式

另一编码方式：one-hot

- 文本特征抽取(类：`sklearn.feature_extraction.text.CountVectorizer`)

```python
from sklearn.feature_extraction.text import CountVectorizer

def countvec():
    """
    对文本进行特征值化
    """
    # 实例化
    cv = CountVectorizer()
    # fit_transform导入数据
    data = cv.fit_transform(['life is short, i like python', 'life is too long, i dislike python'])
    print(cv.get_feature_names())
    print(data.toarray())
    return None


if __name__ == "__main__":
    countvec()
```

返回结果为：

```.
['dislike', 'is', 'life', 'like', 'long', 'python', 'short', 'too']
[[0 1 1 1 0 1 1 0]
 [1 1 1 0 1 1 0 1]]
```

在返回的结果中：

1. 统计所有文章中的所有词，重复的只看作一次
2. 对每篇文章，在词的列表里进行统计每个词出现的次数
3. 单个字母不进行统计(因为没有分类依据)
4. 文本特征抽取可用于文本的分类，情感的分析等

#### 1.5.2 中文文本特征抽取

上面的代码更改：`data = cv.fit_transform(['人生苦短，我用python', '人生漫长，我不用python'])`

返回结果为：

```.
['人生漫长', '人生苦短', '我不用python', '我用python']
[[0 1 0 1]
 [1 0 1 0]]
 ```

 结果无意义，不能作为分类依据，默认不支持中文文本特征抽取，因此要进行分词处理，从而使用到jieba库。

 jieba分词：

```python
import jieba
from sklearn.feature_extraction.text import CountVectorizer

def cutword():
    """
    中文分词
    """
    con1 = jieba.cut('今天很残酷，明天更残酷，后天很美好，但绝大部分人都死在明天的晚上，见不到后天的太阳')
    con2 = jieba.cut('我们看到的从遥远星系发出的光是几百万年以前发出的，因此当我们看到宇宙时，我们是在看他的过去')
    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    # 列表转换为字符串，以空格隔开
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    return c1, c2


def hanzivec():
    """
    中文特征值化
    :return:None
    """
    c1, c2 = cutword()
    print(c1, '\n', c2)

    cv = CountVertorizer()
    data = cv.fit_transform([c1, c2])

    print(cv.get_feature_names())
    print(data.toarray())


if __name__ == "__main__":
    hanzivec()
```

返回结果为：

```.
今天 很 残酷 ， 明天 更 残酷 ， 后天 很 美好 ， 但 绝大部分 人 都 死 在 明天 的 晚上 ， 见 不到 后天 的 太阳
 我们 看到 的 从 遥远 星系 发出 的 光是 几百万年 以前 发出 的 ， 因此 当 我们 看到 宇宙 时 ， 我们 是 在 看 他 的 过去
['不到', '今天', '以前', '光是', '几百万年', '发出', '后天', '因此', '太阳', '宇宙', '我们', '明天', '星系', '晚上', '残酷', '看到', '绝大部分', '美好', '过去', '遥远']
[[1 1 0 0 0 0 2 0 1 0 0 2 0 1 2 0 1 1 0 0]
 [0 0 1 1 1 2 0 1 0 1 3 0 1 0 0 2 0 0 1 1]]
 ```

#### 1.5.3 特征工程之文本`tfidf`

- tf:term frenquency，词的频率
- idf:inverse document frequency，逆文档频率，计算公式(log(总文档数量/改词出现的文档数量))
- `重要性=tf*idf`

```python
'''
TfidfVectorizer(stop_words=None,...)
    返回词的权重矩阵
    TfidfVectorizer.fit_transform(x)
        x:文本或者包含文本字符串的可迭代对象
        返回值:返回sparse矩阵
    TfidfVectorizer.inverse_transform(x)
        x:array数组或者sparse矩阵
        返回值:转换之前的格式
    TfidfVectorizer.get_feature_names()
        返回值:单词列表
'''
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba

def cutword():
    """
    中文分词
    """
    con1 = jieba.cut('今天很残酷，明天更残酷，后天很美好，但绝大部分人都死在明天的晚上，见不到后天的太阳')
    con2 = jieba.cut('我们看到的从遥远星系发出的光是几百万年以前发出的，因此当我们看到宇宙时，我们是在看他的过去')
    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    # 列表转换为字符串，以空格隔开
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    return c1, c2

def tfidfvec():
    """
    返回词的权重矩阵
    """
    c1, c2 = cutword()
    print(c1, '\n', c2)

    tf = TfidfVectorizer()
    data = tf.fit_transform([c1, c2])

    print(tf.get_feature_names())
    print(data.toarray())


if __name__ == "__main__":
    tfidfvec()
```

返回结果为：

```.
今天 很 残酷 ， 明天 更 残酷 ， 后天 很 美好 ， 但 绝大部分 人 都 死 在 明天 的 晚上 ， 见 不到 后天 的 太阳
 我们 看到 的 从 遥远 星系 发出 的 光是 几百万年 以前 发出 的 ， 因此 当 我们 看到 宇宙 时 ， 我们 是 在 看 他 的 过去
['不到', '今天', '以前', '光是', '几百万年', '发出', '后天', '因此', '太阳', '宇宙', '我们', '明天', '星系', '晚上', '残酷', '看到', '绝大部分', '美好', '过去', '遥远']
[[0.23570226 0.23570226 0.         0.         0.         0.
  0.47140452 0.         0.23570226 0.         0.         0.47140452
  0.         0.23570226 0.47140452 0.         0.23570226 0.23570226
  0.         0.        ]
 [0.         0.         0.2        0.2        0.2        0.4
  0.         0.2        0.         0.2        0.6        0.
  0.2        0.         0.         0.4        0.         0.
  0.2        0.2       ]]
  ```

在结果中，**其中数字越大则说明该词在文中的重要性越高，也可以选出其中的词做进一步的分析**。

#### 1.5.4 特征工程之特征预处理

通过特定统计方法将数学转换成算法要求的数据。

```.
特征预处理方式：
数值型数据：标准缩放(1.归一化；2.标准化)
类别型数据：one-hot编码
时间类型：时间的切分
```

- 归一化：通过对原始数据进行变换映射到(默认为[0,1])之间，**当特征同等重要的时候，常常需要进行归一化处理**，但是归一化对异常点的处理不佳，即**鲁棒性较差**，只适合传统精确小数据场景。

公式：

![归一化计算公式](resource/归一化计算公式.png)

公式中，每一列表示每一个特征，每一行表示每一个样本，x''为最终目标。

```python
'''
sklearn归一化API：sklearn.preprocessing.MinMaxScaler
    MinMaxScaler(featrure_range(0,1),...)
        每个特征值的缩放给定范围默认为[0,1]
    MinMaxScaler.fit_transform(x)
        x：numpy array格式的数据[n_samples,n_features]
        返回值：转换后的形状相同的array

归一化步骤：
1.实例化MinMaxScaler
2.通过fit_transform()转换
'''

from sklearn.preprocessing import MinMaxScaler

def mm():
    """
    归一化处理
    :return:None
    """
    mm = MinMaxScaler()
    data = mm.fit_transform([[90,2,10,40],[60,4,15,15]])

    print(data)
    return None


if __name__ == "__main__":
    mm()
```

所得结果为：

```.
[[1. 0. 0. 1.]
 [0. 1. 1. 0.]]
 ```

- 标准化：通过对原始数据进行变化把数据变换到均值为0，方差为1的范围。在有一定的数据量情况下，少量异常点不会影响平均值。计算公式如下：

![标准化公式](resource/标准化计算公式.png)

```python
'''
sklearn标准化API：sklearn.preprocessing.StandardScaler
    StandardScaler.fit_transform(x)
        x：numpy array格式数据[n_samples,n_features]
        返回值：转换后的形式相同的array
    StandardScaler.mean_
        原始数据(训练集)中每列特征的平均值
    StandardScaler.var_
        原始数据每列特征的方差
'''

from sklearn.preprocessing import StandardScaler

def ss():
    """
    标准化
    :return:None
    """
    std = StandardScaler()
    data = std.fit_transform([[2, 3, 5, 7],[1, 8, 2, 9],[3, 4, 6, 5]])
    print(std.mean_, '\n')
    print(std.var_, '\n')
    print(data)
    return None


if __name__ == "__main__":
    ss()
```

所得结果为：

```.
[2.         5.         4.33333333 7.        ]

[0.66666667 4.66666667 2.88888889 2.66666667]

[[ 0.         -0.9258201   0.39223227  0.        ]
 [-1.22474487  1.38873015 -1.37281295  1.22474487]
 [ 1.22474487 -0.46291005  0.98058068 -1.22474487]]
 ```

#### 1.5.5 数据的降维之特征选择

降维即降低特征的数量。特征选择就是单纯地从提取到的所有特征中选择部分特征作为训练集特征，特征在选择前后可以改变值，也可以不改变值，但是选择后的特征维数肯定比之前小。

数据降维方式：

- 特征选择
- 主成分分析

特征选择原因：

- 冗余：部分特征的相关度高，容易消耗计算性能
- 噪声：部分特征对预测结果又影响

特征选择主要方法(三种)：

- Filter(过滤式)：VarianceThreshold
- Embedded(嵌入式)：正则化、决策树
- Wrapper(包裹式)：较少用

```python
'''
sklearn特征选择API：sklearn.feature_selection.VarianceThreshold()
    VarianceThreshold(threshold=0.0)
        删除所有低方差特征
    Variance.fit_transform(x)
        x:numpy array格式的数据[n_samples, n_features]
        返回值：训练集中差异低于threshold的特征将被删除
        默认值为保留所有非零方差的特征，即删除所有样本中具有相同值的特征
'''
from sklearn.feature_selection import VarianceThreshold

def var():
    """
    特征选择，删除低方差的特征
    :return:None
    """
    var = VarianceThreshold()
    data = var.fit_transform([[1, 2, 3 , 4],[0, 2, 5, 4],[8, 2, 6, 7]])

    print(data)
    return None


if __name__ == "__main__":
    var()
```

返回结果为：

```.
[[1 3 4]
 [0 5 4]
 [8 6 7]]
```

结果中删除了一个特征(其特征值为2)。

主成分分析(PCA)

同时改变数据的特征数量和特征数值。因为当特征数量较多的时候，很多特征可能相关。

```python
'''
PCA(n_components=None)
    将数据分解为较低的维数空间
    n_components:为小数时，表示保留0-100%的信息，基本取90-95%的数据信息最好；为整数时，表示减少到的特征数量，使用较少
    PCA.fit_transform(x)
        x:numpy array格式的数据[n_samples, n_features]
        返回值：转换后指定维度的array
'''
from sklearn.decomposition import PCA

def pca():
    """
    主成分分析
    :return:None
    """
    pca = PCA(n_components=0.92)

    data = pca.fit_transform([[2, 0, 2, 34], [23, 3, 43, 5], [12, 3, 54, 6], [23, 45, 5, 67]])
    print(data)
    return None


if __name__ == "__main__":
    pca()
```

所得结果为：

```.
[[ 11.98214361  28.28081114]
 [-29.76854569  -5.86084474]
 [-35.58732941  -7.68093023]
 [ 53.3737315  -14.73903617]]
```

结果显示当保留92%的数据信息时，特征数量减少为两个，同时剩余特征的特征值也发生了变化。

### 1.6 机器学习开发流程

1. 算法是核心，数据和计算是基础。
2. 找准定位，复杂的模型算法由算法工程师做，主要做：</br>
    2.1 分析数据</br>
    2.2 分析具体的业务</br>
    2.3 应用常见的算法</br>
    2.4 特征工程，调参数，优化</br>
3. 需要能力：</br>
    3.1 学会分析问题，使用机器学习的目的以及需要解决的任务</br>
    3.2 掌握算法基本思想，学会对问题用相应的算法解决</br>
    3.3 学会用库和框架解决问题</br>

***开发流程：***

(1)获得数据

- 公司本身就有数据
- 合作过来的数据
- 购买的数据

(2)明确问题

- 根据**目标值**的数据类型划分模型种类，数据基本处理(缺失值，合并表等)。

(3)特征工程

- 对特征进行处理。

(4)找到合适算法预测

- 分类，回归等等
- 建立模型(算法+数据)

(5)评估模型

- 到达一定的准确率合格即可
- 不合格则可以考虑换算法，调整参数，特征工程等

(6)上线使用

- 即以API的形式提供。

### 1.7 机器学习算法分类

数据类型：离散型(数据为整数)，连续型(长度，时间，质量等，数据为非整数)

#### 1.7.1 监督学习(预测，特征值+目标值)

- 分类(目标值离散型)：k-近邻算法，贝叶斯分类，决策树与随机森林，逻辑回归，神经网络
- 回归(目标值连续型)：线性回归，岭回归
- 标注：隐马尔科夫模型

#### 1.7.2 非监督学习(特征值)

- 聚类：K-means算法

### 1.8 回归算法之线性回归
