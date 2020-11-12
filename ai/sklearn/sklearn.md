# sklearn

<!-- vim-markdown-toc Marked -->

* [1. 10种机器学习算法](#1.-10种机器学习算法)
        - [1.1线性回归(Linear Regression)](#1.1线性回归(linear-regression))
        - [1.2逻辑回归(Logistic Regression)](#1.2逻辑回归(logistic-regression))
        - [1.3k-近邻(KNN)](#1.3k-近邻(knn))
        - [1.4支持向量机(SVM)](#1.4支持向量机(svm))
        - [1.5朴素贝叶斯分类器(naive_bayes)](#1.5朴素贝叶斯分类器(naive_bayes))
        - [1.6决策树分类器(Decision Tree)](#1.6决策树分类器(decision-tree))
        - [1.7k-means聚类（K-Means)](#1.7k-means聚类（k-means))
        - [1.8随机森林(Random Forest)](#1.8随机森林(random-forest))
        - [1.9Gradient Boosting 和 AdaBoost算法(GBDT)](#1.9gradient-boosting-和-adaboost算法(gbdt))
        - [1.10PCA特征降维(PCA)](#1.10pca特征降维(pca))

<!-- vim-markdown-toc -->

## 1. 10种机器学习算法

### 1.1线性回归(Linear Regression)

- [线性回归算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

```python
from sklearn.linear_model import LinearRegression
module = LinearRegression()
module.fit(x, y)
module.score(x, y)
module.predict(test)
```

### 1.2逻辑回归(Logistic Regression)

- [逻辑回归算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

```python
from sklearn.linear_model import LogisticRegression
module = LogisticRegression()
module.fit(x, y)
module.score(x, y)
module.predict(test)
```

### 1.3k-近邻(KNN)

- [k近邻算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
module = KNeighborsClassifier(n_neighbors=6)
module.fit(x, y)
predicted = module.predict(test)
predicted = module.predict_proba(test)
```

### 1.4支持向量机(SVM)

- [支持向量机算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

```python
from sklearn import svm
module = svm.SVC()
module.fit(x, y)
module.score(x, y)
module.predict(test)
module.predict_proba(test)
```

### 1.5朴素贝叶斯分类器(naive_bayes)

- [朴素贝叶斯介绍](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

```python
from sklearn.naive_bayes import GaussianNB
module = GaussianNB()
module.fit()
```

### 1.6决策树分类器(Decision Tree)

- [决策树分类器介绍](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)

```python
from sklearn import tree
module = tree.DecisionTreeClassifier(criterion="gini")
module.fit(x, y)
module.score(x, y)
module.predict(test)
```

### 1.7k-means聚类（K-Means)

- [k-means聚类算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

```python
from sklearn.cluster import KMeans
module = KMeans(n_cluster=3, random_stat=0)
module.fit(x, y)
module.predict(test)
```

### 1.8随机森林(Random Forest)

- [随机森林算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
module = RandomForestClassifier()
module.fit(x, y)
module.predict(test)  
```

### 1.9Gradient Boosting 和 AdaBoost算法(GBDT)

- [GBDT算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)

```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
module = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=1, random_stat=0)
module.fit(x, y)
module.predict(test)
```

### 1.10PCA特征降维(PCA)

- [PCA特征降维算法介绍](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

```python
from sklearn.decomposition import PCA
train_reduced = PCA.fit_transform(train)
test_reduced = PCA.transform(test)
```

