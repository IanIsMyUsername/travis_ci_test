#!/bin/bash

COMMIT_MESSAGE="Automatic Generate Timestamp"
PREV_COMMIT=$(git rev-parse HEAD)
PREV_COMMIT_MESSAGE=$(git log --format=%B -n 1 $PREV_COMMIT)

if [[ "$PREV_COMMIT_MESSAGE" == $COMMIT_MESSAGE ]]; then
    exit
fi


# # 创建文件并写入时间戳
# echo $(date +%s) >> timestamp.txt
git config user.email "15120073241@126.com"
git config user.name "Yizhou"
git add timestamp.txt
git commit -m "Automatic Generate Timestamp"
git push origin main
