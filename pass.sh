#!/bin/bash

mkdir pass
cd pass
git clone git@gitee.com:swiftyizhou/swiftgg-plugin-api.git
cp -r ../testContent  swiftgg-plugin-api
cd swiftgg-plugin-api
git config --global user.email "12740625+swiftyizhou@user.noreply.gitee.com"
git config --global user.name "swiftyizhou"
git remote add gitee git@gitee.com:swiftyizhou/swiftgg-plugin-api.git
git checkout mater
git add .
git commit -m "Add files"
git push -f -u gitee master


# curl --location --request POST 'https://gitee.com/api/v5/repos/swiftyizhou/swiftgg-plugin-api/merges' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "access_token": "3892525b43aa6f201f1bdb7f0d4476bb",
#     "head": "new-branch-414",
#     "base": "master",
#     "title": "Merge feature-branch into master",
#     "message": "Merge feature-branch into master"
# }'


# source_branch="new-branch-414"
# target_branch="master"
# curl -X POST \
#   -H "Authorization: token 3892525b43aa6f201f1bdb7f0d4476bb" \
#   -H "Content-Type: application/json" \
#   -d "{\"head\":\"${source_branch}\",\"base\":\"${target_branch}\"}" \
#   "https://gitee.com/api/v5/repos/swiftyizhou/swiftgg-plugin-api/merges"
