import requests
import json
import time

while True:
    print('Performing API call...')
    data = requests.get("https://opensky-network.org/api/states/all")
    json_data = data.json()
    timestamp = json_data['time']
    datapath = './data/'
    filename = f'{datapath}{timestamp}-opensky-extract.json'

    with open(filename, 'w') as file:
        json.dump(json_data, file)

    print(f'Saving file with timestamp {timestamp}...')
    time.sleep(20)
