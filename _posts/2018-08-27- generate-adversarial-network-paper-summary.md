---
layout: post
title: "生成式对抗网络论文阅读整理"
categories: 
- 论文
- 深度学习
tags: 
- GAN网络家族
author: Dimension
---

转自[haoji007](https://blog.csdn.net/haoji007/article/details/80392454)，对目前GAN经典的及最新的较有影响力的论文进行了阅读与整理，目前仅完成了论文梗概的总结。后续将会分篇详细介绍。

<style>
table
{
    font-family:serif;
}
th
{
    background-color:#bdc3c7;
}
td,th
{
	text-align:center;
}
.report{
    width:10%;
}
</style>

<table border="1">
<tr>
<th>归类</th>
<th width="20%">题目</th>
<th class="report">发表</th>
<th>贡献摘要</th>
</tr>

<tr>
<td rowspan="6" bgcolor="#9cd3d3">理论</td>
<td>Generative Adversarial Nets(Ian Goodfellow, Yoshua Bengio)</td>
<td>NIPS2014</td>
<td>发明GAN，生成器与判别器是较简单的多层感知机，对比了RBM、MCMC、DBN、CAE、GSN等工作，给出经典的二元的优化目标，训练过程的图解及算法流程（训练k次D后更新G，随机梯度下降法优化），证明了唯一最优解的存在，说明了最优解时分布的情况，在MNIST、TFD、CIFAR-10上展示了生成图像</td>
</tr>

<tr>
<td>Wasserstein Generative Adversarial Networks（Martin Arjovsky, Soumith Chintala, Leon Bottou）</td>
<td>ICML2017</td>
<td>解决原始GAN训练困难、loss函数无法指示训练过程、生成样本缺乏多样性的问题。分析了原GAN中度量分布远近的距离指标：KL散度和JS散度的缺点——训练过程中出现梯度为零无法学习的情况。引出Wasserstein解决以上问题。将该距离引入训练过程，同时为了求解推导出其对偶问题，以Lipschitz限制其最大局部浮动程度（直观上试图使得输入的样本稍微变化后，判别器给出的分数不能发生太过剧烈的变化，实现时仅仅通过限制各参数的变动范围）。由于拟合的是Wasserstein距离，故去掉最后的sigmoid是问题变为回归问题。（中山大学郑华滨分析）</td>
</tr>

<tr>
<td>Improved Training of Wasserstein GANs(Martin Arjovsky)</td>
<td>ArXiv2017</td>
<td>WGAN虽然理论分析完美，但是训练时发现训在不收敛的情况。WGAN的一作认为关键在于原设计中Lipschitz限制的施加方式不对，使得判别器非常倾向于学习一个简单的映射函数。其在新论文中提出了相应的改进方案：使用梯度惩罚的方法，加入新的loss项使梯度越接近Lipschitz常数K越好，在采样时也不需要整个空间上采，而是抓住生成样本与真实样本集中的区域进行采样求取loss。</td>
</tr>

<tr>
<td>Towards Principled Methods for Training Generative Adversarial Networks</td>
<td>ICLR2017</td>
<td>是WGAN的前作，详细分析了GAN存在的问题，最后提出解决方案。其分析了以下几个问题：为何D越好则更新过程越糟糕（D过好则难以学出正确的梯度信息）；为何GAN的训练非常不稳定（因为G和D的loss优化目标是相反的）；梯度消失问题（两个分布很难有交集，原来的loss函数算出的loss为常数，本文给出一种解决方法是1加入噪声使两分布拉近，2使用Wasserstein距离这种连续性度量的距离）</td>
</tr>

<tr>

<td>Loss-Sensitive Generative Adversarial Networks on Lipschitz Densities（Guojun Qi，伊利诺伊大学）</td>
<td>ArXiv2017</td>
<td>与WGAN关系密切，均采用Lipschitz限制。由于GAN未对真实样本的分布做任何的限定，使得GAN模型具有无限的建模能力，也就导致了过拟合。LSGAN限制其无限建模能力，换成使用按需分配（集中力量优化生成的不好即距离真实样本较远的图像）的建模形式。其引入新的目标函数来实现这一能力。文章给出了LSGAN泛化能力的分析、与WGAN的对比，在第8章给出推广：CLSGAN使得可以利用类别标签来让GAN获得不同类别的生成能力（c设置为类别标签只是其模型的一个特例），文中还分析了在给定条件下的解的理论分析结果。</td>
</tr>

<tr>
<td>On Unifying Deep Generative Models（Zhiding Hu，CMU）</td>
<td>ArXiv2017</td>
<td>构建 GAN 和 VAE 深度生成建模方法之间的形式联系。首先对各自进行综述，对二者的各个步骤进行对比，认为其有着深刻的联系。然后提出二者的结合形式，如对抗变分自编码器。</td>
</tr>

<tr>
<td rowspan="4" bgcolor="#f6f3a7">改进</td>
<td>Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks</td>
<td>ArXiv2015</td>
<td>DCGAN，对原始GAN的第一个重要改进。为生成器与判别器引入深度模型，在generator和discriminator上都使用batch normalization，无理论创新，均为深度模型训练时的改进。</td>
</tr>

<tr>
<td>InfoGAN: Interpretable Representation Learning by Information Maximizing Generative Adversarial Nets（Xi Chen）</td>
<td>NIPS2016</td>
<td>条件GAN，使得输入向量的每个值都有各自对应的含义（可解释性），如控制生成的类别、控制生成人物的发色等。方法是最大化输入的随机向量+条件向量与输出分布之间的互信息，使得输入的条件信息与输出的相关性变大。其在D中给出各个类的概率，然后在loss中也添加相应的loss项（Ls+Lc）。最后展示的结果也是按照各个类别产生的新图像，在MNIST、3D人脸与3D椅子等数据集上给出了生成图像的展示。</td>
</tr>

<tr>
<td>Improved Techniques for Training GANs（Tim Salimans，Goodfellow，Xi Chen）</td>
<td>ArXiv2017</td>
<td>提出了训练GAN时的几种技巧，主要是一种新的BN方法（原来的BN能够提高网络的收敛，但是问题是layer的输出和本次batch内的其他输入相关）：首先从训练集中拿出一个batch在训练开始前固定起来，算出这个特定batch的均值和方差，进行更新训练中的其他batch。再就是特征匹配，提出以中间特征作为衡量标准，而不是预测的标签。在MNIST、CIFAR-10、SVHN上得到了目前最好的结果。</td>
</tr>

<tr>
<td>Adversarial Feature Learning</td>
<td>ICLR2017</td>
<td></td>
</tr>

<tr>
<td rowspan="4" bgcolor="#ff6473">与各领域的结合</td>
<td>Unsupervised and Semi-Supervised Learning with Categorical Generative Adversarial Networks</td>
<td>ICLR2016</td>
<td>从未标记或部分标记的样本中学习判别分类器。在观测样本和他们预测的类别分布间trades-off互信息，对生成式聚类、判别式聚类等进行了综述，通过指派一个标签y给每个样本，将数据分类到K个类别中去的分类器，而不是学习一个二分类函数，将问题由“生成器生成属于数据集的样本”变为“生成属于K个中的一个确切的类别的样本”。在其方法中，会先定性地评估对抗生成器生成的样本的保真度，然后确定CatGAN目标和判别聚类算法(RIM)之间的联系</td>
</tr>

<tr>
<td>Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network</td>
<td>CVPR2017</td>
<td>将生成式对抗网络（GAN)用于SR问题（引入D来解决不同数据域之间分布不一致的问题），使用GAN生成图像中的细节。传统的方法使用的代价函数一般是最小均方差（MSE），即各个像素之间的差值，但这样做会使得生成的图像过于平滑。本文的目标函数第一部分是基于内容的代价函数，第二部分是基于对抗学习的代价函数。基于内容的代价函数除了传统的像素空间的最小均方差以外，又包含了一个基于特征空间的最小均方差。</td>
</tr>

<tr>
<td>Semantic Segmentation using Adversarial Networks（FAIR， Soumith Chintala-WGAN二作）</td>
<td>NIPS2016</td>
<td></td>
</tr>

<tr>
<td>Generative Adversarial Text to Image Synthesis</td>
<td>ICML2016</td>
<td></td>
</tr>

</table>

