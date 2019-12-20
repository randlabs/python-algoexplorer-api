#!/usr/bin/env python

import requests
import json

def fetchGet(url: str):
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception('The request generates an unexpected response')
    return response

def fetchPost(url: str, body: dict):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(body))
    if response.status_code != 200:
        raise Exception('The request generates an unexpected response')
    return response