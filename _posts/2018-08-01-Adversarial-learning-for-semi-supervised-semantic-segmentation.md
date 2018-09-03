---
layout: post
title:  "Adversarial learning for semi-supervised semantic segmentation"
background: green
background-image: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535556737605&di=92ca9e203bfa90ea61ebdaee1d33bcbd&imgtype=0&src=http%3A%2F%2Fbcs.91.com%2Frbpiczy%2Fsoft%2F2013%2F7%2F4%2F64d3f5cc874641c4b81871cc828ce259%2Fthumb_0025b65b68fc4479b8686c30429e9cfb_320x480.jpg
categories: 
- 论文
- 深度学习
tags: 
- 图像分割
author: Dimension
description: 主要使用了半监督的方式进行分割
date: 2018-08-01 20:20:32
ico: note
---

<font color="red">GAN生成对抗网络：</font>由两个子网络组成，generator和discriminator,在训练过程中，这两个子网络进行着最小最大值机制，generator用随机向量输出一个目标数据分布的样例，discriminator从目标样例中区分出生成器生成的样例。generator通过后向传播混淆discriminator，依此generator生成与目标样例相似的样例。

<font color="red">这篇论文中，</font>将generator换成一个分割网络(可以是任意形式的分割网络，如：FCN,DeepLab，DilatedNet……,输入是H\*W\*3,依次是长宽，通道数，输出概率图为H\*W\*C,其中C是语义种类数),这个网络对输入的图片分割输出一个概率图，使得输出的概率图尽可能的接近ground truth。其中discriminator采用了全卷积网络（输入为generator或ground truth得到的概率图，输出位空间概率图H\*W\*1,其中其中像素点p代表这个来自gournd truth(p=1)还是generator(p=0)。

[***代码***](https://github.com/hfslyc/AdvSemiSeg)

在**训练**中，用***半监督机制***，一部分是注解数据，一部分是无注解数据。
 **当用有注解数据时，**分割网络由基于ground truth的标准交叉熵损失和基于鉴别器的对抗损失共同监督。注意，训练discriminator只用标记数据。

**当用无注解数据时，**用半监督方法训练分割网络，在从分割网络中获取未标记图像的初始分割预测后，通过判别网络对分割预测进行传递，得到一个置信图。我们反过来将这个置信图作为监督信号，使用一个自学机制来训练带masked交叉熵损失的分割网络。置信图表示了预测分割的质量。

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/1.png)

### 对抗网络的半监督训练

输入图像$x_n$大小为H*W*3, 分割网络表示为$s(·)$,预测概率图为$s(x_n)$大小为H*W*C。全卷积discriminator表示为$D(·)$,其输入有两种形式：分割预测$s(x_n)$和one-hot编码的gournd truth  $Y_n$.
#### 训练discriminator网络：
  最小化空间交叉熵损失$L_D$,其表示为：

  $$L_D=-\sum_{h,w} (1-y_n)log(1-(s(x_n))^{(h,w)})+y_nlog(D(Y_n)^{(h,w)})$$

  当输入来自分割网络时$y_n=0$,若来自ground truth则为$y_n=1$.
  为了将ground truth转换为C通道的概率图，我们用one-hot机制进行编码，即如果像素$x_n^{(h,w)}$输入类C，则取1，否则为0.
#### 训练分割网络：
  这里使用的损失是多任务损失：

  $$L_{seg}=L_{ce}+λ_{adv}L_{adv}+λ_{semi}L_{semi}$$

  其中$L_{ce}$，$L_{adv}$和$L_{semi}$分别代表 multi-class cross entropy loss, the adversarial loss,和the semi-supervised loss，这里的$λ_{adv}$和$λ_{semi}$.
  这里先考虑用有注解的数据，则：

  $$L_{ce}=-\sum_{h,w}\sum_{c\epsilon{C}}Y_n^{(h,w,c)}log(s(x_n)^{(h,w,c)})$$

  $L_{adv}$表示为：

  $$L_{adv}=-\sum_{h,w}log(D(S(X_N))^{(h,w)})$$
  
#### 用无标签数据训练 
 由于没有ground truth,因此这里不能使用$L_{ce}$,这里提出了用自学机制在无注解数据中利用被训练的discriminator，大意是被训练的discriminator可以生成一个置信图,即$D(S(X_n))^{(h,w)}$,这个公式用来推断预测结构足够接近gournd truth的区域。这里用一个阈值来二值化置信图，$\hat{Y}=argmax(s(x_n))$,使用二值化置信图，半监督损失可以定义为：

 $$L_{semi}=-\sum_{h,w}\sum_{c\epsilon{C}}I(D(S(x_n))^{(h,w)}>T_{semi)}\bullet\hat{Y}_n^{(h,w,c)}log(s(x_n)^{(h,w,c)})$$
 
 其中$I(\bullet)$是指示函数，$T_{semi}$是阈值，注意在训练期间，自学目标值$\hat{Y}_n$和指示函数的值为常量，因此上式可以简单看做空间交叉熵损失。
