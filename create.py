#coding=utf-8
import sys
import time
import os

def replacestr(str):
    sr=''
    for t in str:
        if t==' ':
            sr+='-'
        else:
            sr+=t
    return sr

def main():
    import time

    title=sys.argv[1]
    title_cn=sys.argv[2]
    title1=replacestr(title)
    date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    time=time.strftime('%H:%M:%S',time.localtime(time.time()))

    path=os.getcwd()
    print(os.getcwd())

    file_name=date+'-'+title1+'.md'
    print("file name:"+"_posts/"+file_name)

    post_title=title
    if title_cn!='':
        post_title=title_cn

    if os.path.exists("_posts/"+file_name):
        print("the created file has existed.................")
    else:
        print("create start................")
        post_title.encode('utf-8')
        seq=["---\n",
        "layout: post\n",
        "title:"+post_title+"\n",
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

        # print(seq)
        it=iter(seq)
        file=open("_posts/"+file_name,"w",encoding='utf-8')
        for sequence in it:   
            file.write(sequence)
        file.close()
        print("create finished.................")

if __name__ == '__main__':
    main()