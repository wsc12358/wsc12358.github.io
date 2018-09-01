---
layout: post
title: "Generative adversarial networks to segment skin lesions"
background: red
background-image: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535557015986&di=837eab26e870f14933d4732293da9f60&imgtype=0&src=http%3A%2F%2Fimg.lenovomm.com%2Fs3%2Fimg%2Fapp-img-lestore%2F5048-2015-07-07014724-1436204844158.jpg%3FisCompress%3Dtrue%26width%3D320%26height%3D480%26quantity%3D1%26rotate%3Dtrue
categories: 
- 论文
- 深度学习
tags: 
- 图像分割
author: Dimension
description: 这篇论文主要针对皮肤病变图变化多样且大部分斑点位于图中心的特点，使用GAN进行分割
ico: note
---

# 简介
这是一篇用GAN进行皮肤病变图的分割论文，由于皮肤病变图具有很大的可变性，因此给分割带来挑战，这里提出的方法包括两个models:一个合成精确的皮肤病变分割mask的全卷积网络，和一个区分合成的和真实的分割mask的全卷积网络。在我们的工作中，给出了一个训练集，generator/segmentor尝试输出与ground truth匹配的合成图，同时discriminator/critic用来区分合成图和ground truth.
# 方法
我们的目标是从边缘分割skin lesions,在外观多样性上有独立性，并且没有手工的干预，我们将这里问题看作一个二值密度标记任务：给一个皮肤镜图片，我们旨在预测每一个像素点是'lesions'还是'background'。给一个现有的全卷积分割模型，即合成概率分割mask的segmentor，我们提出设计和清空一个带有单个输出点的DCNN，即critic，用来区别合成分割mask和真实的ground truth。

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/3.png)

## 1 segmentor
这里我们用UNet作为segmentor，用 $I_{rgb}\in{\textbf{I}}$ 表示输入图像，用$\tau\in{T}$表示ground truth mask,$M\in{\textbf{M}}$表示合成分割mask,分割mask中每一个像素点$i$ $M=\{m_i,i=1,,,,,N\}$取值范围为$L=[0,1]$,并且每一个像素点$\tau=\{t_i,i=1,,,N\}$取值范围为{0,1}，给出输入图像$I_{rgb}$和学习参数$\theta_s$,则标签分配$M$的条件概率为：

$$p(m|I_{rgb}:\theta_s)=\sigma(\psi_{\theta_s}(I_{rgb}))$$

这里$\sigma(\cdot)$是用在分割网络输出层$\psi_{\theta_s}(\cdot)$的激活函数sigmoid,我们使用二值交叉熵损失函数：

$$L_{\theta_s}=-\frac{1}{N}\sum_{i=1}^{N}[t_ilog(m_i)+(1-t_i)log(1-m_i)]$$

$t_i$和$m_i$分表表示预测的和真实标签的像素点。
## 2 critic
我们扩展一个DCNN作为判别网络，其接受一个皮肤镜图片和或者一个合成图或者一个真实的病变分割mask作为输入，并尝试区分这两个。特别的，合成图或者真实的病变分割图被连接到RGB通道中，并被分配为1（指真实的图）或者0（指合成图），新的4通道图输入给critic，最后一个单输出点预测真实的二值标签，critic网络包括6个3x3卷积层，3个最大池化层和3个线性层，并且都使用ReLu激活函数，除了最后一层使用sigmoid函数，每一个卷积操作后面都使用了batch normalization.

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/4.png)

综上所述，让$I_{rgb}\in{\textbf{I}}$作为输入图并且$S\in\{M,\tau\}$是合成图和真实分割mask，在输入连接的$(I_{rgb} ,S)$后，将得到一个标签值$L=\{0,1\}$,一旦输入，label分配y的条件概率为：

$$p(y|I_{rgb},S;\theta_c)=\sigma(\psi_{\theta_c}(I_{rgb},S))$$

$\theta_c$表示critic网络的参数，并且$\psi_{\theta_c}$代表critic网络的输出，跟分割网络相似，这里我们使用二值交叉熵作为损失训练critic网络，定义为$L_{\theta_c}$。
## 3 训练
critic网络的误差会反响传播给segmentor进行训练。因此，更新segmentor的最终损失函数为：

$$L_{final}=L_{\theta_s}+ \lambda{L_{\theta_c}}$$

这里的$\lambda=0.2$是用来平衡critic网络误差的系数。