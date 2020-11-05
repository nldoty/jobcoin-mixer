#This file is for keeping track of all API requests.
import json
import requests
import time
from . import config
from .coin_classes import Transaction, Address


def json_print(obj):
    # Used for debugging JSON to make it more readable.
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def check_balance(address):
    # Gets the balance for a single address.
    address_info = get_single_address(address)
    balance = address_info.balance

    return str(balance)


def get_all_transactions():
    # Used to get a log of all transactions from the Jobcoin API. Used for debugging.
    jobcoin_api_url = config.API_TRANSACTIONS_URL
    response = requests.get(jobcoin_api_url)
    response = response.json()

    transactions = []
    for item in response:
        amount = item['amount']
        timestamp = item['timestamp']
        to_address = item['toAddress']
        from_address = item['fromAddress'] if 'fromAddress' in item else None

        transaction = Transaction(amount, timestamp, to_address, from_address)
        transactions.append(transaction)


def get_single_address(address):
    # API call to get all info from a single address
    jobcoin_api_url = config.API_ADDRESS_URL + '/' + address
    response = requests.get(jobcoin_api_url)

    if response and response.content:
        response = response.json()
        balance = response['balance']

        if balance == 0:
            return None

        transactions = []
        for item in response['transactions']:
            amount = item['amount']
            timestamp = item['timestamp']
            to_address = item['toAddress']
            from_address = item['fromAddress'] if 'fromAddress' in item else None

            transaction = Transaction(amount, timestamp, to_address, from_address)
            transactions.append(transaction)

        address = Address(address, balance, transactions)
        return address

    return None


def transfer_coins(from_address, to_address, amount, time_delay=0):
    # Used to transfer coins between two addresses
    time.sleep(time_delay)
    jobcoin_api_url = config.API_TRANSACTIONS_URL
    body = {
        'fromAddress': from_address,
        'toAddress': to_address,
        'amount': amount
    }

    response = requests.post(jobcoin_api_url, body)

    if response.status_code == 200:
        return True
    else:
        # TODO: This designates failure. But what if the API is down? What if its insufficient funds? Needs updating.
        return False


def create_coins(to_address, amount):
    # Used only to create coins for testing purposes.
    jobcoin_api_url = config.API_TRANSACTIONS_URL
    body = {
        'toAddress': to_address,
        'amount': amount
    }

    response = requests.post(jobcoin_api_url, body)

    return True if response.status_code == 200 else False
