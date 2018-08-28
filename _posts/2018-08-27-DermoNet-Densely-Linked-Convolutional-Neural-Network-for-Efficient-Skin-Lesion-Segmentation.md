---
layout: post
title: "DermoNet:Densely Linked Convolutional Neural Network for Efficient Skin Lesion Segmentation"
categories: 
- 论文
- 深度学习
tags: 
- 图像分割
author: Dimension
description: 提出了一种新的分割网络，对皮肤病变图进行分割，创新点为使用了Unet的encoder和decoder原理，连接了残差块，接了DenseNet的特点，网络较大
---

# 简介
在这篇论文中，我们提出了一个有效的全卷积网络(CNN)，叫DermoNet。用于皮肤损伤的分割，允许实时计算。在此多谢我们的密集连接全卷积块(densely connected convolutional blocks)和跳跃连接(skip connections)。网络层可以重新使用前面层的信息和确保后面网络层的高精度。
![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/8.png)

----------
这篇论文的主要贡献：
 1. 将DenseNet转换为一个全卷积网络。特别的，我们的结构由encoder部分的多个dense块组成，并加入一个decoder path来恢复输入图像的分辨率。这将帮助来自不同层的多尺度特征图受到损失函数的惩罚。
 2. encoder和decoder之间有多个跳跃连接，特别地，我们将每个dense block的输出与每个特征分辨率下相应的decoder连接起来。这样做将使网络能够处理前面层的高分辨率特征以及更深层的高语义特性。
 3. 由于我们只对前一个dense block生成的特征图进行了上样，所以所提出的网络使用的参数更少。这样可以使网络在有限的计算预算内达到最佳的精度。
# DermoNet
在训练这个网络时，我们使用了重新调整大小的皮肤镜图片，大小为384x512。被选择的图片尺寸时用来平衡计算代价和分割性能的。测试阶段，首先，对图像进行重新调整，并使用DermoNet模型生成后验概率图，其中每个像素值对应于病变或皮肤的概率。然后，给DermoNet模型输出的二值mask应用一个阈值。
![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/9.png)
## 1 网络结构
网络结构如图3，DermoNet网络包含两个部分：向右的encoder和向左的decoder。
![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/10.png)
![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/12.png)
![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/11.png)
encoder开始有个块，该块用大小为7x7，步长为2的卷积核对输入图像进行卷积，接下来是一个步长为2 的最大池化。encoder后面的部分由4个dense块构成，每一个块有4个层，dense块结构如图4，dense块中每个层的输出特征维都有k个特征图，它们连接到输入。在每个dense块这个操作被重复4次，dense块的输出时前一层输出的连接。如方程1所示

$$x_l=F_l([x_{l-1},x_{l-2},...,x_0])$$

其中$x_l$表示$l$层的输出特征，$F(\cdot)$是非线性函数，定义为卷积后的ReLu并且$[...]$表示连接操作。在DermoNet结构中，encoder的输出被连接到对应的decoder中，使用跳跃连接的好处是可以恢复有encoder下采样丢失的空间信息。
## 2 损失函数
交叉熵损失经常用于分割任务，然而，图像中皮肤损伤的部分只占很小的一部分。用交叉熵损失函数训练的分割网络往往偏向于背景图像而不是损伤本身。这篇论文中，我们使用了基于 Jaccard distance ($L_J$) 的损失,它是Jaccard指数的补充。

$$L_J=1-\frac{\sum_{i,j}(t_{ij} p_{ij})}{\sum_{i,j}t_{ij}^2+\sum_{i,j}p_{ij}^2-\sum_{i,j}(t_{ij} p_{ij})}$$

$t_{ij}$和$p_{ij}$分别表示像素点(i,j)的目标和预测输出，实验结果表明，与传统的交叉熵损失函数相比，该损失函数具有更强的鲁棒性。另外，它非常适合前景和背景的不平衡类。
 