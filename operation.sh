#!/bin/bash
#desc: some operation for article

DATE=`date "+%Y-%m-%d"`
TIME=`date "+%H:%M:%S"`

push()
{
  git commit
  git push
  echo "Successfully push"
}

pull()
{
  git pull
  echo "Successfully pull from github"
}

add-all()
{
   status
   git add --all
   echo "Successfully add all changes"
}

commit()
{
   add-all
   git commit -m "update $DATE $TIME"
   echo "Successfully commit"
}

status()
{
  git status
  echo "Show some infomation about status"
}

PS3="Choice?"
op=(push pull add-all commit status)
select choice in ${op[@]}
do
   case "$choice" in
     push)  push
            break;;
     pull)  pull
            break;;
     add-all) add-all
            break;;
     commit) commit
            break;;
     status) status
            break;;
   esac
done
echo "Your choice is:$choice"
