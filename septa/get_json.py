from requests import request
from json import loads

headers = {'cache-control': 'no-cache'}


def get_json(url):
    """
    Helper method to post a get request and parse the response as JSON.
    :param url: The string representation of the  URL to which to send the GET request.
    :return: A dict from the JSON response.
    :rtype: dict
    """
    response = request('GET', url, headers=headers)
    return loads(response.text)
