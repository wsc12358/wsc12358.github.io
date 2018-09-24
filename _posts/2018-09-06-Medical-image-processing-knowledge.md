---
layout: post
title: "医学图像处理小知识点总结"
background: green #white grey deepgrey blue purple green yellow red orange
background-image: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1536212647934&di=bee8493b6493b60e8e07d213c6791567&imgtype=0&src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201410%2F10%2F20141010002231_LW4Lc.thumb.700_0.jpeg
categories:
- 深度学习
tags:
- 医学图像处理
author: Dimension
description: 这里主要记录了医学图像处理中的小知识点，大多来自论文。
mermaid: true
date: 2018-09-06 10:53:52
ico: note #book game note chat code image web link design lock
---

## 图像处理(分割)网络优化指标
true positive volume fraction (TPVF)： 

$$
TPVF=\frac{|V_{R}\bigcap{V_G}|}{|V_G|}
$$

dice similarity coefficient (DSC)：

$$
DSC=2×{\frac{|V_R\bigcap{V_G}|}{|V_R\bigcup{V_G}|}}
$$

positive predictive value (PPV)：

$$
PPV=\frac{|V_R\bigcap{V_G}|}{|V_R|}
$$

false positive volume fraction (FPVF)，

$$
FPVF=\frac{|V_R|-|V_R\bigcap{V_G}|}{|V_{\varepsilon}-V_G|}
$$

其中，$\vert{V_R}\vert$, $\vert{V_G}\vert$, $\vert{V_{\varepsilon}}\vert$ 分别是segmentation results, ground truth 和 origin image。

![这里是图片](/wsc12358.github.io/assets/images/2018-09-06/1.png)

