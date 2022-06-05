import os
from urllib import response
from dotenv import load_dotenv
from random import uniform
import requests
from socket import gethostname
from os import getpid
from time import sleep


load_dotenv()

VARIANT = float(os.getenv('VARIANT'))
SAVE_DATA_URL = os.getenv('SAVE_DATA_URL')
device = gethostname() + str(getpid())


def main():
    sleep(1)

    beetween = 5 * VARIANT
    temperature = uniform(-1 * between, between)

    try:
        response = requests.get(url=SAVE_DATA_URL, params={'temperature': temperature, 'device': device})
    except:
        print('Data not saved')
        return

    if response.headers['Content-Type'] != 'application/json':
        print('Data not saved')
        return
    
    data = response.json()
    if data['result'] is True:
        print('Data saved')
    else:
        print('Data not saved')

while True:
    try:
        main()
    except KeyboardInterrupt:
        break