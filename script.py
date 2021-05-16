from github import Github
import os
import re
import requests
import yaml
import sys

print('Environment')
print(os.environ)

token = os.getenv("INPUT_REPO_TOKEN")
repo_string = os.getenv("GITHUB_REPOSITORY")
g = Github(token)

repo = g.get_repo(repo_string)
# issue = repo.get_issue(number=12)
# print(issue.title)
# print(issue.body)

# is_presentaiton = False
# print("\nISSUE LABELS")
# labels = issue.get_labels()
# for label in labels:
#     print(label.name)
#     if label.name == 'presentation':
#         is_presentation = True

# # Build regular expression to parse images
# p = re.compile(r'^\!\[[^\]]*]\(([^\)]*)\)')
# image_url = None

# # Let's look at all the comments
# print("\nISSUE COMMENTS:")
# comments = issue.get_comments()
# for comment in comments:
#     results = p.search(comment.body)
#     if results:
#         image_url = results.group(1)
#         print(image_url)
#     else:
#         dict = yaml.safe_load(comment.body)
#         print(dict)

# # Download the image (if found)
# if image_url:
#     filename = 'temp.jpg'
#     request = requests.get(image_url, stream=True)
#     if request.status_code == 200:
#         with open(filename, 'wb') as image:
#             for chunk in request:
#                 image.write(chunk)