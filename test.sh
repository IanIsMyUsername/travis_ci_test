#!/bin/bash

# 创建文件并写入时间戳
echo $(date +%s) >> timestamp.txt
git config user.email "15120073241@126.com"
git config user.name "Yizhou"
git add timestamp.txt
git commit -m "Modify example.txt"
git push origin main
