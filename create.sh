#!/bin/bash
#author:xu3352
#desc: create a new post articles with template

TITLE=$1
TITLE_ZH=$2
TEMPLATE=draft_template.md
DATE=`date "+%Y-%m-%d"`
TIME=`date "+%H:%M:%S"`
# echo $DATE $TIME

DIR=`pwd`

# file path generate
FILE_NAME="$DATE-`echo $TITLE|sed 's/[ ][ ]*/-/g'`.md"
echo "file name:" _posts/$FILE_NAME

# template content
#CONTENT=`cat $TEMPLATE`

# fill title
POST_TITLE=$TITLE
if [ -n "$TITLE_ZH" ]; then
    POST_TITLE=$TITLE_ZH
fi
CONTENT=`echo "${CONTENT}" | sed "s/{title}/${POST_TITLE}/g"`

# fill time
CONTENT=`echo "${CONTENT}" | sed "s/{time}/${DATE} ${TIME}/g"`

# output file (check exists)
if [ ! -e "$DIR/_posts/$FILE_NAME" ]; then
    echo "---" >>_posts/$FILE_NAME
    echo "layout: post">>_posts/$FILE_NAME
    echo "title: \"${POST_TITLE}\"">>_posts/$FILE_NAME
    echo "background: red">>_posts/$FILE_NAME
    echo "background-image:">>_posts/$FILE_NAME
    echo "categories:">>_posts/$FILE_NAME
    echo "-">>_posts/$FILE_NAME
    echo "tags:">>_posts/$FILE_NAME
    echo "-">>_posts/$FILE_NAME
    echo "author: Dimension">>_posts/$FILE_NAME
    echo "description:">>_posts/$FILE_NAME
    echo "mermaid: true">>_posts/$FILE_NAME
    echo "date: $DATE $TIME">>_posts/$FILE_NAME
    echo "ico:">>_posts/$FILE_NAME
    echo "---">>_posts/$FILE_NAME
    echo "\n">>_posts/$FILE_NAME
    echo "* 目录   ">>_posts/$FILE_NAME
    echo "{:toc #markdown-toc}">>_posts/$FILE_NAME
    echo "Successfully Create a markdown file in _post/"
else
    echo "file exists..." 
fi



