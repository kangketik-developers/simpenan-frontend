import json

import requests

url = "http://151.106.112.217:8000/report"


def get_lists():
    resp = requests.get(url)
    return json.loads(resp.text)

def get_lists_filtered(bulan, tahun):
    resp = requests.get(f"{url}/{bulan}/{tahun}")
    return json.loads(resp.text)