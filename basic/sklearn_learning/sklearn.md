# sklearn相关知识

## 1. 10种机器学习算法

### 1.1线性回归(Linear Regression)

[线性回归算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

```python
from sklearn.linear_model import LinearRegression
module = LinearRegression()
module.fit(x, y)
module.score(x, y)
module.predict(test)
```

### 1.2逻辑回归(Logistic Regression)

[逻辑回归算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

```python
from sklearn.linear_model import LogisticRegression
module = LogisticRegression()
module.fit(x, y)
module.score(x, y)
module.predict(test)
```

### 1.3k-近邻(KNN)

[k近邻算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
module = KNeighborsClassifier(n_neighbors=6)
module.fit(x, y)
predicted = module.predict(test)
predicted = module.predict_proba(test)
```

### 1.4支持向量机(SVM)

[支持向量机算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

```python
from sklearn import svm
module = svm.SVC()
module.fit(x, y)
moduel.score(x, y)
module.predict(test)
module.predict_proba(test)
```

### 1.5朴素贝叶斯分类器(naive_bayes)

[朴素贝叶斯介绍](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

```python
from sklearn.naive_bayes import GaussianNB
module = GaussianNB()
module.fit()
```
