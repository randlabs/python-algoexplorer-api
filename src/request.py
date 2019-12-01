#!/usr/bin/env python

import requests
import json

def fetchGet(url):
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return False
    return response

def fetchPost(url, body):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(body))
    if response.status_code != 200:
        return False
    return response