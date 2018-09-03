---
layout: post
title: "Adversarial synthesis learning enable segmentation without target modality ground truth"
background: green
background-image: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535557944784&di=944fc47ad1afd3552c6d117ea37e5fdc&imgtype=0&src=http%3A%2F%2Fattimg.dospy.com%2Fimg%2Fday_121031%2F20121031_80c2817861d48198af2dRy888Dz8Fr8E.png
categories: 
- 论文
- 深度学习
tags: 
- 图像分割
author: Dimension
description: 无需使用CT的人工标签，即可实现不成对的MRI到CT图像的合成和CT脾肿大的分割
date: 2018-08-07 15:56:08
ico: note
---

# 简介
基于深度学习的分割有一个关键的限制：缺乏普遍性。通常，当用不同的成像方式分割器官或从不同的疾病组分割异常器官时，一个人会手工标注新的训练图像。如果一个人能够从一种模式(例如，MRI)中重用手工标签来训练一种新的模式(例如，CT)的分割网络，那么手动的努力就可以减轻。在此之前，已有两种阶段方法被提出用于使用循环生成对抗网络(CycleGAN)来合成目标模式的训练图像。然后，这些努力训练了一个独立使用合成图像的分割网络。然而，这两个独立的阶段并没有使用合成和分割之间的互补信息。因此，我们提出了一种新颖的端对端合成分割网络(EssNet)，无需使用CT的人工标签，即可实现不成对的MRI到CT图像的合成和CT脾肿大的分割。在这片论文中，EssNet通过不成对的MRI和CT扫描进行训练，只使用MRI扫描的手工标签。
# 数据
以不成对的60例全腹MRI T2w扫描和19例全腹CT脾肿大脾做为实验数据，每个MRI分别手工绘制6个标签(脾、左肾、右肾、肝、胃、体)，每次CT扫描手工绘制1个标签(脾)。采用75例正常脾脏全腹CT扫描，训练DCNN方法。
# 方法
EssNet网络结构如图2所示，这里A代表MR图像，B代表CT图像。两个生成器G1,G2是两个有9块ResNet组成的generator, G1将模态A的图像x转换为图像B($G_1(x)$),同时G2将模态B的图像y转换为图像A($G_2(y)$)。PatchGAN被用作两个对抗的discriminator(D1和D2)。D1用来分辨CT图像时真实的还是生成的，D2则用来判别MR图像。这里使用了两个训练途径(Path A和Path B)。这个循环的生成自网络基本上相似于CycleGAN.

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/5.png)

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/6.png)

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/7.png)

EssNet的主要目标是用来端到端的生成和分割，分割网络作为G1之后的一个额外向前的分支，被串联到Path A中。S的网络结构与G1完全相同，即：9块ResNet。
训练网络中用到了5个损失函数，两个adversarial损失如下：

$$L_{GAN}(G_1,D_1,A,B)=E_{y\thicksim{B}}[log(D_1(y))]+E_{x\thicksim{A}}[log(1-D_1(G_1(X)))]$$

$$L_{GAN}{G_2,B_2,B,A}=E_{x\thicksim{A}}[log(D_2(X))]+E_{y\thicksim{}B}[log(1-D_2(G_2(y)))]$$

两个 cycle consistency loss $L_{cycle}$用来比较重构图像和真实图像。

$$L_{cycle}(G_1,G_2,A)=E_{x\thicksim{A}}[||G_2(G_1(x))-x||_1]$$

$$L_{cycle}(G_2,G_1,A)=E_{x\thicksim{B}}[||G_1(G_2(y))-y||_1]$$

分割损失如下：

$$L_{seg}(S,G_1,A)=-\sum{_i}m_i\cdot{log(S(G_1(x_i)))}$$

m是图像x的手工标签，i是像素点索引。total loss定义如下：

$$
\begin{equation}
\begin{aligned}
&L_{total}= \lambda_1\cdot{L_{GAN}(G_1,D_1,A,B)}+\lambda_2\cdot{L_{GAN}(G_1,B_2,B,A)}+\lambda_3\cdot{L_{cycle}(G_1,G_2,A)}\\
&+\lambda_4\cdot{L_{cycle}(G_2,G_1,B)}+\lambda_5\cdot{L_{seg}(S,G_1,A)}
\end{aligned}
\end{equation} 
$$

在工作中，根据经验，$\lambda$的取值分别为$\lambda_1=1$,$\lambda_2=1$,$\lambda_3=10$,$\lambda_4=10$,$\lambda_5=1$，为了最小化$L_{total}$，这里使用了Adam优化器，通过path A和path B的重构图和分割图如图3所示。
在测试中，仅仅使用被训练的网络S，$B^{'}$代表测试CT图像，采用自动分割和手工分割的Dice相似系数(DSC)值作为评价不同分割方法性能的指标。所有统计显著性检验均采用Wilcoxon 秩检验(p<0.05)

