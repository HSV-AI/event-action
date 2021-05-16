from github import Github
import os
import re
import requests
import yaml
import sys

token = os.getenv("INPUT_REPO_TOKEN")
g = Github(token)

print('Environment')
print(os.environ)
