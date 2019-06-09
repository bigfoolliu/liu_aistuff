# 数学相关知识

## 范数(norm)

具有`长度`概念的函数

### 向量范数

#### 1-范数

即向量元素绝对值之和
$$||x||_1=\displaystyle \sum^{N}_{i=1}{|x_i|}$$

#### 2-范数

欧几里得范数，常用计算向量长度，即向量元素绝对值的平方和开方
$$||x||_2=\sqrt{\displaystyle \sum^{N}_{i=1}x_i^2}$$

#### $\infty$范数

即所有向量元素绝对值中的最大值
$$||X||_{\infty}=\displaystyle \max_i{|x_i|}$$

#### $-\infty$范数

即所有向量绝对值中的最小值
$$||X||_{-\infty}=\displaystyle \min_i{|x_i|}$$

#### $p$-范数

即向量元素绝对值中的P次方和的1/p次幂
$$||x||_p=(\displaystyle \sum^{N}_{i=1}|x_i|^p)^{\frac{1}{p}}$$
