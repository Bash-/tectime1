import logging
import requests
import json
import time

logging.basicConfig(filename='./api_logs.log', level=logging.DEBUG)
DELAY_IN_SEC = 5

while True:
    logging.info('Performing API call...')
    data = None
    try:
        data = requests.get("https://opensky-network.org/api/states/all")
        data.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logging.warning(err)

    if data:
        json_data = data.json()
        timestamp = json_data['time']
        datapath = './data/'
        filename = f'{datapath}{timestamp}-opensky-extract.json'

        with open(filename, 'w') as file:
            json.dump(json_data, file)
        logging.info(f'Saving file with timestamp {timestamp}...')
    time.sleep(DELAY_IN_SEC)


