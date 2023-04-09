import requests
import json
import os

# secret_key = os.environ["COMMITRESULTTOREP"]
secret_key2 = os.environ["GITEE_TOKEN"]

print(secret_key2)

# # GitHub API Token
# GITHUB_TOKEN = "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"

# # Gitee API Token
# GITEE_TOKEN = "2423fd11aafd58c6c0d0bbf4aeb40434"

# # GitHub Repo Details
# GITHUB_REPO_OWNER = "IanIsMyUsername"
# GITHUB_REPO_NAME = "travis_ci_test"

# # Gitee Repo Details
# GITEE_REPO_OWNER = "swiftyizhou"
# GITEE_REPO_NAME = "sswiftgg-plugin-api"

# # GitHub File Details
# GITHUB_FILE_PATH = "abc.text"

# # Gitee File Details
# GITEE_FILE_PATH = "content/cde.txt"
# GITEE_FILE_CONTENT = "cde.txt"

# # GitHub API URLs
# GITHUB_API_URL = "https://api.github.com"
# GITHUB_REPO_URL = f"{GITHUB_API_URL}/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}"
# GITHUB_FILE_URL = f"{GITHUB_REPO_URL}/contents/{GITHUB_FILE_PATH}"

# # Gitee API URLs
# GITEE_API_URL = "https://gitee.com/api/v5"
# GITEE_REPO_URL = f"{GITEE_API_URL}/repos/{GITEE_REPO_OWNER}/{GITEE_REPO_NAME}"
# GITEE_FILE_URL = f"{GITEE_REPO_URL}/contents/{GITEE_FILE_PATH}"

# # GitHub Headers
# GITHUB_HEADERS = {
#     "Accept": "application/vnd.github.v3+json",
#     # "Authorization": f"token {GITHUB_TOKEN}"
# }

# # Gitee Headers
# GITEE_HEADERS = {
#     "Accept": "application/json",
#     "Content-Type": "application/json;charset=UTF-8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#     "Private-Token": GITEE_TOKEN
# }

# # Get GitHub File Details
# response = requests.get(GITHUB_FILE_URL, headers=GITHUB_HEADERS)
# github_file_details = json.loads(response.content)['content'].rstrip("\n")

# # Get the SHA of the existing file on Gitee (if it exists)
# response = requests.get(GITEE_FILE_URL, headers={"User-Agent": "Mozilla/5.0", "Authorization": f"Bearer {GITEE_TOKEN}"})
# if response.status_code == 200:
#     sha = response.json()["sha"]
# else:
#     sha = None

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

# # Push File to Gitee
# response = requests.put(GITEE_FILE_URL, headers=GITEE_HEADERS, json=gitee_file_payload)

# if response.status_code == 200:
#     print("File pushed to Gitee successfully!")
# else:
#     print(f"Failed to push file to Gitee: {response.content}")
