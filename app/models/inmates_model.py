import json

import requests

url = "http://10.10.10.2:8000"


def get_lists():
    resp = requests.get(url)
    return json.loads(resp.text)


def get_detail(uid):
    resp = requests.get(f"{url}/{uid}")
    if resp.status_code == 200:
        return json.loads(resp.text)
    return None

def get_document(uid):
    resp = requests.get(f"{url}/document/{uid}")
    if resp.status_code == 200:
        return json.loads(resp.text)
    return {"items": ""}
