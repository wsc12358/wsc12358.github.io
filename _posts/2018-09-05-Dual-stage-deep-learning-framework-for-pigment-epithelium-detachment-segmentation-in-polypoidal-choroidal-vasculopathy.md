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