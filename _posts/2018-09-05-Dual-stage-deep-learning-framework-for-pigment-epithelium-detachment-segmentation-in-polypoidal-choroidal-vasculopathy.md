---
layout: post
title: "Dual-stage deep learning framework for pigment epithelium detachment segmentation in polypoidal choroidal vasculopathy"
background: grey #white grey deepgrey blue purple green yellow red orange
background-image: http://img4.duitang.com/uploads/item/201509/26/20150926104627_4xrcE.thumb.700_0.jpeg
categories:
- 论文
- 深度学习
tags:
- 图像分割
- OCT
author: Dimension
description: 这篇论文利用了两个阶段来对PED分割，第一阶段确定BM层，第二阶段对PED分割
mermaid: true
date: 2018-09-05 20:53:04
ico: note #book game note chat code image web link design lock
---

>首先传送门--------------->[论文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5611923/pdf/boe-8-9-4061.pdf)

## 简介
息肉状脉络膜血管病变（polypoidal choroidal vasculopathy(pcv)）是一种具有威胁性的渗透性黄斑病，视网膜色素上皮脱离(pigment epithelium detachment (PED))是其常见的症状，表现在视网膜色素上皮(RPE)下的渗漏和出血，由于PED volume可以预测PCV疾病的治疗效果，因此在临床实践中需要精确可靠的PED分割进行测量；因此精确有效的PED分割在PCV诊断和治疗中至关重要。

一般的，PED可以分为3类：serous,vascularized 和 drusenoid PEDs。Serous PED是由于在sub-PER空间中液体聚集造成的；Vascularized PED,这是血管增生或者sub-PER血管增生的结果，相比于其它类型的PED，这种对视力具有更大的威胁，但是也更容易治疗；Drusenoid PED 主要是由脉络膜玻璃膜疣引起的，因此不常见。目前用计算机辅助诊断系统主要三个挑战：

1. 形态扭曲限制了之前只是的使用
2. 不期望的斑点和不期望的畸形会影响到边界描绘的精确度
3. serous 和 vascularized PED之间的灰度不均影响了分割精确度

如下图，serous PED是在PRE层下面出现的拱形区域，而vascularized PED在RPE层下具有非均质标志，具有高反射性血管病变和低反射性管腔。因此，邻近组织的同质性以及PED内部的异质性给PCV患者带血管蒂的PED的自动分割带来了困难。

![这里是图片](/wsc12358.github.io/assets/images/2018-9-5/1.png)

论文中介绍了几个传统的(非深度学习)的方法，然而，对于图像质量和灰度变化都有很大的敏感性。针对OCT图像，提出了一种基于图搜索的DNN分割模型。Roy等人提出了一种RelayNet的网络分割视网膜层和流体。这篇论文提出了一种基于DNN的框架对PED进行分割。是一种双阶段的DNN的学习。首先通过DNN对图像中BM层进行学习，接着我们使用得到的BM层作为参考来辅助另一个DNN来对PED区域进行分割。虽然单级网络不能解决不同类型的OCT成像问题，但我们的框架关注不同阶段的不同问题，因此我们的框架比单级网络表现更好。

本文提出了一种利用DNN的双阶段学习框架，对患有PCV的病人的PED进行分割，从而减少了手动分割带来的问题(专家的主观性，手动分割误差以及耗时)。采用不同的算法和临床医师对50例患者的光学相干断层扫描进行定量评价。双阶段DNN在所有分割精度参数（包括true positive volume fraction (85.74 ± 8.69%), dice similarity coefficient (85.69 ± 8.08%), positive predictive value (86.02 ± 8.99%) and false positive volume fraction (0.38 ± 0.18%).）上均优于已有的PED分割方法。双阶段DNN实现了精确的PED定量信息，可与多种类型的PEDs协同工作，并与人工描绘吻合良好，说明它是PCV管理的潜在自动助手。

## 方法
### 1 双阶段PED分割框架
给一个去噪后的图像$\hat{I}$,我们使用CNN来获取特征并利用这些特征来区分PED区域，分割PED的方法是双阶段，我们构造了两个DNN网络（S1-Net和S2-Net）,FCN作为S1-Net和S2-Net的结构(见表1)，它是一种现成的强大的CNN模型，用于提取面向PED的整体图像特征，以学习端到端PED分割。在FCN之后，由于FCN的5个池化层使得feature map的子采样分辨率为32，我们将filter size设为64,stride设为32，以确保得到的分割图的分辨率与输入图像一致。在我们的双阶段学习方案中，经过归一化和去噪处理后，我们首先通过S1-Net模型从图像中捕获BM层，然后使用识别后的BM层作为约束，通过S2-Net模型进行PED识别和描绘。框架结构如下：
![这里是图片](/wsc12358.github.io/assets/images/2018-9-5/2.png)

![这里是图片](/wsc12358.github.io/assets/images/2018-9-5/3.png)

