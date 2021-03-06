---
layout: post
istop: true
background: purple
background-image: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535556683033&di=854c5dfb4a5b53e58a7ca39315305563&imgtype=0&src=http%3A%2F%2Fuploads.xuexila.com%2Fallimg%2F1706%2F28-1F622164P0.jpg
title:  "ubuntu深度学习环境的配置"
categories: 
- 深度学习
- Linux
tags: 
- 环境配置
author: Dimension
description: ubuntu16.04中配置深度学习环境的基础就是禁用nouveau原生显卡驱动，装NVIDIA显卡驱动，cuda和cudnn
date: 2018-07-29 15:32:45
ico: web
---
在ubuntu中配置GPU的深度学习环境相较于win问题要多很多，这几天琢磨了一下Ubuntu下的环境配置，参考很多人的博客，也遇到了不少坑，好不容易配置成功了，希望写下来，和大家分享，避免大家走弯路。环境的配置主要是nvidia显卡驱动的安装，在驱动安装的过程中遇到了问题，可以参考博客后面的<font color="red">问题解决方案</font>，主要步骤就是装nvidia驱动，然后是安装cuda和cudnn，这两个一般问题不大。配置成功后就可以根据需要安装自己使用的深度学习框架（比如目前比较火的tensorflow和pytorch）。这两个框架本人建议使用Anconda安装，一来方便安装，二来如果出错，可以直接删除anconda文件夹重新安装即可。
## 软件要求
		Ubuntu16.04
		Nvidia gtx 750 Ti
		Cuda 9.0
		Cudnn 7.0

## Nvidia显卡驱动的安装
### 1 禁用显卡驱动nouveau
网上很多文章说在官网下载run文件安装，这样安装的成功率较低，不建议这样做。还有在出现循环登录，黑屏时好多博客说卸载重装，这样也不大提倡，具体解决这些问题看博客后面的解决方案，亲测有效。由于nvidia的显卡驱动是闭源软件，因此ubuntu上默认是没有的，自带的显卡驱动叫做nouveau，安装之前要将nouveau先禁用掉，在终端里输入：
```bash
sudo vim /etc/modprobe.d/blacklist-nouveau.conf
```
在vim编辑器中输入以下两行：
```bash
blacklist nouveau
options nouveau modset=0
```
然后配置文件生效，终端中输入：
```bash
sudo update-initramfs –u
```
### 2. 接下来安装一些后面会用到的32位lib，终端中依次输入

```bash
sudo apt-get install lib32ncurses5
sudo apt-get install lib32z1 
```
然后重启，输入：
```bash
sudo reboot
```
### 3. 再次进入系统
同时按下Ctrl+Alt+F1进入tty模式，登录账号，输入用户名密码。然后关闭图形界面服务，输入：
```bash
sudo service lightdm stop
```
接下来添加nvidia驱动的ppa源并进行安装：
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
```
查看可安装的驱动版本，选择合适的版本安装，这里安装的384版本，
```bash
ubuntu-drivers devices
```
安装nvidia驱动及其依赖的包，
```bash
sudo apt-get update sudo apt-get install nvidia-384
sudo apt-get install mesa-common-dev
sudo apt-get install freeglut3-dev
```
打开图形界面：
```bash
sudo service lightdm start
```
<font color="red">禁用Secure boot的问题(非常非常重要！！！好多博客说在BIOS中禁用Secure boot,这样也可以，但会影响到win的启动，所以直接使用mok工具即可，如果这一步操作不成功，就九九归一了，滑稽)：</font>
```bash
sudo moktuil --disable-validation
```
<font color="#2e16b1">然后输入8-16位密码（这里最好用简单的密码，本人之前设置很复杂的密码，结果在后面的mok manager界面输入密码时经常出错，所以如：88888888这样的密码很容易成功)</font>
然后重启，输入：
```bash
sudo reboot
```
<font color="red">如果出现蓝色界面，选择改变secure boot状态的选项，进去提示输入对应位的密码（如:enter 2 characters:则输入密码的前两位），输入几遍后最后选择yes启动。</font>
打开终端，输入，nvidia-smi和nvidia-settings如果输出如下图，说明安装成功：

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/14.png)

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/15.png)

这时nvidia就安装好了，如果碰到黑屏，循环登录，参考后面的<font color="red">**问题解决方案**</font>。
## Cuda的安装
找到下载文件的路径
```bash
sudo sh cuda_9.0.176_384.81_linux.run
```
回车，一路往下运行，直到提示“是否为NVIDIA安装驱动nvidia-384？”，选择否，因为已经安装好驱动程序了，其他的全都是默认，安装位置默认是/usr/local/cuda，配置环境变量，运行如下命令打开profile文件
```bash
sudo sh cuda_9.0.176_384.81_linux.run
```
打开文件后在文件末尾添加路径，也就是安装目录，命令如下：
```bash
export  PATH=/usr/local/cuda-9.0/bin:$PATH
export  LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64$LD_LIBRARY_PATH　
```
保存，然后重启电脑
```bash
sudo reboot
```
测试CUDA的例子

```bash
cd  /usr/local/cuda-9.0/samples/1_Utilities/deviceQuery
sudo make
./deviceQuery
```

如果显示的是关于GPU的信息，则说明安装成功了。
最后你会看到cuda驱动、sample、tookit已经安装成功,但是缺少一些库。

环境变量配置
安装完毕后，再声明一下环境变量，并将其写入到 ~/.bashrc 的尾部:
```bash
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
exportLD_LIBRARY_PATH=/usr/local/cuda9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
然后设置环境变量和动态链接库，在命令行输入：
```bash
sudo gedit /etc/profile
```
在打开的文件末尾加入：
```bash
export PATH=/usr/local/cuda/bin:$PATH
```
保存之后，创建链接文件：
```bash
sudo gedit /etc/ld.so.conf.d/cuda.conf
```
在打开的文件中添加如下语句：
```bash
/usr/local/cuda/lib64
```
然后执行
```bash
sudo ldconfig
```
使链接立即生效

