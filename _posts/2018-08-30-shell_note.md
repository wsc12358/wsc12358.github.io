---
layout: post
title:  "shell教程"
background: blue
background-image: http://pic.58pic.com/58pic/14/43/52/37k58PIC72w_1024.png
categories: 
- Linux
tags: 
- shell
author: Dimension
description: 主要记录了shell最基础的语法以及简单的应用
mermaid: true
date: 2018-08-30 19:20:21
ico: book
---

* 目录   
{:toc #markdown-toc}

# 1 shell概述
shell最初是在UNIX系统中形成和发展的，UNIX中的shell有很多种，Linux继承了UNIX中shell的全部功能，现在默认使用的是bash。以下是Linux的系统结构。
![图片找不到了]({{ site.baseurl }}/assets/images/2018-8-30/2.png)
## 1.1 shell的特点和主要版本
### 1.1.1 shell的特点
1. 可以组合任意的命令组合成新的命令
2. 允许灵活的使用数据流，提供通配符，输入/输出重定向，管道线机制，方便模式匹配，I/O处理和数据传输。
3. 结构化程序模块
4. 提供后台执行的能力
5. 提供可配置环境，允许用户创建和修改命令，命令提示符和其他系统行为。
6. 提供一个高级命令语言，允许用户创建从简单到复杂的程序，这些称为shell脚本，利用shell脚本，可以把Linux命令组合起来，作为新的命令使用。

### 1.1.2 shell的种类
Linux提供多种不同的shell，常用的有Bourne shell(简称 sh)、C shell(简称 csh)、Korn shell(简称 ksh)和Bourne Again shell(简称 bash)
## 1.2 shell脚本的建立和执行
### 1.2.1 shell脚本的建立
shell脚本可以用任意的编辑器创建，例如vim,emacs等
### 1.2.2 shell脚本的执行
shell脚本的执行方式有3种。
1.输入重定向到shell脚本，让shell从给定文件中读入命令行，并进行相应处理，执行形式是：
```
bash<ex1
```
shell从ex1文件中读取命令并执行，当读到文件末尾时，终止执行，并把控制返回到shell命令状态，<font color="red">此时，脚本名后面不能带参数</font>
2.以脚本名作为bash参数执行
```
bash 脚本名 [参数]
```
例如：
```
bash ex2 /usr/meng /usr/zhang
```
其执行过程与1一样，<font color="red">好处是可带参</font>
如果以目前shell(以.表示)执行一个脚本，可以用如下简便方式
```
. 脚本名 [参数]
```
它以脚本名作为参数，这种方式可以用来程序调试
3.将shell脚本的权限设置为可执行，然后在提示符下执行
用`chmod`将脚本设置为有“执行”权限，例如
```
chmod a+x ex2
```
shell脚本ex2对所有用户都有了`执行`权限,然后再如下执行
```
./ex2
```
或者将脚本所在目录添加到命令搜索路径(PATH)中，例如：
```
$PATH=$PATH:.
```
把当前工作目录(以'.'表示)添加到命令搜索目录中，这样在命令提示符后输入脚本名ex2就可以执行该脚本：
```
ex2
```
# 2 命令历史
bash提供了命令历史功能，系统为每个用户维护了一个命令历史文件(~/.bash_history),查看历史命令可以在命令提示符后输入`history`即可
## 2.1 显示历史命令
如果history后面给出一个正整数，例如：
```
history 50
```
将显示命令历史表中最后50个命令
如果在history后给出一个文件名，例如
```
history al
```
那么，就把al作为历史文件名
## 2.2 执行历史命令
表1列出了基本事件字格式及意义，利用它们可以访问历史表中的命令行
表1 基本事件制定字格式及其意义

| 格式        | 意义   |
|!!|重新上一条命令，也就是"!-1"|
|!n|重新执行第n条历史命令|
|!-n|重新执行倒数第n条命令，如!-1就等于!!|
|!string|重新执行以string开头的最近的历史命令行，例如!ca表示访问钱满最近的cat命令|
|!?string?|重新执行最近的、其中包含字符串string的那条历史命令，例如，!?hist?表示重复前面的含有hist的命令|
|!#|到现在位置所有输入的整个命令行|

## 2.3 配置历史命令环境
默认方式下，bash用户的历史命令保存在用户主目录下的`.bash_history`文件中，但用户可以通过对环境变量`HISTFILE`赋值来改变存放历史命令的文件，例如：
```
$HISTFILE="/home/用户名/.myhistory"
```
默认情况下历史文件只能保存500条命令，超过限定值，最早的命令就会被删除，可以设置环境变量`HISTSIZE`来修改存放命令数
```
$HISTSIZE=600
```
# 3 命令补全
输入目录名或文件名的开头部分，按`Tab`键即可补全，如果输入过程中不知道后面的字符，而系统也无法确定唯一的名称时，可以先按`Esc`键，再按`?`键，系统将输出所有的可匹配字符
# 4 别名
## 4.1 定义别名
定义别名的格式如下：
```
alias [name=[value]]
```
如果没有参数，将在标准输出上显示别名清单，其格式为:`name=value`,其中，name是定义的别名名称，value是别名所代表的内容。
下面是一个定义别名的例子赋值号`=`左右不能有空格：
```
alias ll='ls -l'
```
## 4.2 取消别名
如果想取消别名，可使用如下命令：
```
unalias name...
```
执行后，就从别名表中删除由`name`制定的别名。例如：
```
unalias ll
```
再执行`ll`,将输出`ll: alias not found`
# 5 shell的特殊字符
shell中除使用普通字符外，还使用一些特殊字符，它们有特定的含义，如通配符`*`和`?`,管道线`|`,以及单引号，双引号等
## 5.1 通配符
### 5.1.1 一般通配符
通配符用于模式匹配，如文件名匹配，路径名搜索，字符串查找等。常用的通配符有4种。
1. `*`(星号)---匹配任意字符的0次或多次出现，例如，`f*`可以匹配`f,fa,f1,fa2,ffa.s`等，即匹配以`f`打头的任意字符串。但应注意，文件名前面的圆点`(.)`和路径名中的斜线`(/)`必须显式匹配，例如：模式`*file`不能匹配`.profile`，而`.*file`才可以匹配`.profile`。模式`/etc*.c`不能匹配在`/etc`目录下带有后缀`.c`的文件，而模式`/etc/*.c`会匹配这些文件。
2. `？`(问号)---匹配任意一个字符，例如`f?`可以匹配`f1,fa,fb`等，但不能匹配`f,fabc,f12`等。
3. [字符组]---匹配该字符组所限定的任意一个字符，例如：`f[abcd]`可以匹配`fa,fb,fc`和`fd`，但不能匹配`f1,fa1,fab`等，方括号的字符组可以由直接给出的字符组成，如上面所示，或由表示限定范围的起始字符、终止字符及中间一个连字符`(-)`组成。例如：`f[a-d]`与`f[abcd]`作用相同，又如`f[1-9]`与`f[123456789]`相同，但前者表示方式更简洁。<br>
应该注意，连字符仅在一对方括号中表示字符范围，如在方括号外就成为了普通字符了。但是，前面介绍的字符`*`和`?`在一对方括号外是通配符，若出现在方括号内，他们就失去通配符的能力，成为普通字符了，例如：模式`-a[*?]abc`只有一对方括号是通配符，因此他匹配的字符串只有`-a*abc`和`-a?abc`。
4. `!`(惊叹号)或者`^`---如果它紧跟在一对方括号的左方括号`([)`之后，表示不在一对方括号中所列出的字符。例如：`f[!1-9].c`表示以`f`的打头，后面一个字符不是数字`1~9`的`.c`文件名，它可以匹配`fa.c,fb.c,fm.c`等。
5. `{string1,string2}`匹配`string1`或`string2`(或更多)其一字符串，`a{abc,xyz,123}b` `a`与`b`之间只能是`abc, xyz, 123`其一
6. 特殊匹配：`[[:space:]]`:表示匹配空白字符，`[[:punct:]]`:表示匹配标点符号，`[[:digit:]]`:表示匹配数字，`[[:lower:]]`:表示匹配小写字母，`[[:upper:]]`:表示匹配大写字母，`[[:alpha:]]`:表示匹配字母，不区分大小写，`[[:alnum:]]`:表示匹配字母数字。

<font color="red">需要说明的是：通配符看起来有点象正则表达式语句，但是它与正则表达式不同的，不能相互混淆。把通配符理解为shell 特殊代号字符就可。而且涉及的只有，*,? [] ,{} 这几种。</font>
在一个正则表达式中，可以同事使用`*`和`?`。
例如，`/usr/meng/f?/*`匹配目录`/usr/meng`下，子目录名以`f`打头，后随一个任意字符的这些子目录下的所有文件名。
又如，`chapter[0-9]*`表示`chapter`之后紧跟着零个或多个`0~9`的数字，它可匹配`chapter,chapter0,chapter1,chapter29,chapter123`等。
### 5.1.2 模式表达式
模式表达式是那些包含一个或多个通配符的字。`bash`除支持`Bourne shell`中的`*`,`.`,`?`和`[...]`通配符外，还提供特有的扩展模式匹配表达式，下面介绍其形式和含义。
1. `*`(模式表)---匹配给定模式表中0次或多次出现的`模式`，各模式之间以`|`分开，例如：`file*(.c|.o)`将匹配文件`file, file.c, file.o, file.c.c, file.o.o, file.c.o, file.o.c`等，但不可以匹配`file.h`或`file.s`等。
2. `+`(模式表)---匹配给定模式表中一次或多次出现的`模式`，各模式之间以`|`分开。例如：`file+(.c|.o)`匹配文件`file.c, file.o, file.c.o, file.c.c`等，但不可以匹配`file。`
3. `？`(模式表)---匹配模式表中任意一种0次或1次出现的`模式`，各模式之间以`|`分开，例如，`file?(.c|.o)`只匹配`file, file.c`和`file.o`,它不匹配多个模式或模式的重复出现，即不匹配`file.c.c, file.c.o`等。
4. `@`(模式表)---仅匹配模式表中给定一次出现的`模式`，各模式之间以`|`分开，例如：`file@(.c|.o)`匹配`file.c`和`file.o`,但不匹配`file, file.c.c, file.c.o`等。
5. `!`(模式表)---除给定模式表中的一个`模式`外，它可以匹配其他任何东西。

可以看出，模式表达式的意义是递归的，每个表达式中都可以包含一个或多个模式，如`file*(.[cho]|.sh)`是合法的模式表达式。<font color='red'>但在使用是应注意，由于带<font color="#000">*</font>和<font color="#000">+</font>的表达式可以匹配给定的组合，若利用此种表达式来删除文件存在危险，有可能将系统配置文件删除。因此，必须小心使用。</font>

## 5.2 引号
在shell中引号分为三种：单引号、双引号和倒引号。
### 5.2.1 双引号
由双引号括起来的字符(除`$`、倒引号\`和反斜线(`\`))均作为普通字符对待。这是三个字符仍保留其特殊功能：`$`代表变量替换，即用预先指定的变量值代替`$`和变量，倒引号\`表示命令替换，反斜线`\`仅当气候的字符是`$`,\`,`"`或者换行符之一时，`\`才是转义字符。转义字符告诉`shell`,不要对其后面的那个字符进行特殊处理，只是当做普通字符。
例如： 双引号的作用示例
```
cat ex3
    echo "current directory is `pwd`"
    echo "home directory is $HOME"
    echo "file*.?"
    echo "directory '$HOME'"
ex3
    current directory is /home/mengqc/prog
    home directory is /home/mengqc
    file*.?
    directory '/home/mengqc'
```
由脚本ex3看出，第一个`echo`语句中，在双引号括起来的字符串中包含'pwd'(此处到引号)。执行该语句时，先执行倒引号括起来的`pwd`,并将结果代替’pwd‘(此处倒引号)。从而得到输出结果的第一行。<br>
第二个`echo`中，双引号中`$HOME`,执行时先以`HOME`环境变量的值替代`$HOME`,然后显示整个参数字符串。<br>
第三个`echo`语句中，双引号中的字符都作为普通字符出现，所以执行结果如第三行所示。
第四个`echo`语句中，双引号有`‘$HOME’`，此时，单引号作为普通字符出现，而`$HOME`表示对`HOME`值的引用，因此结果如第四行所示。
### 5.2.2 单引号
单引号将引号内的所有字符都当做普通字符来呈现，例如：
```
str='echo "diretory is $HOME"'
echo $str
echo "diretory is $HOME"
```
其结果是把`“echo "diretory is $HOME"”`作为整体赋值给`str`，由于使用了单引号，`echo`和`$HOME`作为普通字符对待。
又如：
```
echo 'The time is `date`,the file is $HOME/abc'
The time is `date`,the files is $HOME/abc
```
### 5.2.3 倒引号
倒引号将引号内的内容当成命令来执行，在shell执行时，会先执行该命令行，并将它的标准输出结果取代倒引号部分，例如：
```
echo current diretory is `pwd`
current diretory is /home/wsc
```
利用这种功能可以进行命令置换，即把倒引号括起来的命令的执行结果赋值给指定变量，例如：
```
today=`date`
echo Today is $today
```
输出结果为：
```
Today is 2018年  08月  31日  星期五 18:34:28 CST
```
又如：
```
users=`who|wc -l`
echo The number of users is $users
The number os users is 5
```
可以看出，在命令置换时，倒引号中可以是单条命令或多条命令的组合，如管道线等。另外，倒引号可以嵌套使用。嵌套使用时，内层的倒引号必须反斜线`(\)`将其转义，例如：
```
Nuser=`echo The number of users is \`who|wc -l\``
echo $Nuser
the number of users is 5
```
如果内层倒引号不使用转义形式，而直接以原型出现在字符串中，成如下形式：
```
Nuser=`echo The number of users is `who|wc -l``
```
回车后，将出现
0
接着输入：
```
echo $Nuser
```
将显示一个空行。反斜线`(\)`是转义字符，它能把特殊字符当做普通字符。例如：
```
echo "Filename is \"$HOME\"$*"
```
则显示
```
Filename is "home/wsc"$*
```
如果想在字符串中使用反斜线`(\)`本身，可以采用`(\\)`的形式，<font color="red">应当注意，在单引号中，反斜线也成了普通字符，不能完成转义功能</font>
## 5.3 输入/输出重定向符
执行一个`shell`命令时，通常会打开3个文件：`标准输入文件(stdin)`、`标砖输出文件(stdout)`和`标准出错输出文件(stderr)`。它们分别对应`键盘`、`屏幕`、`屏幕终端`
### 5.3.1 输入重定向符号
输入重定向符`<`的作用是，把命令(或可执行文件)的标准输入重定向到制定文件，例如，在一个文件`cmds`中包含以下内容
```
cat cmds
echo "your working diretory is `pwd`"
echo "your name is `logname`"
echo "The time is `date`"
who
```
然后输入：
```
bash<cmds
```
shell命令解释程序从cmds中读取命令行并执行
输入重定向的一般形式是：
> 命令<文件名

### 5.3.2 输出重定向符
输出重定向符`>`的作用是，把命令(或可执行程序)的标准输出重新定向到指定文件中，例如：shell脚本exp1的内容如下：
```
echo "The time is `date`"
echo "Your name is `logname`"
echo "Working diretory is `pwd`"
echo "It has `ls -l|wc -l` files."
```
执行下列命令：
```
exp1>tmp1
```
屏幕上无任何信息
执行以下命令：
```
cat tmp1
The time is 2018年 08月 31日 星期五 20:11:11 CST
Your name is mengqc
Wording directory is /home/mengqc
It has 26 files
```
输出重定向的一般形式是
>命令>文件名

这里，文件名可以是普通文件或是对应与I/O设备的特别文件名，例如：
```
cat f1.c>/dev/lp0
```
将文件`f1.c`的内容在并行打印机上打印输出

### 5.3.3 输出附加定向符
输出附加定向符`>>`的作用是，把命令(或可执行程序)的输出附加到指定文件的后面，而该文件原有内容不被破坏，例如：
```
ps -l>>psfile
```
把`ps`命令的输出附加到文件`psfile`的结尾处。利用`cat`命令就可看到`psfile`的全部信息，包括原有内容和新添内容。<br>
使用输出附加定向符时，如果指定文件不存在，就创建一个新文件，输出附加定向符的一般形式是：
>命令>>文件名

### 5.3.4 即时文件定向符
即时文件(here document)有重新定向符`<<`、一对标记符以及若干输入行组成，它允许把shell程序的输入行重新定向到一个命令，即时文件的形式是：
>命令 [参数]<<标记符
>   输入行
>标记符

例如：
```
mail $1<<!!
Best wishes to you on your birthd_y.
!!
```
其中，标记符是`!!`，它要成对出现，`<<`之后的`!!`标记输入行开始，而最后的`!!`标记即时文件结束。标记符可以是别的能明显识别的符号。如`%`,甚至可以是用双引号括起来的字符串。如果没有用第二个标记符作为结束符，当遇到文件末尾，同样也可以结束即时文件。<br>
即时文件能使相应命令的输入重新定向，使它的输入取自两个标记符之间的若干输入行。如执行上面示例时，命令`mail`就把一对`!!`之间的输入行送给`$1`所对应的收信人。<br>
可见，预先把要处理的固定信息放入即时文件，有相应命令执行时立即读取，这种方式比边输入数据进行处理要方便的多。<br>
输入和输出重新定向可以连在一起使用。例如：
```
wc -l<infile>outfile
```
的功能是，命令`wc`从文件`infile`中输入信息，按`行`统计后的结果送到另一个文件`outfile`中，并不在屏幕上显示。
### 5.3.5 与文件描述字有关的重定向
在`UNIX/Linux`系统中，每一个`打开`的文件都有系统赋予的一个文件描述字，它是一个小整数。一个文件打开后，用户可以直接用这个描述子来引用对应的文件。如前所述，<font color="red">系统为每个进程自动打开三个标准文件(即校准输入、标准输出和错误输出)，其文件描述字分别是0,1,2。<color>
前面已经列举了标准输入和标准输出重新定向的例子。标准错误也可重定向倒一个文件中，其一般形式是：
>命令 2>文件名
>命令 2>>文件名

例如：
```
gcc m1.c 2>errfile
```
的作用是，对C语言源文件`m1.c`进行编译，将产生的错误信息重新定向倒文件`errfile`中，其中数字`2`表示标准错误输出的文件。**标准输出和标准错误输出可以冲定向到同一文件**。
>command $>file

其功能是，把命令`command`的标准输出和标准错误输出重定向到同一文件`file`中。
上述命令等价与下面的命令：
>command>file 2>& 1

其中，`2>& 1`表示把标准错误输出重定向到标准输出：
由于前面已把标准输出定向到`file`,所以标准错误输出也随之定向到`file`。从而可以看出，`shell`处理重新定向时是从左到右进行的。<br>
与重新定向有关的文件描述字是`0-9`,共`10`个文件描述字。用户自己可以随意定义并使用的文件描述字是`3-9`。例如，命令`cmd`原来要把输出放到文件描述字`9`对应的文件上，现在想把输出重定向到文件`f1`中，则可以使用下属形式：
>cmd 9>f1

上述输出的重新定向也可以推广到输入重定向。例如，`cmd 3<& 5`使两个文件描述字`3`和`5`都与同一个输入文件相关联，从而使命令`cmd`的输入源不止一个。
## 5.4 注释，管道线和后台命令
### 5.4.1 注释
`#`开头的正文行表示注释，如果`shell`脚本中第一行是以`#!`开头，则后面的字符串就是所使用`shell`的绝对路径
### 5.4.2 管道线
管道线是由`(|)`隔开的拖杆命令组成的序列，例如：
```
ls -l $HOME|wc -l
```
在管道线中，每个命令执行时都有一个独立的过程，***前一个命令的输出正是下一个命令的输入。从而管道县中有一类命令也称为“过滤器”，过滤器首先读取输入，然后将输入以某种简单方式进行变换（相当于过滤），再将处理结果输出，如`grep, tail, sort和wc`等命令就称为过滤器。*** <br>
一个管道线中可以包括多条命令，例如：
```
ls |grep m?.c|wc -l
```
显示当前目录中文件名以`m`打头，后随一个字符的所有`C`语言的数目。
### 5.4.3 后台命令
通常，在主提示符之后输入的命令都立即得到执行，在执行过程中，用户和系统可以发生交互作用---用户输入的数据，系统进行处理，并输出执行结果，这种工作方式就是前台方式。<br>
但是，可能有些程序的执行要花费较长时间，如果调用C编译器对C程序进行编译，如果想在编译的同事做别的事情，可以输入命令：
```
gcc m1.c&
```
即在一条命令的最后输入`&`符，告诉`shell`在后台启动该程序。而`shell`马上显示主提示符，提醒用户可以输入新的命令。
如果一个程序需要从终端输入数据，就不应该在后台启动该程序，以免发生前后太程序对终端访问的冲突。
利用前后台进程轮流在`CPU`上执行，可以提高工作效率，充分利用系统资源，通常规定，后台程序的调度优先级都低于前台进程优先级。
## 5.5 命令执行操作符
多条命令可以在一行中出现，它们可以顺序执行，也可能在相邻命令间存在逻辑关系
### 5.5.1 顺序执行
例如：
```
pwd
who|wc -l
cd /usr/bin
```
显然它们按顺序执行，可以写到一行，例如：
```
pwd; who|wc -l; cd /usr/bin
```
### 5.5.2 逻辑与
逻辑与操作符`&&`可把两个命令联系在一起，其一般形式如下：
>命令1&&命令2

如果`命令1`执行成功，才会执行`命令2`，否则，不执行`命令2`。
### 5.5.3 逻辑或
逻辑或操作符`||`可把两个命令联系起来，其一般形式是：
>命令1\|\|命令2

先执行`命令1`，若不成功，则执行`命令2`，否则，若`命令1`执行成功，则不执行`命令2`
## 5.6 成组命令
将若干命令组合在一起，在逻辑上看做一个命令，组合命令有两种方式，用花括号`{}`和用圆括号`()`将命令括起来
### 5.6.1 {}形式
用`{}`括起来的全部命令在语法上视为一条命令，出现管道线的一边，成组命令从左到右依次执行，在管道线中，成组命令把各命令的执行结果汇集到一起，形成一个输出流，这个流作为管道线的下一个命令的输入，例如：
```
{ echo "User Report for `date`.";who; }|pr
```
结果为
>2014-04-02   09:59               Page1<br>
>User Report for 2011年  04月  02日 星期六  09:59:26  CST<br>
>mengqc  :0    2011-04-02    09:27<br>
>mengqc  pts/0   2011-04-02   09:27<br>
>mengqc  pts/1   2011-04-02   09:27

从上例可见，`{}`中的`echo`和`who`命令的执行结果一起经“管道”攒给命令`pr`。
使用`{}`时在格式上注意，左括号`{`后面应有一个空格，有括号`}`之前应有一个分号`(;)`
`{}`也可以包含若干独占一行的命令，例如：
```
{ echo "Report of users for `date`."
echo
echo "There are `who|wc -l` users logged in."
echo
who:sort;}|pr
```
可见，`{}`中的命令表必须用分号或换行符终止。
### 5.6.2 ()形式
成组命令也可以用圆括号括起来。例如：
```
(echo "Current diretory is `pwd`."
 cd /home/mengqc;  ls -l;
 cp m1  em1&&rm m1
cat em1)|pr
```
如上所示，在`()`括起来成组命令时，左括号`(`后不必有空格，右括号`)`之前也不需要加分号。
这种形式的成组命令的执行过程与`{}`括起来的形式相同。
但是，二者存在重要的区别：用`{}`括起来的成组命令只是在`shell`内执行命令表，不产生新的进程；而用`()`括起来的成组命令是在新的子`shell`内执行，要建立新的进程，因此在`()`内的命令不会改变`shell`的变量值及工作目录等。

# 6 shell变量
`shell`变量是`边定义，边赋值`，`shell`变量有两种变量，`环境变量`和`临时变量`，环境变量是永久性变量，不会随shell脚本执行结束而消失，临时变量是在shell程序内部定义的，使用范围仅限于程序内部。
## 6.1 用户定义的变量
### 6.1.1 变量名
用户定义的变量，字母或下划线打头，由字母，数字和下划线组成的序列，大小写敏感。
### 6.1.2 变量赋值
定义变量并赋值的一般形式是：
>变量名=字符串

例如：
```
myfile=/usr/meng/ff/mc.c
```
### 6.1.3 引用变量值
程序中引用变量值时，在变量名前加上一个字符`$`符，它告诉`shell`，要进行变量值的替换。例如：
```
dir=/usr/meng/ff
echo $dir
```
输出结果：`/usr/meng/ff`
**注意：未赋值的变量，或者前面未定义的变量,输出是空串**
如果变量值中含有空格，制表符和换行符，应该用双引号括起来。
### 6.1.4 命令替换
有两种形式可以把一个命令的执行结果赋给变量
一种形式是：
>\`命令表\`

其中，命令表使用倒引号引用命令。例如：
```
dir=`pwd`
```
另一种形式是：
>$(命令表)

命令表是用分号隔开的命令，上面的形式可改写为：
```
dir=$(pwd)
```
又如：
```
echo $(pwd;cd /home/mengqc;ls -d)
```
*用户定义的变量值还可以使用`read`命令读入或根据条件进行参数替换*
## 6.2 数组
`bash`只提供一维数组，并且没有限定数组大小。数组元素赋值的一般形式是：
>数组名[下标]=值

例如：
```
city[0]=beijing
city[1]=shanghai
city[2]=tianjin
```
也可以用`declare`命令声明一个数组，一般形式是：
>declare -a 数组名

读取数组元素值的一般格式是：
>${数组名[下标]}

例如：
```
echo ${city[0]}
```
也可以组合赋值，一般形式是：
>数组名=(值1，值2，...值n)

例如：
```
A=(This is an example of shell script)
echo ${A[0]} ${A[2]} ${A[3]} ${A[6]}
this an example script
echo ${A[8]}

```
A[8]超出数组范围，因此是空串。
数组名表示下标为`0`的数组元素，如`city`等价于`city[0]`。使用`*`或者`@`作为下标，则会以数组中所有元素取代`[*]`或者`[@]`。例如：
```
week=(Mon Tue Sun)
week[6]=Fri
week[4]=Wen
echo ${week[*]}
Mon Tue Sun Wen Fri
```
unset可以取消数组定义，例如用`unset week或unset week[*],unset week[@]`取消数组定义。
## 6.3 变量引用
有效的变量引用方式如下：

<table border="0" align="center">
<tr>
<td>$name</td>
<td>${name}</td>
<td>${name[n]}</td>
<td>${name[*]}</td>
</tr>

<tr>
<td>${name[@]</td>
<td>${name:-word}</td>
<td>${name:=word}</td>
<td>${name:?word}</td>
</tr>

<tr>
<td>${name:+word}</td>
<td>${name#pattern}</td>
<td>${name##pattern}</td>
<td>${name%pattern}</td>
</tr>

<tr>
<td>${name%%pattern}</td>
<td>${#@}</td>
<td><img src="{{ site.baseurl }}/assets/images/2018-8-30/1.png"></td>
<td>${#name}</td>
</tr>

<tr>
<td>${#name[*]}</td>
<td>${#name[@]}</td>
<td></td>
<td></td>
</tr>
</table>
下面对各种引用方式简要说明：

1. `$name` 表示变量`name`的值，若变量未定义，则用控制替换。
2. `${name}` 它与`$name`相同，用`{}`括起来，目的是把变量名与后面的字符分隔开，避免出现混淆，替换后`{}`被取消。
3. `${name[n]}` 表示数组`name`中第n个元素的值。
4. `${name[*]}`和`${name[@]}` 都表示数组`name`中所有`非空元素`的值，每个元素的值用空格分开，如果用双引号把它们都括起来，那么二者的区别是：对于`${name[*]}`,它被扩展成一个词(即字符串),这个词由以空格分开的各个数组元素组成；对于`${name[@]}`,它被扩展成多个词，每个数组元素是一个词，如果数组`name`中没有元素，则`${name[@]}`被扩展为空串，例如：
```
person=("Zhang San","Li Si","Wang Wu")
for i in "${name[*]}"; do echo $i; done
Zhang San Li Si Wang Wu  #（执行结果显示）
for i in "${name[@]}"; do echo $i; done
Zhang San   #(执行结果显示)
Li Si
Wang Wu
``` 
如果表达式`${name[@]}`没有用双引号括起来，那么元素值中嵌入的空格就作为字段分隔符出现，从而重新划分各字段，例如：
```
for i in ${person}; do echo $i; done
Zhang    #(执行结果)
San
Li
Si
Wang 
Wu
```
5. `${name:-word}, ${name:word}, ${name:+word}, ${name:?word}` 它们的计算方法将在下节`参数置换变量`介绍
6. `${name#pattern}`和`${name##pattern}`如果`pattern`与`name`值的开头匹配，那么把`name`值去掉匹配部分之后的结果就是该表达式的值；否则，`name`的值就是该表达式的值。但是，在第一种格式中，`name`值去掉的部分是与`pattern`匹配最少的部分；而在第二种格式中，`name`值去掉的部分是与`pattern`匹配最多的部分。例如：
```
echo $PWD
/home/mengqc
echo ${PWD#*/}
home/mengqc
echo ${PWD##*/}
mengqc
```
其中，`pattern`表示匹配模式，它可以是包含任何字符序列、变量和命令替换及通配符的串。
7. `${name % pattern}`和`${name %% pattern}`如果`pattern`与`name`值的末尾匹配。那么`name`的值中去掉匹配部分后的结果就是该表达式的值；否则，该表达式的值就是`name`的值。在第一种格式中，去掉的部分是最少匹配的部分；而在第二种格式中，去掉的部分是最多匹配的部分。例如：
```
FILE=T.myfile.c
echo ${FILE%.*}
T.myfile
echo ${FILE%%.*}
T
```
8. `${#@}`和`${#*}` 它们的值分别是由`$@`个`$*`返回的参数的是。
9. `${#name[i]}`其值是数组`name`第`i`个元素值的长度(字符个数)
10. `${#name[*]}`和`${#name[@]}`它们的值就是数组`name`中已经设置的元素的个数。

## 6.4 输入/输出命令
### 6.4.1 read命令
可以利用`read`命令从键盘上读取数据，然后赋值给制定的变量。`read`命令的一般格式是：
>read 变量1[ 变量2... ]

例如：
```
read a b c
```
利用read可以交互式的给变量赋值，输入数据时，数据间以`空格`或者`制表符`作为分隔符，变量个数和数据个数可出现下属三种情况。
1. 变量个数与给定数据个数相同，则依次对应赋值。例如：
```
read x y z
Today is Monday
echo &z &x &y
Monday Today is
```

2. 变量个数少于数据个数，则从左至右对应赋值，但最后一个被赋予剩余的所有数据，例如：
```
read n1 n2 n3
First Second Third 1234 abcd [按enter]
echo $n3
Third 1234 abcd
echo $n2 $n1
Second First
```

3. 变量个数多于给定数据个数，则依次对应赋值，而没有数据与之对应的变量的变量取空串。例如：

```
read n1 n2 n3
#(用户输入) 
1 2 [按enter]
echo $n3

echo $n1 $n2
1 2
```

### 6.4.2 echo命令
`echo`后面各参数以空格隔开，以换行符终止。如果`echo`带有选项`-e`,那么其后的参数中可以有一下转义字符，用于输出控制或印出无法显示的字符。这些转义字符及其作用如下：
1. `\a` 响铃报警
2. `\b` 退一个字符位置
3. `\c` 它出现在参数的最后位置，在它之前的参数被显示后，光标不换行，新的输出信息接在该行的后面。例如，执行`echo -e "Enter the file name  ->\c"`之后：
```
Enter the file name ->$_
```
这种形式与带`-n`选项的命令功能相同：
```
echo -n "Enter the file name ->"
```
4. `\e`转义字符
5. `f`换页
6. `\n`显示换行
7. `\r`回车
8. `\t`水平制表符
9. `\v`垂直制表符
10. `\\`印出反斜线
11. `\m`m是一个1位，2位或3位八进制数，它表示一个`ASCII`码字符，m必须以0开头。
12. `\xm`m是一个1位，2位和3位十六进制数，它表示一个ASCII码字符。

## 6.5 位置参数
### 6.5.1 位置参数及其应用
在`shell`脚本的位置参数分别是：0,1,2，...，因为它们与命令行上具体位置的实参相对应。命令名(脚本名)对应位置变量0，第一个实参对应位置变量1，第二个实参对应位置变量2，...,如果位置变量是由两个或更多的数字构成，那么必须用一对`{}`括起来，如`{10}`,`{11}`,命令行实参与脚本中位置变量的对应关系如下：
![图片找不到了]({{ site.baseurl }}/assets/images/2018-8-30/3.png)
### 6.5.2 用set命令为位置参数赋值
在shell程序中可以利用`set`命令为位置参数赋值或重新赋值，例如，`set m1.c m2.c m3.c`把字符串`m1.c`赋值给`$1`,`m2.c`赋值给`$2`,`m3.c`赋值给`$3`,但是`$0`不能用`set`命令赋值，它的值总是命令名。
## 6.6 移动位置参数
如果在脚本中使用的位置参数不超过9个，那么只用`$1～￥9`即可，但是，实际给定的命令行参数有可能多余9个，此时就需要用`shift`命令移动位置参数，没执行一次`shift`命令，就把命令行上的实参向左移一位，即相当于位置参数向右移动一个位置。
```
命令行：       ex7   A   B   C   D   E   F
原位置参数：    $0   $1  $2  $3  $4  $5  $6 
移位后位置参数： $0       $1  $2  $3  $4  $5
```
可以看出，`shift`命令执行后，新`$1`的值是原`$2`的值，新`$1`的值是原`$2`的值，新`$2`的值是原`$3`的值，依次类推。
`shift`命令不能将`$0`移走，所以经`shift`右移位置参数后，`$0`的值不会发生变化，`shift`命令可以带有一个整数作为参数，例如，`shift 3`的功能是，每次把位置参数右移`2`为，如果未带参数，则默认值为`1`。`shift`命令示例：
```
cat ex8
#!/bin/bash
#ex8 shell script to demonstrate the shift command
echo $0 $1 $2 $3 $4 $5 $6 $7 $8 $9
shift
echo $0 $1 $2 $3 $4 $5 $6 $7 $8 $9
shift 4
echo $0 $1 $2 $3 $4 $5 $6 $7 $8 $9
#end
```
其输出是：
> ex8  A  B  C  D  E  F  G  H  I  J  K<br>
> ex8  A  B  C  D  E  F  G  H  I<br>
> ex8  B  C  D  E  F  G  H  I  J<br>
> ex8  F  G  H  I  J  K<br>

从实例可以看出，使用`shift`命令可以将后面的实参移到前面来，从而得到处理。
## 6.7 预先定义的特殊变量
在shell中，预先定义了几个有特殊含义的shell变量，它们的值只能由shell根据实际情况来赋值，而不能有用户重新设置。

|$#|表示命令行上参数的个数，但不包含shell脚本名本身|
|$?|表示上一条命令执行后的返回值，他是一个十进制数，多数shell命令执行成功是，返回值为0值：如果执行失败，则返回实际参数的个数。|
|$$|表示当前进程的进程号。每个进程都有唯一的进程号(即PID)，所以利用`$$`的值可为临时文件生成唯一的文件名|
|$!|表示上一个后台命令对应的进程号，是一个由`1~5`位数字构成的数字串|
|$-|是由当前shell设置的执行标志名组成的字符串|
|$*|表示在命令行中实际给出的所有实参字符串，它并不仅限于9个实参|
|$@|与$*相同，但是使用时加引号，并在引号中返回每个参数。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。| 

# 7 参数置换变量
参数置换变量是另一种为变量赋值的方式，其一般形式是：
>变量2=$(变量1 op 字符串)

其中，`op`表示操作符，它可以是下列4个操作符之一：`：-， ：=， ：+和:?`，变量2的值取决于变量1是否为空串，利用哪个操作符，以及字符串的取值。操作符前后不能留空格。以下是对其总结：
<table align="center">
<tr>
<th>格式</th>
<th>var1为空</th>
<th>var1不为空</th>
</tr>

<tr>
<td>var2=${ var1:-string }</td>
<td>var2=string<br>
var1不变</td>
<td>var2=$var1<br>
var1不变</td>
</tr>

<tr>
<td>var2=${ var1:=string }</td>
<td>var2=string<br>
var1=string</td>
<td>var2=$var1<br>
var1不变</td>
</tr>

<tr>
<td>var2=${ var1:+string }</td>
<td>var2为空<br>
var1不变</td>
<td>var2=string<br>
var1不变</td>
</tr>

<tr>
<td>var2=${ var1:?string }</td>
<td>输出格式：<br>
shell脚本名：var:string<br>
并退出shell<br>
var2不变</td>
<td>var2=$var1<br>
var1不变</td>
</tr>
</table>

# 8 算数运算
`bash`中执行整数算数运算的敏玲是`let`,其语法格式为：
>let arg...

其中，`arg`是单独的算数表达式，表达式与c语言的表达式语法一样，命名参数在表达式中直接利用名称访问，前面不要带`$`符。
`let`命令的替代表示形式是：
>((算数表达式))

bash中的算数运算符及其优先级和结合性

<table align="center" width="100%">
<tr>
<td style="background-color:#bdc3c7;">优先级</td>
<td style="background-color:#bdc3c7;">运算符</td>
<td style="background-color:#bdc3c7;">结合性</td>
<td style="background-color:#bdc3c7;">功能</td>
</tr>

<tr>
<td rowspan="2">1</td>
<td>id++</td>
<td>&lt;-----</td>
<td>变量id后缀加</td>
</tr>

<tr>
<td>id--</td>
<td>&lt;-----</td>
<td>变量id后缀减</td>
</tr>

<tr>
<td rowspan="2">2</td>
<td>++id</td>
<td>&lt;-----</td>
<td>变量id前缀加</td>
</tr>

<tr>
<td>--id</td>
<td>&lt;-----</td>
<td>变量id前缀减</td>
</tr>

<tr>
<td rowspan="2">3</td>
<td>-</td>
<td>&lt;-----</td>
<td>取表达式的负值</td>
</tr>

<tr>
<td>+</td>
<td>&lt;-----</td>
<td>取表达式的正值</td>
</tr>

<tr>
<td rowspan="2">4</td>
<td>！</td>
<td>&lt;-----</td>
<td>逻辑非</td>
</tr>

<tr>
<td>～</td>
<td>&lt;-----</td>
<td>按位取反</td>
</tr>

<tr>
<td>5</td>
<td>**</td>
<td>-----&gt;</td>
<td>方幂</td>
</tr>

<tr>
<td rowspan="3">6</td>
<td>*</td>
<td>-----&gt;</td>
<td>乘</td>
</tr>

<tr>
<td>/</td>
<td>-----&gt;</td>
<td>除</td>
</tr>

<tr>
<td>%</td>
<td>-----&gt;</td>
<td>取模</td>
</tr>

<tr>
<td rowspan="2">7</td>
<td>+</td>
<td>-----&gt;</td>
<td>加</td>
</tr>

<tr>
<td>-</td>
<td>-----&gt;</td>
<td>减</td>
</tr>

<tr>
<td rowspan="2">8</td>
<td>&lt;&lt;</td>
<td>-----&gt;</td>
<td>左移若干二进制位</td>
</tr>

<tr>
<td>&gt;&gt;</td>
<td>-----&gt;</td>
<td>右移若干二进制位</td>
</tr>

<tr>
<td rowspan="4">9</td>
<td>&gt;</td>
<td>-----&gt;</td>
<td>大于</td>
</tr>

<tr>
<td>&gt;=</td>
<td>-----&gt;</td>
<td>大于等于</td>
</tr>

<tr>
<td>&lt;</td>
<td>-----&gt;</td>
<td>小于</td>
</tr>

<tr>
<td>&lt;=</td>
<td>-----&gt;</td>
<td>小于等于</td>
</tr>

<tr>
<td rowspan="2">10</td>
<td>==</td>
<td>-----&gt;</td>
<td>相等</td>
</tr>

<tr>
<td>！=</td>
<td>-----&gt;</td>
<td>不相等</td>
</tr>

<tr>
<td>11</td>
<td>&</td>
<td>-----&gt;</td>
<td>按位与</td>
</tr>

<tr>
<td>12</td>
<td>^</td>
<td>-----&gt;</td>
<td>按位异或</td>
</tr>


<tr>
<td>13</td>
<td>|</td>
<td>-----&gt;</td>
<td>按位或</td>
</tr>

<tr>
<td>14</td>
<td>&&</td>
<td>-----&gt;</td>
<td>逻辑与</td>
</tr>


<tr>
<td>15</td>
<td>||</td>
<td>-----&gt;</td>
<td>逻辑或</td>
</tr>

<tr>
<td>16</td>
<td>?:</td>
<td>&lt;-----</td>
<td>条件计算</td>
</tr>

<tr>
<td rowspan="6">17</td>
<td>=</td>
<td>&lt;-----</td>
<td>赋值</td>
</tr>

<tr>
<td>+=  -=</td>
<td rowspan="5">&lt;-----</td>
<td rowspan="5">运算且赋值</td>
</tr>

<tr>
<td>*=  /=</td>
</tr>

<tr>
<td>%=  &=</td>
</tr>

<tr>
<td>^=  !=</td>
</tr>

<tr>
<td>&gt;&gt;=  &lt;&lt;=</td>
</tr>

<tr>
<td>18</td>
<td>,</td>
<td>-----&gt;</td>
<td>从左到右顺序计算，如expr1,expr2</td>
</tr>
</table>

bash表达式中可以使用括号，用来改变运算符的操作顺序。当表达式中有shell的特殊字符时，必须用双引号括起来。例如：`let "val=a|b"`。如果不括起来，shell会把命令行`let val=a|b`中的`|`看做管道线，利用`let`命令的等价形式`((...))`时，算数表达式可以不用双引号括起来。例如：
```
((v=6|5))
echo $v_
7
```
**注意，((...))只能包含一个算数表达式，并且只有使用$((算数表达式))形式，才能返回表达式的值。**例如：
```
echo "((12*9))"
((12*9))
echo "$((12*9))"
108
```
*当`let`命令计算表达式的值时，若最后结果不为0，则`let`命令的返回值为0（表示“真”），否则，返回1（表示“假”），因此，`let`命令可以用于`if`语句的条件测试。*
# 9 控制结构
## 9.1 if语句
其一般形式为：
```
if 测试条件
then 命令1
else 命令2
fi
```
通常，`if`测试部分是利用`test`命令实现的。其实，条件测试可以利用一般命令执行成功与否来做判断，如果命令正常结束，则表示执行成功，其返回值为0，条件测试为真；如果命令执行不成功，其返回值不为非0，条件测试为假。所以`if`的语句的更一般形式是：
```
if 命令表1
then 命令2
else 命令3
fi
```
## 9.2 条件测试
条件测试有三种形式：
第一种使用`test`命令。
第二种是用一对方括号`[]`将测试条件括起来。这两种形式是等价的。例如，测试位置参数`$1`是否`s`是已存在的普通文件，可写为：
```
test -f "$1"
```
也可以写成：
```
[ -f "$1" ]
```
第三种形式是：
>[[条件表达式]]

`test`命令可以和多种系统运算符一起使用，这些运算符可以分为4种：`文件测试运算符`、`字符串测试运算符`、`数值测试运算符`和`逻辑运算符`。<br>
### 9.2.1 文件测试运算符的形式及其功能

|参数|功能|
|-r 文件名|若文件存在并且是用户可读的，则测试条件为真|
|-w 文件名|若文件存在并且是用户可写的，则测试条件为真|
|-x 文件名|若文件存在并且是用户可执行的，则测试条件为真|
|-f 文件名|若文件存在并且是普通文件，则测试条件为真|
|-d 文件名|若文件存在并且是目录文件，则测试条件为真|
|-p 文件名|若文件存在并且是命名的FIFO文件，则测试条件为真|
|-b 文件名|若文件存在并且是块设备文件，则测试条件为真|
|-c 文件名|若文件存在并且是字符设备文件，则测试条件为真|
|-s 文件名|若文件存在并且是文件的长度大于0，则测试条件为真|
|-t 文件描述字|若文件被打开且其文件描述字是与终端设备相关的，则测试条件为真，默认的“文件描述字”是1|

### 9.2.2 字符串测试运算符的形式以及功能

|参数|功能|
|-z s1|如果字符串s1的长度为0，则测试条件为真|
|-n s1|如果字符串s1的长度大于0，则测试条件为真|
|s1|如果字符串s1不是空字符串，则测试条件为真|
|s1=s2|如果s1等于s2，则测试条件为真."="也可以用"=="代替，在“=”前后应有空格|
|s1!=s2|如果s1不等于s2，则测试条件为真|
|s1&lt;s2|如果按字典顺序s1在s2之前，则测试条件为真|
|s1&gt;s2|如果按字典顺序s1在s2之后，则测试条件为真|

### 9.2.3 数值测试运算符

|参数|功能|
|n1 -eq n2|如果整数n1等于整数n2，则测试条件为真|
|n1 -ne n2|如果整数n1不等于整数n2，则测试条件为真|
|n1 -lt n2|如果整数n1小于整数n2，则测试条件为真|
|n1 -le n2|如果整数n1小于等于整数n2，则测试条件为真|
|n1 -gt n2|如果整数n1大于整数n2，则测试条件为真|
|n1 -ge n2|如果整数n1大于等于整数n2，则测试条件为真|

### 9.2.4 逻辑运算符

|符号|作用|
|！---逻辑非(NOT)|它放在任意逻辑表达式之前，使原来为真的表达式为假，原来为假的变为真|
|-a---逻辑与(AND)|它放在两个逻辑表达式之间，仅当两个表达式都为真时，结果才为真|
|-o---逻辑或(OR)|它放在两个逻辑表达式之间，其中只要有一个表达式为真，结果就为真|
|(表达式)---圆括号|它把一个逻辑表达式括起来是之成为一个整体，优先得到运算|

### 9.2.5 特殊条件测试
除了以上条件测试外，在`if`语句和循环语句中，还常用下列三个特殊条件测试语句
>1. `:`表示不做任何事情，其退出值为0
>2. `true`表示总为真，其退出值是0
>3. `false`表示总为假，其退出值是255

## 9.3 case语句
case语句允许进行多重条件选择，其一般语法形式是：
```
case 字符串 in
模式字符串1) 命令
           ...
           命令;;
模式字符串2) 命令
           ...
           命令;;
    ...
模式字符串n) 命令
           ...
           命令;;
esac
```
>1. 每个模式字符串后面可有一条或多条mingling，其最后一条命令必须以两个分号(即;;)结束
>2. 模式字符串中可以使用通配符
>3. 如果一个模式字符串中包含多个模式，那个各模式之间应以竖线`(|)`隔开，表示格式是“或”的关系，即只要给定字符串与其中一个模式匹配，就会执行其后的命令表。
>4. 各模式字符串应是唯一的，不应重复出现。并且要合理安排它们的出现顺序。
>5. `case`语句以关键字`case`开头，以关键字`esac`结束
>6. `case`的退出（返回）值是整个结构中最后执行的那个命令的退出值。若没有执行任何命令，则退出值为0。

## 9.4 while语句
shell中有三种用于循环的语句，即`while`，`for`和`until`语句。
while的一般形式是：
```
while 测试条件
do
    命令表
done
```
其执行过程是先进行条件测试，若为真，则进入循环，执行其中命令，再做条件测试......直至测试条件为假时，才终止`while`语句的执行。
## 9.5 until语句
until语句的一般形式是：
```
until 测试条件
do
    命令表
done
```
测试条件与`while`不同，当测试条件为假时，才进入循环体。直至测试条件为真时终止循环。
## 9.6 for语句
### 9.6.1 值表方式
其一般格式为：
```
for 变量 [in 值表]
do  
    命令表
done
```
值表可以是文件正则表达式，其格式为：
```
for 变量 in 文件正则表达式
do
    命令表
done
```
### 9.6.2 算数表达式方式
其一般格式为:
```
for((e1;e2;e3))
do
    命令表
done
```
其中，`e1,e2,e3`是算术表达式，它的执行过程与C语言中for语句相似。`e1,e2,e3`这三个表达式中任何一个都可以减少，但彼此间的分号不能缺少，在此情况下，缺省的表达式默认值为1.
整个`for`语句的返回值是`命令表中最后一条命令执行后的返回值，`如果任一算术表达式非法，那么该语句失败。
## 9.7 break命令和continue命令
### 9.7.1 break命令
`break`命令可以使脚本从循环中退出来，其语法格式是：
>break [n]

其中，`n`表示跳出`n`层循环，默认值为`1`，表示跳出一层循环，如果`n=3`，则表示跳出`3`层循环。
### 9.7.2 continue命令
`continue`命令跳出循环体中在它之后的语句，回到本层循环的开头，进行下一次循环。其语法格式是：
>continue [n]

其中，`n`表示从包含`continue`语句的最内层循环体向外跳到第`n`层循环。默认值为1。循环曾数由内向外编号。
## 9.8 exit命令
`exit`命令的功能是立即退出正在执行的`shell`脚本，并设定退出值。其语法格式是：
>exit [n]

其中，n是设定的退出值（退出状态）。如果未显示给出n的值，则退出值设为最后一个命令的执行状态。
## 9.9 select语句
`select`语句通常用于菜单的设计，它自动完成接受用户输入的整个过程，包括显示一组菜单项及读入用户的选择。`select`语句的语法格式是：
```
select identifier[in word...]
do
    命令表
done
```
`select`语句的应用：
```
cat ex16
PS3="Choice?"
select choice in query add delete update list exit
do
   case "$choice" in
     query) echo "Call query routine"
            break;;
     add) echo "Call add routine"
            break;;
     delete) echo "Call delete routine"
            break;;
     update) echo "Call update routine"
            break;;
     list) echo "Call list routine"
            break;;
     exit) echo "Call exit routine"
            break;;
   esac
done
echo "Your choice is:$choice"

ex16
1)query
2)add
3)delete
4)update
5)list
6)exit
echice? 2 (用户输入2)
Call add routine
Your choice is: add
```
执行`select`语句时，会列出序号`1～n`标记的菜单，序号与`in`之后给定的字(word)对应，然后给出提示（PS3的值），并接受用户的选择，并将该数据赋给环境变量`REPLY`。如果输入的数据是`1～n`中的一个值，那么参数`identifier`（本例中为choice）就置为该数字对应的字。如果未输入数据，则重新显示该菜单，该参数设置为`null`。对于每一个选择执行`do-done`的命令行，直至遇到`break`或者文件结束标志。
**如果in word...这一部分省略，那么参数identifier就以位置参数($1,$2,...)作为给定的值**
# 10 函数
在`shell`脚本中可以定义并使用函数。其定义格式如下：
```
[function]函数名()
{
    命令表
}
```
其中，关键字`function`可以默认。例如：
```
showfile()
{
    if[ -d "$1" ]
    then cd "$1"
        cat m*.c|pr
    else echo "$1 is not a diretory."
    fi
    echo "End of the function"
}
```
函数先定义，后会用。调用函数时，直接利用函数名，如`showfile`,不必带圆括号，就像一般命令那样使用。`shell`脚本与函数间的参数传递可利用位置参数和变量直接传递。变量的值可以由`shell`脚本传递给被调用函数，而函数中所用的位置参数`$1, $2`等对应于函数调用语句中的实参，这一点与普通命令不同。例如：`showfile /home/mengqc`中，其实参`/home/mengqc`是函数`showfile`中`$1`的值。
函数应用示例：
```
cat ex17
#func is a function name
#it echos the values of variables and arguments
func()
{
    echo "Let's begin now."
    echo $a $b $c
    echo $1 $2 $3
    echo "The end."
}
a="Working directory"
b="is"
c=`pwd`
func Welcome You Byby
echo "Today is `date`"

ex17
Let's begin now
Working directory is /home/mengqc
Welcome You Byby
The end.
Today is 2018年 09月 01日 星期六 22:26:17 CST
```
shell中的函数把若干命令集合在一起，通过一个函数名加以调用。如果需要，还可多次调用。执行函数并不创建新的进程。而是通过shell进程执行。<br>
通常，函数中的最后一个命令执行之后，就退出被调用函数。也可利用return命令立即退出函数，其语法个还是是：
>return [n]

其中，n是退出函数时的退出值（退出状态），即`$?`的值，当n值默认时，则退出值是最后一个命令执行后的退回值。
# 11 shell文件包含
和其他语言一样，Shell 也可以包含外部脚本。这样可以很方便的封装一些公用的代码作为一个独立的文件。
Shell 文件包含的语法格式如下：
```
. filename   # 注意点号(.)和文件名中间有一空格

或

source filename
```
