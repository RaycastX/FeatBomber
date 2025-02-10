from utils import phone_convert


def get_call_service(phone):
    call_services = {
        'DNS': {
            'url': 'https://www.dns-shop.ru/auth/auth/fast-authorization/',
            'data': {
                'FastAuthorizationLoginLoadForm[login]': phone,
                'FastAuthorizationLoginLoadForm[token]': '',
                'FastAuthorizationLoginLoadForm[isPhoneCall]': 1,
            },
            'json': False
        },
        'ECPU': {
            'url': 'https://ecpu.ru/login/',
            'data': {
                'city_id': 52,
                'name': 'Raycast',
                'phone': phone,
                'btn_reg': 'Регистрация'
            },
            'json': False
        }
    }

    return call_services


def get_sms_service(phone):
    sms_services = {
        'PAULONIA': {
            'url': 'https://admin.paulonia.ru/api/v1/get_code',
            'data': {
                'phone': phone_convert(phone, 1)
            },
            'json': True
        },
    }

    return sms_services