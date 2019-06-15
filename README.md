# liu_aistuff

stuff about ai

## 计算模型－计算图

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

- 特征抽取对文本进行特征值化
- 对字典数据进行特征值化(类：`sklearn.feature_extraction.DictVectorizer`)

返回的格式为：sparse矩阵格式

另一编码方式：one-hot

- 文本特征抽取(类：`sklearn.feature_extraction.text.CountVectorizer`)

在返回的结果中：

1. 统计所有文章中的所有词，重复的只看作一次
2. 对每篇文章，在词的列表里进行统计每个词出现的次数
3. 单个字母不进行统计(因为没有分类依据)
4. 文本特征抽取可用于文本的分类，情感的分析等

#### 1.5.2 中文文本特征抽取

要进行分词处理，从而使用到jieba库。

#### 1.5.3 特征工程之文本`tfidf`

- tf:term frenquency，词的频率
- idf:inverse document frequency，逆文档频率，计算公式(log(总文档数量/改词出现的文档数量))
- `重要性=tf*idf`

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

公式中，每一列表示每一个特征，每一行表示每一个样本，x''为最终目标。

- 标准化：通过对原始数据进行变化把数据变换到均值为0，方差为1的范围。在有一定的数据量情况下，少量异常点不会影响平均值。计算公式如下：

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

主成分分析(PCA)

同时改变数据的特征数量和特征数值。因为当特征数量较多的时候，很多特征可能相关。

结果显示当保留92%的数据信息时，特征数量减少为两个，同时剩余特征的特征值也发生了变化。

### 1.6 机器学习开发流程

1. 算法是核心，数据和计算是基础。
2. 找准定位，复杂的模型算法由算法工程师做，主要做:
  2.1 分析数据
  2.2 分析具体的业务
  2.3 应用常见的算法
  2.4 特征工程，调参数，优化
3. 需要能力:
  3.1 学会分析问题，使用机器学习的目的以及需要解决的任务
  3.2 掌握算法基本思想，学会对问题用相应的算法解决
  3.3 学会用库和框架解决问题

***开发流程***

(1)获得数据

- 公司本身就有数据
- 合作过来的数据
- 购买的数据
- 爬虫获得数据

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

#### 1.7.2 无监督学习(特征值)

- 聚类：K-means算法

#### 如何选择合适的算法

- 根据机器学习算法的目的
  - 预测目标变量的值：监督学习算法，然后确定目标变量类型，离散型则可选择`分类器算法`，连续型可选择`回归算法`
  - 非预测目标变量的值：无监督学习算法，然后确定是否需要将数据划分为离散的组，是的话则使用`聚类算法`，如果还需要估计数据与分组的相似度，则需要使用`密度估计算法`
