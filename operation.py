#coding=utf-8
import sys
import time
import os

date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
time=time.strftime('%H:%M:%S',time.localtime(time.time()))

def status():
    os.system('git status')
    print("Show some infomation about status")

def add_all():
    status()
    os.system('git add --all')
    print("Successfully add all changes")

def commit():
    add_all()
    str=f'git commit -m "{date}"'
    os.system(str)
    print("Successfully commit")

def push():
    commit()
    os.system('git push')
    print("Successfully push")

def pull():
    os.system('git pull')
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


