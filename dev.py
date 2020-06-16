import requests
import json
import time
import pprint
import json
import datetime

# Test suite
from test import generate_response

# Constants
DEV_MAX = 20
DEV_MODE = True
CSV_COLS = ['State', 'Account Name', 'Net Deposits', 'Net Profit', 'Total Saved']

fout = "results.csv"
fo = open(fout, 'a')

def entry_screen(dev_mode):
    if not dev_mode:
        print("    /_\\")
        print("   /_|_\\")
        print("  /_|👁️‍🗨️|_\\")
        print(" /_|_|_|_\\")
        print("/_|_|_|_|_\\")
    else:
        print("No fun :(")

def generate_line(response_items, index):
    success = response_items.get('Success')
    payload = response_items.get('Payload')
    errors = response_items.get('Errors')
    date = response_items.get('Date')
    balance = payload['Balance']
    bid_request_amount = payload['BidRequestAmount']
    go_grow_accounts = payload['GoGrowAccounts']
    for account in go_grow_accounts:
        account_name = account['Name']
        deposits = account['NetDeposits']
        profit = account['NetProfit']
        saved = account['TotalSaved']

    # # all data
    # # sequence = [str(errors), state, account_name, str(balance), str(bid_request_amount), str(deposits), str(profit), str(saved)]

    sequence = [str(index), str(date), ('success', 'fail')[errors is not None and success], account_name, str(deposits), str(profit), str(saved)]
    line = ', '.join(sequence)

    print(line)
    return line + '\n'

def write_results(sample, dev_mode):
    if not dev_mode:
        print(len(sample))
    else:
        index = 0
        for response in sample:
            index +=1
            fo.write(generate_line(response, index))
        fo.close

def run_script(current):
    #print('Running script at ' + str(current))
    response = generate_response()

    # real app call
    # response = query_balance()

    # set the date
    response.update( {'Date' : current})
    return response

def main():
    dev_mode = DEV_MODE
    entry_screen(dev_mode)
    starttime=datetime.datetime.now()
    print('Starting script at ' + str(starttime))
    hits = 0
    response_list =[]
    while hits < DEV_MAX:
        current = datetime.datetime.now()
        response = run_script(current)
        response_list.append(response)
        # sanity check
        print(len(response_list))
        hits += 1
        time.sleep(1 * 60)
    write_results(response_list, dev_mode)

if __name__ == '__main__':
    main()
