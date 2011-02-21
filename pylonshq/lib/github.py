# -*- coding: utf-8 -*- 
from github2.client import Github

def init_github(settings):
    api_user = settings.get('github.api.user')
    api_token = settings.get('github.api.token')
    username = settings.get('github.username') or api_user
    return Github(api_user, api_token, requests_per_second=1)