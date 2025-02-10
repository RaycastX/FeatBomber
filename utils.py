from fake_useragent import UserAgent

import requests

headers = {'User-Agent': UserAgent().random}


def send_post_request(url, data, json=False):
    if json:
        response = requests.post(url, json=data, headers=headers)
    else:
        response = requests.post(url, data=data, headers=headers)

    return response


def phone_convert(phone, type_convert): #1 - 89999999999
    if type_convert == 1:
        return '8' + phone[1:]