#### 1.1 预处理
原始图像为512 × 496,在网络中，对图像进行调整处理，使其大小为384 384像素，在框架输出最终结果时，采用双线性插值的方法将图像恢复到原来的分辨率，得到最终结果。虽然我们使用的DNN结构(FCN)可以采用任何分辨率的图像，但是我们对输入大小进行了规范化，以提高框架的效率。根据这些分割方法的实验结果，输入大小的规范化对性能影响不大。如下图(a)所示，由于OCT机器或其他噪声源的信号传输，实际临床应用中OCT图像通常包含意想不到的斑点和图案。为了减少这种成像噪声的影响，采用基于概率的非局部均值滤波器，该滤波器与其他最先进的散斑去除技术相竞争，能够精确地保留边缘和结构细节，并且对OCT图像的去噪过程具有较小的计算成本，从而对原始图像进行去噪。

#### 1.2 BM层识别学习
为了能够识别BM层，我们将去噪的图像$\hat{I}$输入给S1-Net。卷积层和池化层序列的输出是高度卷积的数据，可以代表I的内在信息和语义信息。然后，将得到的高卷积数据传递到反卷积层(表1中S1-Net的最后一层)，即卷积的转置对卷积数据进行上采样。该学习需要每个训练图像对应的BM层的ground truth。在BM层下面的区域中，在ground truth上填充前景像素，使正负样本相对平衡。我们利用填充的ground truth训练S1-Net。如图(c)和(d)所示，与基于线的ground truth训练相比，通过该训练可以得到更紧凑、更精确的BM层。因此，我们可以得到概率图R(如图(d)所示)，与$\hat{I}$分辨率相同。我们使用R作为BM图层的识别结果。

#### 1.3 PED描边
在PED描边阶段，我们使用第一阶段得到的R来辅助S2-Net对PED描边。灰度图$\hat{I}$被转换为一个RGB图G。如图(e)所示，在G中，被识别的BM层出现了红线。我们将G输入S2-Net，并将其与PED区域的ground truth进行训练。因此，在S1-Net中，输入数据的大小和第一个滤波器组是不同的。由于BM层是施加在S2-Net的输入数据上，这个约束依次且固有地附加到面向PED区域的feature map上。我们把S2-Net的输出作为分割映射，然后采用0.5的阈值来描绘PED轮廓(如图(f)所示)。

![这里是图片](/wsc12358.github.io/assets/images/2018-9-5/4.png)

### 2 框架设定
我们用MatConvNet实现了框架。epochs为50，batch size为20，learning rate为0.0001。我们的实验遵循十倍交叉验证协议，每个验证过程包含45个病人扫描作为训练集，5个扫描作为验证集。

### 3 DNN与框架优化
框架的主要结构是FCN,当数据$X\in{\mathbb{R}^{m×h×d}}$经过卷积层，卷积组$\{F_{1},F_{2},...,F_{d^{'}}\}$将生成$d^{'}$维的特征图，在训练阶段，这些卷积和偏置将会更新，从而使生成的特征图更具有区分PED的能力。池化层通常在卷积层之后，给特征图降维。这些过程获得的特征对输入移位和失真不太敏感。在实践中，输入数据通常会传递到一组卷积层和池化层中，这样所提取的特征图比低级手工得到的特征更具有内在性和语义性。提取特征图后，嵌入的反卷积层将得到与输入图像分辨率相同的分割概率图。反卷积的转置定义为:

$$
Y_{i^{''}j^{''}d^{''}}=\sum_{d^{'}=1}^{D}\sum_{i^{'}=1}^{\varphi(H^{'},r)}\sum_{j^{'}=1}^{\varphi(W^{'},r)}F_{1+ri^{'}+\phi(i^{''}+z,r),1+rj^{'}+\phi(j^{''}+z,r),d^{''},d^{'}}×X_{1-i^{'}\varphi(i^{''}+z,r),1-j^{'}\varphi(j^{''}+z,r),d^{'}}
$$

其中$F\in{\mathbb{R}^{H^{'}×W^{'}×D×D^{'}}}$是反卷积权重，X和Y分别是反卷积的输入和输出，z是反卷积padding大小，r是卷积步长，$\phi(a,b)=(a-1)mod b$,$\varphi(a,b)=\frac{a-1}{b}$。
损失函数定义为：

$$
L=\sum_{x\in{S}}(-x^{c}+log\sum_{t=1}^{2}e^{x^{t}})+\lambda||W||^2
$$

其中，S是训练图像像素集合，$x^t$是位置x第t通道反卷积输出，c是x的label，$\lambda$是权重W的衰减正则化，通常设为0.0005。

### 7 优化指标
我们这里用到的优化指标有true positive volume fraction (TPVF), dice similarity coefficient (DSC), positive predictive value (PPV) 和 false positive volume fraction (FPVF)，其定义如下：

$$
TPVF=\frac{|V_{R}\bigcap{V_G}|}{|V_G|}
$$

$$
DSC=2×{\frac{|V_R\bigcap{V_G}|}{|V_R\bigcup{V_G}|}}
$$

$$
PPV=\frac{|V_R\bigcap{V_G}|}{|V_R|}
$$

$$
FPVF=\frac{|V_R|-|V_R\bigcap{V_G}|}{|V_{\varepsilon}-V_G|}
$$

其中，$\vert{V_R}\vert$, $\vert{V_G}\vert$, $\vert{V_{\varepsilon}}\vert$ 分别是BM和ILM之间的segmentation results, ground truth 和 retina volume,
