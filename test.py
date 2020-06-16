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


def generate_response():

    # Mock
    response_text = {'Errors': None, 'Payload': {'Balance': 0.0, 'BidRequestAmount': 0,'GoGrowAccounts': [{'Name': 'Extra Income','NetDeposits': 109.67,'NetProfit': 0.24,'TotalSaved': 109.91}, {'Name': 'Extra Income', 'NetDeposits': 109.67, 'NetProfit': 0.24, 'TotalSaved': 109.91}],'Reserved': 0.0,'TotalAvailable': 0.0},'Success': True}
    #json_ob = json.loads(response_text)
    return response_text
    # pprint.pprint(json_ob)


def mock_query_balance():
    "BOND-1: Makes an API call to the bondora backend to query current account data"
    response = generate_response()
    print(response)
    # if response.status_code == 200:
    #     print('Success!')
    #     return response
    # elif response.status_code == 404:
    #     print('Not Found. Aborting')

def run_script(current):
    print('Running script at ' + str(current))
    response = mock_query_balance()

def main():
    starttime=time.time()
    print('Starting script at ' + str(starttime))
    hits = 0
    while True:
        current = time.time()
        hits += 1
        print ('Tick ' + str(hits))
        run_script(current)
        time.sleep(1 *60)


if __name__ == '__main__':
    main()
