---
layout: post
title: "18种和“距离(distance)”、“相似度(similarity)”相关的量的小结"
background: red
background-image: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535557261869&di=26fa8f88702fbc95ad0b102658c090b7&imgtype=0&src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201410%2F02%2F20141002195730_ywXJB.jpeg
categories: 
- 深度学习
tags: 
- 损失函数
author: Dimension
description: 这是一些在深度学习图像处理过程中，如果不想用交叉熵损失，可以用这些距离作为损失
ico: chat
---

在计算机人工智能领域，距离(distance)、相似度(similarity)是经常出现的基本概念，它们在自然语言处理、计算机视觉等子领域有重要的应用，而这些概念又大多源于数学领域的度量(metric)、测度(measure)等概念。 
这里拮取其中18种做下小结备忘，也借机熟悉markdown的数学公式语法。

<style>
table
{
    font-family:serif;
    width:100%;
    word-break:break-all; 
    word-wrap:break-all;
}
th
{
    background-color:#bdc3c7;
}
td,th
{
	text-align:center;
}
.left
{
    text-align:left;
    width:40%;
}
.equation
{
    text-align:left;
    width:40%;
}
.name_en{
    width:10%;
}
.name_cn{
    width:10%;
}
</style>

<table border="1">
<tr>
<th class="name_en">英文名</th>
<th class="name_cn">中文名</th>
<th class="equation">算式</th>
<th class="left">说明</th>
</tr>

<tr>
<td>Euclidean Distance</td>
<td>欧式距离</td>
<td>$d=\sqrt{\sum_{i=1}^n(x_i-y_i)^2}$</td>
<td>以古希腊数学家欧几里得命名的距离；也就是我们直观的两点之间直线最短的直线距离</td>
</tr>

<tr>
<td>Manhattan Distance</td>
<td>曼哈顿距离</td>
<td>$d=\sum_{i=1}^{n}|x_i-y_i|$</td>
<td>是由十九世纪的赫尔曼·闵可夫斯基所创词汇；是种使用在几何度量空间的几何学用语，用以标明两个点在标准坐标系上的绝对轴距总和；也就是和象棋中的“車”一样横平竖直的走过的距离；曼哈顿距离是超凸度量</td>
</tr>

<tr>
<td>Minkowski Distance</td>
<td>闵氏距离</td>
<td>$d=\sqrt[p]{\sum_{i=1}^{n}(x_i-y_i)^p}$</td>
<td>以俄罗斯数学家闵可夫斯基命名的距离；是欧式距离的推广，p=2时等价于欧氏距离，和p-范数等值</td>
</tr>

<tr>
<td>Hamming Distance</td>
<td>海明距离</td>
<td>逐个字符(或逐位)对比，统计不一样的位数的个数总和</td>
<td>所得值越小，参与对比的两个元素约相似；下面是从wikipedia借的4bit的海明距离示意图 <img src="{{site.baseurl}}/assets/images/2018-8-27/13.png" width="40%" height="40%"></td>
</tr>

<tr>
<td>Jaccard Coefficient</td>
<td>杰卡德距离</td>
<td>$J(A,B)=\frac{|A\cap{B}|}{A\cup{B}}$</td>
<td>越大越相似；分子是A和B的交集大小，分母是A和B的并集大小</td>
</tr>

<tr>
<td>Ochiai Coefficient</td>
<td>？</td>
<td>$K=\frac{n(A\cap{B})}{\sqrt{n(A)\times{n(B)}}}$</td>
<td></td>
</tr>

<tr>
<td>Pearson Correlation</td>
<td>皮尔森相关系数</td>
<td>$r=\frac{\sum_{i=1}^{n}(X_i-\overline{x})(y_i-\overline{y})}{\sqrt{\sum_{i=1}^{n}(X_i-\overline{x})^2}\sqrt{\sum_{i=1}^{n}(y_i-\overline{y})^2}}$</td>
<td>分子是两个集合的交集大小，分母是两个集合大小的几何平均值。是余弦相似性的一种形式</td>
</tr>

<tr>
<td>Cosine Similarity</td>
<td>余弦相似度</td>
<td>$S=\frac{x\cdot{y}}{|x||y|}$</td>
<td></td>
</tr>

<tr>
<td>Mahalanobis Distance</td>
<td>马氏距离</td>
<td>$d=\sqrt{(\overrightarrow{x}-\overrightarrow{y})^T{S^{-1}}(\overrightarrow{x}-\overrightarrow{y})}$<br>其中S是x和y的协方差矩阵</td>
<td>印度统计学家马哈拉诺比斯(P. C. Mahalanobis)提出的，表示数据的协方差距离。它是一种有效的计算两个未知样本集的相似度的方法；若协方差矩阵是对角阵(diagonal)，则该距离退化为欧式距离</td>
</tr>

