import requests
import json
import time
import pprint

token = '0telPH0HBn1QUIIIgTcUJqPu752MELPD7WCR75VFCRTwFUUp'
payload = {}
headers = {
  'Authorization': 'Bearer ' + token
}
url = "https://api.bondora.com/api/v1/account/balance"

def query_balance():
    "BOND-1: Makes an API call to the bondora backend to query current account data"
    response = requests.request("GET", url, headers=headers, data = payload)
    if response.status_code == 200:
        print('Success!')
        return response
    elif response.status_code == 404:
        print('Not Found. Aborting')

def map_response(response):
    json_ob = json.loads(response.text.encode('utf8'))
    pprint.pprint(json_ob)

def run_script(current):
    print('Running script at ' + str(current))
    response = query_balance()
    map_response(response)

def main():
    starttime=time.time()
    print('Starting script at ' + str(starttime))
    hits = 0
    while True:
        current = time.time()
        hits += 1
        print ('Tick ' + str(hits))
        run_script(current)
        time.sleep(15 *60)


if __name__ == '__main__':
    main()
