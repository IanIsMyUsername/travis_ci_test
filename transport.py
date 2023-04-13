# # 导入GitPython模块
# import git
#
# # 定义本地仓库路径和远程仓库地址
# local_repo_path = 'testContent/'
# remote_repo_url = 'https://gitee.com/swiftyizhou/swiftgg-plugin-api.git'
#
# # 初始化Git仓库对象
# repo = git.Repo(local_repo_path)
#
# # 将更改添加到暂存区
# repo.index.add(['folder_to_commit'])
#
# # 提交更改并指定提交信息
# commit_message = 'Committing folder_to_commit'
# repo.index.commit(commit_message)
#
# # 推送更改到远程仓库
# origin = repo.remote(name='origin')
# origin.push()


# import requests
# import json
# import os
#
# # Gitee API Token
# GITEE_TOKEN = os.environ["GITEE_TOKEN"]
#
# # GitHub Repo Details
# GITHUB_REPO_OWNER = "IanIsMyUsername"
# GITHUB_REPO_NAME = "travis_ci_test"
#
# # Gitee Repo Details
# GITEE_REPO_OWNER = "swiftyizhou"
# GITEE_REPO_NAME = "sswiftgg-plugin-api"
#
# # GitHub File Details
# GITHUB_FILE_PATH = "abc.text"
#
# # Gitee File Details
# GITEE_FILE_PATH = "content/cde.txt"
# GITEE_FILE_CONTENT = "cde.txt"
#
# # GitHub API URLs
# GITHUB_API_URL = "https://api.github.com"
# GITHUB_REPO_URL = f"{GITHUB_API_URL}/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}"
# GITHUB_FILE_URL = f"{GITHUB_REPO_URL}/contents/{GITHUB_FILE_PATH}"
#
# # Gitee API URLs
# GITEE_API_URL = "https://gitee.com/api/v5"
# GITEE_REPO_URL = f"{GITEE_API_URL}/repos/{GITEE_REPO_OWNER}/{GITEE_REPO_NAME}"
# GITEE_FILE_URL = f"{GITEE_REPO_URL}/contents/{GITEE_FILE_PATH}"
#
# # GitHub Headers
# GITHUB_HEADERS = {
#     "Accept": "application/vnd.github.v3+json",
# }
#
# # Gitee Headers
# GITEE_HEADERS = {
#     "Accept": "application/json",
#     "Content-Type": "application/json;charset=UTF-8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#     "Private-Token": GITEE_TOKEN
# }
#
# # Get GitHub File Details
# response = requests.get(GITHUB_FILE_URL, headers=GITHUB_HEADERS)
# github_file_details = json.loads(response.content)['content'].rstrip("\n")
#
# # Get the SHA of the existing file on Gitee (if it exists)
# response = requests.get(GITEE_FILE_URL, headers={"User-Agent": "Mozilla/5.0", "Authorization": f"Bearer {GITEE_TOKEN}"})
# if response.status_code == 200:
#     sha = response.json()["sha"]
# else:
#     sha = None
#
# # Create Gitee File Payload
# gitee_file_payload = {
#     "access_token": GITEE_TOKEN,
#     "message": f"Update {GITHUB_FILE_PATH}",
#     "content": github_file_details,
#     "branch": "master",
#     "sha": sha,
#     "committer": {
#         "name": GITEE_REPO_OWNER,
#         "email": f"{GITEE_REPO_OWNER}@users.noreply.gitee.com"
#     }
# }
#
# # Push File to Gitee
# response = requests.put(GITEE_FILE_URL, headers=GITEE_HEADERS, json=gitee_file_payload)
#
# if response.status_code == 200:
#     print("File pushed to Gitee successfully!")
# else:
#     print(f"Failed to push file to Gitee: {response.content}")
