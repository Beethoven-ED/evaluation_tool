#!/bin/sh

# Usage:
# sh clone_and_eval.sh activity_name github_user_id student_id
activity=$1
userid=$2
studentid=$3

echo "Evaluating $activity for student $studentid (github user $userid)"

if [ ! -d ./$activity ]
then
  mkdir ./$activity
fi

if [ -d ./$activity/$studentid ]
then
  rm -rf ./$activity/$studentid
fi

git clone https://github.com/$userid/$activity.git ./$activity/$studentid

cd ./$activity/$studentid
make
grade=`sh test.sh ./main 0 | tail -`
cd ../../
echo "$studentid,$grade" >> ./$activity.csv


