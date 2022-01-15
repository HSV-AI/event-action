from github import Github
import os
import re
import requests
import yaml
import sys
import json
import tweepy

token = os.getenv("INPUT_REPO_TOKEN")
repo_string = os.getenv("GITHUB_REPOSITORY")
g = Github(token)

repo = g.get_repo(repo_string)

path = os.getenv("GITHUB_EVENT_PATH")

with open(path) as f:
  data = json.load(f)

print(data['issue']['number'])
issue_number = data['issue']['number']

issue = repo.get_issue(number=issue_number)
print(issue.title)
print(issue.body)

# Build regular expression to parse images
p = re.compile(r'^\!\[[^\]]*]\(([^\)]*)\)')
image_url = None

# Let's look at all the comments
print("\nISSUE COMMENTS:")
comments = issue.get_comments()
for comment in comments:
    results = p.search(comment.body)
    if results:
        image_url = results.group(1)
        print(image_url)
    else:
        dict = yaml.safe_load(comment.body)
        print(dict)

# Download the image (if found)
if image_url:
    filename = 'temp.jpg'
    request = requests.get(image_url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)