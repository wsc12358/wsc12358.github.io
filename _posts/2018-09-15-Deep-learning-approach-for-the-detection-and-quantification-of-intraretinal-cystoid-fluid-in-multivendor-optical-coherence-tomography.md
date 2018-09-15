---
layout: post
title: "Deep learning approach for the detection and quantification of intraretinal cystoid fluid in multivendor optical coherence tomography"
background: grey #white grey deepgrey blue purple green yellow red orange
background-image: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1537621174&di=a0cfa523bb26e6e3f9529b829cc54f0c&imgtype=jpg&er=1&src=http%3A%2F%2Fimg5q.duitang.com%2Fuploads%2Fitem%2F201504%2F29%2F20150429093823_5jv3K.thumb.700_0.jpeg
categories:
- 论文
- 深度学习
tags:
- 图像分割
- OCT
author: Dimension
description: 这是一篇关于IRC的分割，AMD是一种常见的疾病，而流体积聚是最明显的特征，通过检测流体的变化可以有效诊断。本片主要对视网膜内囊状流体进行分割，分为两个阶段，先分割出视网膜，然后在分割IRC。
mermaid: true
date: 2018-09-15 12:58:35
ico: note #book game note chat code image web link design lock
---

* 目录   
{:toc #markdown-toc}

>首先传送门 [论文](https://www.osapublishing.org/DirectPDFAccess/A5496432-FB20-B17F-21EFB7C0D1C5D190_383190/boe-9-4-1545.pdf?da=1&id=383190&seq=0&mobile=no)

## 简介
我们开发了一种深度学习算法，用于在光谱域光学相干层析成像(SD-OCT)卷中自动分割和量化视网膜内囊状液(IRC)。之前也提出了一些用视网膜解剖的先验信息的方法，确实提高了性能。对于IRC的分割和量化任务，该算法接近人的性能，总体Dice系数为0.754±0.136，类内相关系数为0.936。该方法允许快速定量IRC体积测量，可用于改善患者护理，降低成本，并允许快速可靠的分析在大的人口研究。年龄相关的黄斑退化(AMD)是一种复杂的多因素视网膜疾病，其中基因和环境在疾病的发展中扮演者重要的角色。渗出性AMD常见的治疗方法是注射抗血管内皮生长因子(anti-VEGF)。这种治疗可以阻止引起血管液渗漏的视网膜内异常血管，血液，脂肪的生长。

![图片找不到了]({{ site.baseurl }}/assets/images/2018-9-15/1.png)

anti-VEGF治疗通常每月进行一段时间，对患者造成高负担，但并不总能改善视力。此外，anti-VEGF治疗费用昂贵，每月一次的治疗也会给医疗系统带来巨大的财政负担。然后提出了另外两种治疗方法，PRN和TE。当视网膜出血或积液再次发生时才进行再治疗，然而，为了提供个性化的护理和减少不必要的注射，这些方案需要持续评估液体的存在及其随时间的变化。流体积累在光谱域光学相干层析成像(SD-OCT)成像中表现最好，这是评价AMD治疗成功与否不可或缺的工具。SD-OCT成像提供了一种无创性，高分辨率，三维可视化的视网膜，其中流体是一个可见的反射区。然后介绍了很多以前的分割方法，但都是运行在但设备获得的SD-OCT卷上，流体积累在光谱域光学相干层析成像(SD-OCT)成像中表现最好，这是评价AMD治疗成功与否不可或缺的工具。SD-OCT成像提供了一种无创性，高分辨率，三维可视化的视网膜，其中流体是一个可见的反射区。
本文提出了一种深度学习算法，用于对不同SD-OCT设备获得的SD-OCT卷中的IRC进行检测、分割和量化。该算法基于完全卷积神经网络(FCNN)，通过对SD-OCT卷进行语义分割来分割IRC，即，分析SD-OCT体中的每个像素，并给出属于IRC的概率。提出的FCNN实现了一个多尺度的分析，提供了一个大的上下文窗口，允许精确的分割范围广泛的囊肿，从小的微囊肿到大的腹腔内囊肿跨越广泛的b扫描区域。提出的FCNN的大建模能力允许它学习广泛的不同复杂特性，能够捕获IRC外观的大变异性和供应商依赖的SD-OCT特征。通过在训练过程中加入视网膜分割的额外步骤来限制搜索空间，进一步提高了分割性能。算法性能在1)AMD晚期患者IRC的SD-OCT数据大私有数据库中进行评估;2)健康控制中心的数据集;3)一个公开的数据集，包含四个不同供应商的IRC提供的SD-OCT卷。

