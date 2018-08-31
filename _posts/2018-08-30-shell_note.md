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
---

* 目录   
{:toc #markdown-toc}

# shell概述
shell最初是在UNIX系统中形成和发展的，UNIX中的shell有很多种，Linux继承了UNIX中shell的全部功能，现在默认使用的是bash。
## 1 shell的特点和主要版本
### 1.1 shell的特点
1. 可以组合任意的命令组合成新的命令
2. 允许灵活的使用数据流，提供通配符，输入/输出重定向，管道线机制，方便模式匹配，I/O处理和数据传输。
3. 结构化程序模块
4. 提供后台执行的能力
5. 提供可配置环境，允许用户创建和修改命令，命令提示符和其他系统行为。
6. 提供一个高级命令语言，允许用户创建从简单到复杂的程序，这些称为shell脚本，利用shell脚本，可以把Linux命令组合起来，作为新的命令使用。

### 1.2 shell的种类
Linux提供多种不同的shell，常用的有Bourne shell(简称 sh)、C shell(简称 csh)、Korn shell(简称 ksh)和Bourne Again shell(简称 bash)
## 2 shell脚本的建立和执行
### 2.1 shell脚本的建立
shell脚本可以用任意的编辑器创建，例如vim,emacs等
### 2.2 shell脚本的执行
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
# 命令历史
bash提供了命令历史功能，系统为每个用户维护了一个命令历史文件(~/.bash_history),查看历史命令可以在命令提示符后输入`history`即可
## 1 显示历史命令
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
## 2 执行历史命令
表1列出了基本事件字格式及意义，利用它们可以访问历史表中的命令行
表1 基本事件制定字格式及其意义

| 格式        | 意义   |
|!!|重新上一条命令，也就是"!-1"|
|!n|重新执行第n条历史命令|
|!-n|重新执行倒数第n条命令，如!-1就等于!!|
|!string|重新执行以string开头的最近的历史命令行，例如!ca表示访问钱满最近的cat命令|
|!?string?|重新执行最近的、其中包含字符串string的那条历史命令，例如，!?hist?表示重复前面的含有hist的命令|
|!#|到现在位置所有输入的整个命令行|


## 3 配置历史命令环境
默认方式下，bash用户的历史命令保存在用户主目录下的`.bash_history`文件中，但用户可以通过对环境变量`HISTFILE`赋值来改变存放历史命令的文件，例如：
```
$HISTFILE="/home/用户名/.myhistory"
```
默认情况下历史文件只能保存500条命令，超过限定值，最早的命令就会被删除，可以设置环境变量`HISTSIZE`来修改存放命令数
```
$HISTSIZE=600
```
# 命令补全
输入目录名或文件名的开头部分，按`Tab`键即可补全，如果输入过程中不知道后面的字符，而系统也无法确定唯一的名称时，可以先按`Esc`键，再按`?`键，系统将输出所有的可匹配字符
# 别名
## 1 定义别名
定义别名的格式如下：
```
alias [name=[value]]
```
如果没有参数，将在标准输出上显示别名清单，其格式为:`name=value`,其中，name是定义的别名名称，value是别名所代表的内容。
下面是一个定义别名的例子赋值号`=`左右不能有空格：
```
alias ll='ls -l'
```
## 2 取消别名
如果想取消别名，可使用如下命令：
```
unalias name...
```
执行后，就从别名表中删除由`name`制定的别名。例如：
```
unalias ll
```
再执行`ll`,将输出`ll: alias not found`
# shell的特殊字符
shell中除使用普通字符外，还使用一些特殊字符，它们有特定的含义，如通配符`*`和`?`,管道线`|`,以及单引号，双引号等
## 1 通配符
### 1.1 一般通配符
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
### 1.2 模式表达式
模式表达式是那些包含一个或多个通配符的字。`bash`除支持`Bourne shell`中的`*`,`.`,`?`和`[...]`通配符外，还提供特有的扩展模式匹配表达式，下面介绍其形式和含义。
1. `*`(模式表)---匹配给定模式表中0次或多次出现的`模式`，各模式之间以`|`分开，例如：`file*(.c|.o)`将匹配文件`file, file.c, file.o, file.c.c, file.o.o, file.c.o, file.o.c`等，但不可以匹配`file.h`或`file.s`等。
2. `+`(模式表)---匹配给定模式表中一次或多次出现的`模式`，各模式之间以`|`分开。例如：`file+(.c|.o)`匹配文件`file.c, file.o, file.c.o, file.c.c`等，但不可以匹配`file。`
3. `？`(模式表)---匹配模式表中任意一种0次或1次出现的`模式`，各模式之间以`|`分开，例如，`file?(.c|.o)`只匹配`file, file.c`和`file.o`,它不匹配多个模式或模式的重复出现，即不匹配`file.c.c, file.c.o`等。
4. `@`(模式表)---仅匹配模式表中给定一次出现的`模式`，各模式之间以`|`分开，例如：`file@(.c|.o)`匹配`file.c`和`file.o`,但不匹配`file, file.c.c, file.c.o`等。
5. `!`(模式表)---除给定模式表中的一个`模式`外，它可以匹配其他任何东西。

可以看出，模式表达式的意义是递归的，每个表达式中都可以包含一个或多个模式，如`file*(.[cho]|.sh)`是合法的模式表达式。<font color='red'>但在使用是应注意，由于带<font color="#000">*</font>和<font color="#000">+</font>的表达式可以匹配给定的组合，若利用此种表达式来删除文件存在危险，有可能将系统配置文件删除。因此，必须小心使用。</font>

## 2 引号
在shell中引号分为三种：单引号、双引号和倒引号。
### 2.1 双引号
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
### 2.2 单引号
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
### 2.3 倒引号
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
## 3输入/输出重定向符
执行一个`shell`命令时，通常会打开3个文件：`标准输入文件(stdin)`、`标砖输出文件(stdout)`和`标准出错输出文件(stderr)`。它们分别对应`键盘`、`屏幕`、`屏幕终端`
### 3.1 输入重定向符号
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

### 3.2 输出重定向符
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
`命令>文件名`



