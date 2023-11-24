import concurrent.futures
import datetime
import time

import requests

HOST = 'https://base64-api.base64.gke.tanzu.dk'
API_PATH = '/'
ENDPOINT = HOST + API_PATH
MAX_THREADS = 100
CONCURRENT_THREADS = 20

def send_api_request():
    print ('Sending API request: ', ENDPOINT)
    r = requests.get(ENDPOINT)
    print ('Received: ', r.status_code, r.text)

start_time = datetime.datetime.now()
print ('Starting:', start_time)

with concurrent.futures.ThreadPoolExecutor(MAX_THREADS) as executor:
    futures = [ executor.submit(send_api_request) for x in range (CONCURRENT_THREADS) ]
time.sleep(5)
end_time = datetime.datetime.now()
print ('Finished start time:', start_time, 'duration: ', end_time-start_time)