## 方法
### 1 数据
数据来自于 European Genetic Database (EUGENDA, [http://eugenda.org](http://eugenda.org))
数据集被随机分成三组，**训练集**由60名患者的103份SD-OCT (3131 b -scan)组成。**验证集**来自16名患者的19份SD-OCT测定值(540 b -scan)，**测试集**由75名患者的99份SD-OCT值(2487 b -scan)组成。
测试集的进一步分裂成三个子集,第一个测试集组成的53个SD-OCT卷(1480 B-scans)来自32个病人,第二个测试集组成的10个SD-OCT卷(324 B-scans)患者和33个SD-OCT组成的一套控制测试卷(683 B-scans)33健康对照组。

![图片找不到了]({{ site.baseurl }}/assets/images/2018-9-15/2.png)

在训练集IRC和全视网膜的全体积注释中，即，在视网膜色素上皮(RPE)的外边界与内边界之间的区域。注释由经验丰富的评分员使用计算机辅助注释平台进行，该平台允许手工进行像素级注释和校正。为了减少注释时间，使用半自动的方法进行注释。将初步分割算法生成的初始视网膜和IRC分割结果提交给评分者，如果系统提出的初始注释中存在错误，评分者将获得人工校正的工具。来自EUGENDA数据库的注释b扫描示例如图2所示。
IRC的第一个测试集注释是由评分员使用与训练集相同的计算机辅助注释平台进行的.
为了评估观察者之间的可变性，我们从第二个测试集中随机选择了包含IRC的50个b扫描进行注释。这50个b -scan由3个独立观察员注释，其中1个作为参考标准。在没有计算机辅助注释平台支持的情况下进行注释。
为了评估该算法对多个供应商的适用性，我们从一个公开可用的数据库(OPTIMA)中创建了一个外部集，该数据库包含40个SD-OCT卷，由4个不同的SD-OCT设备获得。
*  Heidelberg Spectralis HRA+OCT (Heidelberg Engineering, Heidelberg, Germany)
* Zeiss Cirrus (Carl Zeiss Meditec, Dublin, CA, USA)
* Topcon 3D 2000 (Topcon Medical Systems, Paramus, NJ, USA)
* Nidek RS3000 (Nidek, Aichi, Japan)

![图片找不到了]({{ site.baseurl }}/assets/images/2018-9-15/3.png)

图3显示了四个设备中每个设备的注释b扫描示例
这个外部数据集由15个SD-OCT卷的训练集和15个SD-OCT卷的测试集组成。除了Nidek之外，训练和测试子集每个供应商都包含4卷，其中有3卷。

![图片找不到了]({{ site.baseurl }}/assets/images/2018-9-15/4.png)

为外部数据集中的训练和测试集提供了两名独立观察员的手工像素级IRC注释。在这项研究中，我们使用了两个观察者的交点，即，其中两个观察者都同意存在IRC，作为训练算法的参考标准。

### 2 深度学习算法
这里提出的方法是在整个SD-OCT卷上进行检测，分割和量化的。在处理完一个卷中的所有b扫描后，将产生的分段合并成输出卷分割。这个算法由两个网络组成，第一个用于分割视网膜，第二个分割IRC。图4给出了整个处理机制。

#### 2.1 第一个任务，视网膜分割
在阈值化之后，第一步的输出是一个二进制图像，表示ILM和RPE之间的所有像素。图5(b)显示了这个任务的输出示例。进一步的网络细节在2.3节描述，2.4节介绍训练过程。

![图片找不到了]({{ site.baseurl }}/assets/images/2018-9-15/5.png)

#### 2.2 第二个任务，视网膜内囊状流体(IRC)分割
该FCNN使用两种不同的方法将上一步产生的输出集成在一起:1)作为额外的输入，2)作为网络训练过程的约束。对于第一种方法，附加输入，将由视网膜分割步骤产生的二值视网膜分割与输入b扫描叠加在一起，作为双通道输入提供给FCNN。这个添加允许网络学习位置特定的特性，可以提高分割性能。对于第二种方法，视网膜分割输出用于创建一个权重图，在训练期间给予视网膜内的位置更多的重要性，而忽略了视网膜外的区域，即脉络膜组织和玻璃体液。给定训练集B-scan Bi，其得到的视网膜分割Ri和作为参考标准的人工标注IRC Si(见图5)，对于$B_i$中位置x的权重图定义如下：
![图片找不到了]({{ site.baseurl }}/assets/images/2018-9-15/6.png)

其中在$B_i$ ，$N_{retina}$是除IRC的视网膜的像素点个数，$N_{IRC}$表示IRC的像素点个数，