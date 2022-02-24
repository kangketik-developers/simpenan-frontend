import json

import requests

url = "http://151.106.112.217:8000/attendance"


def get_lists():
    resp = requests.get(url)
    return json.loads(resp.text)


def get_detail(uid):
    resp = requests.get(f"{url}/{uid}")
    if resp.status_code == 200:
        return json.loads(resp.text)
    return {"items": ""}
