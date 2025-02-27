from bomber import start_call_bomber, start_sms_bomber, start_callback_bomber, start_bomber
from config import number_attack_types

import time


def start():
    start_bomber('123')
    print('Example: 79999999999')
    phone = input('Enter your phone number (without +): ')

    print("""
    Attack types list
    1. SMS
    2. Call
    3. Callback
    """)

    type_attack = int(input('Select attack type: '))

    if type_attack <= number_attack_types and type_attack != 0:
        if type_attack == 1:
            start_sms_bomber(phone)
        elif type_attack == 2:
            start_call_bomber(phone)
        elif type_attack == 3:
            start_callback_bomber(phone)
    else:
        print('Please select correct type, restart... \n')
        time.sleep(1.5)
        start()
        return

if __name__ == '__main__':
    start()