<tr>
<td>Kullback-Leibler Divergence</td>
<td>K-L散度</td>
<td>$D(P||Q)=\sum_{i=1}^{n}P(i)log{\frac{P(i)}{Q(i)}}$</td>
<td>即相对熵；是衡量两个分布(P、Q)之间的距离；越小越相似</td>
</tr>

<tr>
<td>PMI(Pointwise Mutual Information)</td>
<td>点对互信息</td>
<td>$pmi=log{\frac{p(x,y)}{p(x)p(y)}}=log{\frac{p(y|x)}{p(y)}}$</td>
<td>利用co-occurance来衡量x和y的相似度；越大越相关；可以看做局部点的互信息(mutual information)</td>
</tr>

<tr>
<td>NGD(Normalized Google Distance)</td>
<td>？</td>
<td>$NGD(x,y)=\frac{max\{logf(x),logf(y)\}-logf(x,y)}{logM-min\{logf(x),logf(y)\}}$</td>
<td>这是google用来衡量两个不同的关键字(keyword)的检索结果之间的相关程度；其中f(x)代表包含了关键字x的页面数量，f(x,y)代表同时包含了关键字x和关键字y的页面的数量，M代表google所搜索的总页数；若两个关键字总是成对出现在页面上，那么NGD值为0，相反的，如果两个关键字在所有页面上都没有同时出现过，那么NGD值为无穷；该量是从normalized compression distance (Cilibrasi & Vitanyi 2003)衍生而来的</td>
</tr>

<tr>
<td>Levenshtein Distance(Edit Distance)</td>
<td>Levenshtein距离(编辑距离)</td>
<td>$$  f(n)=\begin{cases} 
max(i,j) & \text {if min(i,j)=0} \\ 
\begin{cases}
lev_{a,b}(i-1,j)+1 & \\
lev_(a,b)(i,j-1)+1 & \\
lev_{a,b}(i-1,j-1)+1
\end{cases} & \text{otherwise}
\end{cases}$$</td>
<td>是指两个字串之间，由一个转成另一个所需的最少编辑操作次数；俄罗斯科学家Vladimir Levenshtein在1965年提出这个概念；编辑距离越小的两个字符串越相似，当编辑距离为0时，两字符串相等</td>
</tr>

<tr>
<td>Jaro-Winkler Distance</td>
<td>？</td>
<td>$$
\begin{cases}
0, & \text{if m=0}\\
\frac{1}{3}(\frac{m}{s_1}+\frac{m}{s_2}+\frac{m-t}{m}) & \text{otherwise}
\end{cases}
$$</td>
<td></td>
</tr>

<tr>
<td>Lee Distance</td>
<td>李氏距离</td>
<td>$$d=\sum_{i=1}^{n}|x_i-y_i|$$</td>
<td>在编码理论(coding theory)中两个字符串间距离的一种度量方法</td>
</tr>

<tr>
<td>Hellinger Distance</td>
<td>？</td>
<td>$$H^2(P,Q)=\frac{1}{\sqrt{2}}\sqrt{\int(\sqrt{\frac{dP}{d\lambda}}-\sqrt{\frac{dQ}{d\lambda}})^2{d\lambda}}\\
当\frac{dP}{d\lambda},\frac{dQ}{d\lambda}为概率密度函数时，进一步有\\
H^2(P,Q)=\sqrt{1-\int{\sqrt{f(x)g(x)}\,{\rm d}x}}$$</td>
<td>注意在作为概率意义的计算时需在测度空间进行；通常被用来度量两个概率分布的相似度，它是f散度的一种；由Ernst Helligner在1909年引进</td>
</tr>

<tr>
<td>Canberra Distance</td>
<td>坎贝拉距离</td>
<td>$$d(\vec p,\vec q)=\sum_{i=1}^{n}\frac{|p_i-q_i|}{|p_i|+|q_i|}\\where\\
\vec p=(p_1,p_2,...p_n)\\and\\
\vec q=(q_1,q_2,..q_n)$$</td>
<td></td>
</tr>

<tr>
<td>Chebyshev Distance</td>
<td>切比雪夫距离</td>
<td>$$
\begin{equation}
\begin{aligned}
D_{Chebyshev}(p,q)&=max_{i}(|p_i-q_i|)\\
&=lim_{k \to +\infty}(\sum_{i=1}^{n}|p_i-q_i|^k)^{\frac{1}{k}}
\end{aligned}
\end{equation} 
$$</td>
<td>切比雪夫距离是由一致范数(uniform norm)(或称为上确界范数)所衍生的度量，也是超凸度量</td>
</tr>
</table>




