import json

import requests

url = "http://10.10.10.2:8000/report"


def get_lists():
    resp = requests.get(url)
    return json.loads(resp.text)

def get_lists_filtered(bulan, tahun):
    resp = requests.get(f"{url}/{bulan}/{tahun}")
    return json.loads(resp.text)
