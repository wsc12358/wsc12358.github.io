---
layout: post
title: python遇到的小问题
background: red
background-image: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535987243669&di=f35aed4999121d345a4027d38aa81e2d&imgtype=0&src=http%3A%2F%2Fs13.sinaimg.cn%2Fmw690%2F006aHRmjzy7g7ZZs7gg1c
categories:
- 编程语言
tags:
- python
author: Dimension
description: 这里主要记录了一些日常开发中遇到的python小问题，在这里做一总结
mermaid: true
date: 2018-09-03 20:16:11
ico: note
---

* 目录   
{:toc #markdown-toc}
<br>

## python中如何在字符串中插入变量
代码示例：
```
import sys
import time
import os

date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
time=time.strftime('%H:%M:%S',time.localtime(time.time()))

str=f'现在时间： {date} {time}'
print(str)

输出：现在时间： 2018-09-03 20:23:36
```

## python中终端输入
代码示例：
```python
str=input()
print(str)

（用户输入） hello world
输出： hello world
```

## python中实现switch/case语句
代码示例：
```
#coding=utf-8
import sys
import time
import os

date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
time=time.strftime('%H:%M:%S',time.localtime(time.time()))

def status():
    print("Show some infomation about status")

def add_all():
    print("Successfully add all changes")

def commit():
    print("Successfully commit")

def push():
    print("Successfully push")

def pull():
    print("Successfully pull from github")

def other():
    print("Your choice was wrong")

def notify_result(num):
    numbers = {
        0 : push,
        1 : pull,
        2 : commit,
        3 : add_all,
        4 : status
    }

    method = numbers.get(num, other)
    if method:
        method()

def show():
    print("choice?")
    print("0 : push")
    print("1 : pull")
    print("2 : commit")
    print("3 : add_all")
    print("4 : status")
    

if __name__ == "__main__":
    show()
    choice=input()
    notify_result(int(choice,base=10))

(用户输入)：1
输出： Successfully pull from github
```
## python中调用系统命令
代码示例：
```
import os
os.system('git status')

输出：
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   create.py
        deleted:    test.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        _posts/2018-09-03-python-note.md

no changes added to commit (use "git add" and/or "git commit -a")
```
## 创建文件并在文件中写入字符串
代码示例：
```
seq=["---\n",
    "layout: post\n",
    "title: "+post_title+"\n",
    "background: red\n",
    "background-image:\n",
    "categories:\n",
    "-\n",
    "tags:\n",
    "-\n",
    "author: Dimension\n",
    "description:\n",
    "mermaid: true\n",
    "date: "+date+" "+time+"\n",
    "ico:\n",
    "---\n",
    "\n",
    "* 目录   \n",
    "{:toc #markdown-toc}"]

file=open("_posts/"+file_name,"w",encoding='utf-8')
for sequence in it:   
    file.write(sequence)
file.close()
```
或者
```
file=open("_posts/"+file_name,"w",encoding='utf-8')
file.writelines(seq)
file.close()
```




