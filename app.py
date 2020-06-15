import requests
import json
import time


token = '0telPH0HBn1QUIIIgTcUJqPu752MELPD7WCR75VFCRTwFUUp'

payload = {}
headers = {
  'Authorization': 'Bearer ' + token
}

def query_balance(headers):
    "BOND-1: Makes an API call to the bondora backend to query current account data"
    url = "https://api.bondora.com/api/v1/account/balance"
    return requests.request("GET", url, headers=headers, data = payload)

def map_response(response):
    json_ob = json.loads(response.text.encode('utf8'))
    print(json_ob.dumps(parsed, indent=4, sort_keys=True))

def run_script(current):
    print('Running script at ' + str(current))
    #response = query_balance(headers)
    #map_response(response)


starttime=time.time()
print('Starting script at ' + str(starttime))

while True:
    current = time.time()
    print ('Tick ')
    run_script(current)
    time.sleep(60.0 - ((current - starttime) % 60.0))
