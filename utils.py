from fake_useragent import UserAgent

import requests

headers = {'User-Agent': UserAgent().random}


def send_post_request(url, data, json=False):
    if json:
        response = requests.post(url, json=data, headers=headers)
    else:
        response = requests.post(url, data=data, headers=headers)

    return response


def phone_convert(phone, type_convert): #1 - 89999999999, #2 - 7 (999) 999-99-99
    if type_convert == 1:
        return '8' + phone[1:]
    elif type_convert == 2:
        return f'{phone[0]} ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9:11]}'
