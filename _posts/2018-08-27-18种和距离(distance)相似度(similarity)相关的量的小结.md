---
layout: post
title: 18种和“距离(distance)”、“相似度(similarity)”相关的量的小结
categories: 
- 深度学习
tags: 
- 数学
author: Dimension
---

在计算机人工智能领域，距离(distance)、相似度(similarity)是经常出现的基本概念，它们在自然语言处理、计算机视觉等子领域有重要的应用，而这些概念又大多源于数学领域的度量(metric)、测度(measure)等概念。 
这里拮取其中18种做下小结备忘，也借机熟悉markdown的数学公式语法。

| 英文名 | 中文名 | 算式 | 说明 | 
| ------------- |:-------------:| -----:| -----:| 
| Euclidean Distance | 欧式距离 | $d=\sqrt{\sum_{i=1}^n(x_i-y_i)^2}$ | 	以古希腊数学家欧几里得命名的距离；也就是我们直观的两点之间直线最短的直线距离|
|Manhattan Distance|曼哈顿距离|$d=\sum_{i=1}^{n}|x_i-y_i|$|	是由十九世纪的赫尔曼·闵可夫斯基所创词汇；是种使用在几何度量空间的几何学用语，用以标明两个点在标准坐标系上的绝对轴距总和；也就是和象棋中的“車”一样横平竖直的走过的距离；曼哈顿距离是超凸度量|
|Minkowski Distance|闵氏距离|$d=\sqrt[p]{\sum_{i=1}^{n}(x_i-y_i)^p}$|	以俄罗斯数学家闵可夫斯基命名的距离；是欧式距离的推广，p=2时等价于欧氏距离，和p-范数等值|
|Hamming Distance|海明距离|逐个字符(或逐位)对比，统计不一样的位数的个数总和|	所得值越小，参与对比的两个元素约相似；下面是从wikipedia借的4bit的海明距离示意图![这里写图片描述](https://img-blog.csdn.net/20180817210320214?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dzYzEyMzU4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)|
|Jaccard Coefficient|杰卡德距离|$J(A,B)=\frac{|A\cap{B}|}{A\cup{B}}$|	越大越相似；分子是A和B的交集大小，分母是A和B的并集大小|
|Ochiai Coefficient|?|$K=\frac{n(A\cap{B})}{\sqrt{n(A)\times{n(B)}}}$||
|Pearson Correlation|皮尔森相关系数|$r=\frac{\sum_{i=1}^{n}(X_i-\overline{x})(y_i-\overline{y})}{\sqrt{\sum_{i=1}^{n}(X_i-\overline{x})^2}\sqrt{\sum_{i=1}^{n}(y_i-\overline{y})^2}}$|	分子是两个集合的交集大小，分母是两个集合大小的几何平均值。是余弦相似性的一种形式|
|Cosine Similarity|余弦相似度|$S=\frac{x\cdot{y}}{|x||y|}$||
|Mahalanobis Distance|马氏距离|$d=\sqrt{(\overrightarrow{x}-\overrightarrow{y})^T{S^{-1}}(\overrightarrow{x}-\overrightarrow{y})}$其中S是x和y的协方差矩阵|印度统计学家马哈拉诺比斯(P. C. Mahalanobis)提出的，表示数据的协方差距离。它是一种有效的计算两个未知样本集的相似度的方法；若协方差矩阵是对角阵(diagonal)，则该距离退化为欧式距离|
|Kullback-Leibler Divergence|K-L散度|$D(P||Q)=\sum_{i=1}^{n}P(i)log{\frac{P(i)}{Q(i)}}$|	即相对熵；是衡量两个分布(P、Q)之间的距离；越小越相似|
|PMI(Pointwise Mutual Information)|点对互信息|$pmi=log{\frac{p(x,y)}{p(x)p(y)}}=log{\frac{p(y|x)}{p(y)}}$|	利用co-occurance来衡量x和y的相似度；越大越相关；可以看做局部点的互信息(mutual information)|
|NGD(Normalized Google Distance)|?|$NGD(x,y)=\frac{max\{logf(x),logf(y)\}-logf(x,y)}{logM-min\{logf(x),logf(y)\}}$|	这是google用来衡量两个不同的关键字(keyword)的检索结果之间的相关程度；其中f(x)代表包含了关键字x的页面数量，f(x,y)代表同时包含了关键字x和关键字y的页面的数量，M代表google所搜索的总页数；若两个关键字总是成对出现在页面上，那么NGD值为0，相反的，如果两个关键字在所有页面上都没有同时出现过，那么NGD值为无穷；该量是从normalized compression distance (Cilibrasi & Vitanyi 2003)衍生而来的|
|Levenshtein Distance(Edit Distance)|Levenshtein距离(编辑距离)|$$  f(n)=\begin{cases} 
max(i,j) & \text {if min(i,j)=0} \\ 
\begin{cases}
lev_{a,b}(i-1,j)+1 & \\
lev_(a,b)(i,j-1)+1 & \\
lev_{a,b}(i-1,j-1)+1
\end{cases} & \text{otherwise}
\end{cases}$$|是指两个字串之间，由一个转成另一个所需的最少编辑操作次数；俄罗斯科学家Vladimir Levenshtein在1965年提出这个概念；编辑距离越小的两个字符串越相似，当编辑距离为0时，两字符串相等|
|Jaro-Winkler Distance|?|$$
\begin{cases}
0, & \text{if m=0}\\
\frac{1}{3}(\frac{m}{s_1}+\frac{m}{s_2}+\frac{m-t}{m}) & \text{otherwise}
\end{cases}
$$||
|Lee Distance|李氏距离|$$d=\sum_{i=1}^{n}|x_i-y_i|$$|在编码理论(coding theory)中两个字符串间距离的一种度量方法|
|Hellinger Distance|?|$$H^2(P,Q)=\frac{1}{\sqrt{2}}\sqrt{\int(\sqrt{\frac{dP}{d\lambda}}-\sqrt{\frac{dQ}{d\lambda}})^2{d\lambda}}\\
当\frac{dP}{d\lambda},\frac{dQ}{d\lambda}为概率密度函数时，进一步有\\
H^2(P,Q)=\sqrt{1-\int{\sqrt{f(x)g(x)}\,{\rm d}x}}$$|注意在作为概率意义的计算时需在测度空间进行；通常被用来度量两个概率分布的相似度，它是f散度的一种；由Ernst Helligner在1909年引进|
|Canberra Distance|坎贝拉距离|$$d(\vec p,\vec q)=\sum_{i=1}^{n}\frac{|p_i-q_i|}{|p_i|+|q_i|}\\where\\
\vec p=(p_1,p_2,...p_n)\\and\\
\vec q=(q_1,q_2,..q_n)$$||
|Chebyshev Distance|切比雪夫距离|$$D_{Chebyshev}(p,q)=max_{i}(|p_i-q_i|)=lim_{k \to +\infty}(\sum_{i=1}^{n}|p_i-q_i|^k)^{\frac{1}{k}}$$|切比雪夫距离是由一致范数(uniform norm)(或称为上确界范数)所衍生的度量，也是超凸度量|

 