## cudnn的安装
1) 继续Ctrl+alt+F1进入的字符界面
2) 进入解压后的cudnn-9.0-linux-x64-v7.0.tgz文件cuda，在终端执行下面的指令安装：
```bash
tar -zxvf cudnn-9.0-linux-x64-v7.0.tgz
cd cuda    
sudo cp lib64/lib* /usr/local/cuda/lib64/    
sudo cp include/cudnn.h /usr/local/cuda/include/
```
然后更新网络连接：
```bash
cd /usr/local/cuda/lib64/  
sudo chmod +r libcudnn.so.7.0.3  # 自己查看.so的版本  
sudo ln -sf libcudnn.so.7.0.3. libcudnn.so.7  
sudo ln -sf libcudnn.so.7 libcudnn.so  
sudo ldconfig  
```
重新启动图形化界面
```bash
sudo service lightdm start
```
再Ctrl+alt+F7退出Text Mode

## 问题解决方案

在安装nvidia显卡驱动的过程中会遇到各种各样的问题，这里主要说明一下常见的3个问题：

<font color="red">问题1：</font> 安装Ubuntu的时候，卡在Ubuntu的LOGO界面或黑屏

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/16.png)

 <font color="red">问题2：</font>  双显卡安装Nvidia驱动，循环登录或黑屏

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/17.png)

<font color="red">问题3：</font>  启动后黑屏，并出现ubuntu the system is running in low-graphics mode 的错误

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/18.png)

<font color="green">针对以上3个问题，我们这里提出了相应的解决方案。</font>
<font color="d60062">注意！！！：对于问题1和问题2，如果下面对应的方法无效，则去掉"quiet splash"后面的apci_osi或者nomodeset,在vt_handoff后面添加acpi_osi或者nomodeset！！！</font>
<br>
<font color="red">方案1（针对问题1）：</font>
1.	启动系统后在Grub界面，选择ubuntu系统的那一行，然后按E键，就会进入Grub的编辑状态。

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/19.png)

2、在quiet splash 后面加（先打空格）nomodeset，然后按F10保存启动

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/20.png)

3、由于那个是临时改动，所以还需要一步，打开终端：
```bash
sudo vi /etc/default/grub
```

编辑打开的文件，找到GRUB_CMDLINE_LINUX_DEFAULT那一行，在后面加上(在quiet splash后打一个空格) nomodeset，保存，然后在终端输入 ：
```bash
sudo update-grub 
```

重启即可。

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/21.png)

<font color="red">方案2（针对问题2）：</font>
问题的根源是集显的问题（但由于我们是双系统或双显卡或着存在Grub启动项，导致没有解决到问题的根本！）
这一切的原因就是因为我们装系统的时候，加的那个参数nomodeset 接下来详细教程
1、	首先确定是否nvidia驱动已安装，按Ctrl+Alt+F1进入tty模式，登录，然后输入nvidia-smi如果输出显卡信息，说明安装成功了。
2、重新启动，在Grub界面选Ubuntu系统那一行然后按E键进入编辑模式：

![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/22.png)
 
3、也是上图那个位置，在 "quiet splash nomodeset",主要看是否有nomodeset，有的话删除它（可能有人是queit splash= nomodeset,删除'= nomodeset'即可！）
4、然后在原来那个位置加 acpi_osi=linux（代码之间用空格隔开！），然后按F10启动，就可以进入界面了。
5、最后一步，保存信息，打开终端：
```bash
sudo vi /etc/default/grub 或 sudo gedit /etc/default/grub
#打开文件后将nomodest删除替换为 acpi_osi=linux
#然后更新grub
sudo update-grub
```
![这里写图片描述]({{site.baseurl}}/assets/images/2018-8-27/23.png)

解释一下 Grub引导了系统进行启动，所以它的参数被传入了，即nomodeset（调用集显）如果存在，系统就会一直调用集显，然后就出现循环登录或黑屏。由于刚刚安装系统一般没有驱动，很多人只能通过调用集显去进入图形界面（除非在命令行下安装了驱动），导致了nomodeset参数的加入。
而acpi_osi=linux是告诉Grub，电脑将以Linux系统启动，调用其中驱动，所以可以用Nvidia的驱动进行显示了！
<font color="red">方案3（针对问题3）：</font>
当开机出现ubuntu the system is running in low-graphics mode错误时，按下Ctrl+Alt+F1,登录
输入：
```bash
cd /etc/X11
```
然后输入：
```bash
sudo cp xorg.conf.failsafe xorg.conf
```
重启：

```bash
sudo reboot
```

