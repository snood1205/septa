from requests import request
from json import loads

headers = {'cache-control': 'no-cache'}


def get_json(url):
    response = request('GET', url, headers=headers)
    return loads(response.text)
