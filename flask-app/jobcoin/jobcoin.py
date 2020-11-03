import json
import decimal
from random import choice, randint, uniform
from . import api
from . import config
from .coin_classes import Transaction

ROUND_FACTOR = 8


def mix_coins(address_list, mixer_address, transactions=None):
    # Main function for mixing a users coins.

    # Checks if coins have been added to the mixer's unique address.
    amount_coins_added = api.check_balance(mixer_address)
    if not amount_coins_added:
        return False

    api.transfer_coins(mixer_address, config.MIXER_POOL_ADDRESS, amount_coins_added)
    num_addresses = len(address_list)
    num_transactions = randint(num_addresses, 4 * num_addresses) if not transactions else int(transactions)
    print("Number of transactions:" + str(num_transactions))

    # Creates random amounts of coins to be sent, with random addresses to send them to.
    coin_amounts_list = randomize_coins(num_transactions, amount_coins_added)
    addresses_list = randomize_addresses(num_transactions, address_list)

    assert len(coin_amounts_list) == len(address_list)

    transactions_list = []
    for i in range(num_transactions):
        transaction = Transaction(coin_amounts_list[i], None, addresses_list[i], config.MIXER_POOL_ADDRESS)
        transactions_list.append(transaction)

    return transactions_list


def make_transactions(transactions_list):
    for transaction in transactions_list:
        amount = transaction.amount
        to_address = transaction.to_address
        from_address = transaction.from_address
        api.transfer_coins(from_address, to_address, amount)


def convert_transactions_list_to_json(transactions_list):
    json_list = []

    for item in transactions_list:
        to_address = item.to_address
        amount = item.amount
        str = to_address + ": " + amount + " coins"
        json_list.append(str)

    return {
        'transactions': json_list
    }


def randomize_addresses(num_addresses, addresses):
    new_address_list = addresses

    for i in range(len(addresses), num_addresses):
        tmp_address = choice(addresses)
        new_address_list.append(tmp_address)

    print("Sorting addresses. Length of addresses: " + str(len(new_address_list)))
    new_address_list = shuffle(new_address_list)
    return new_address_list


def randomize_coins(num_buckets, balance):
    bucket_dist = []
    buckets = []
    sum = 0
    for i in range(num_buckets-1):
        # This is here because doing floating point math on financial transactions can cause precision issues.
        # Instead, I round to a fixed amount, then multiply by the fixed amount to achieve an integer.
        # Later, once the math is done, I convert to a str and add a decimal place in, so no rounding errors take place.
        tmp = round(uniform(0, int(balance)), ROUND_FACTOR)

        tmp *= (10 ** ROUND_FACTOR)
        bucket_dist.append(int(tmp))

    bucket_dist.append(int(balance) * (10 ** ROUND_FACTOR))
    bucket_dist.append(int(0))
    bucket_dist.sort()

    for i in range(1, len(bucket_dist)):
        tmp = int(bucket_dist[i] - bucket_dist[i-1])
        sum += tmp
        tmp = str(tmp)
        tmp = tmp.zfill(8)
        tmp = tmp[:-ROUND_FACTOR] + "." + tmp[-ROUND_FACTOR:]
        buckets.append(tmp)

    print("TOTAL: " + str(sum/(10**ROUND_FACTOR)))

    return buckets


def shuffle(items):
    print("items: " + ' '.join(map(str, items)))
    # Fisher-Yates shuffle
    n = len(items)
    for i in range(n-1, 0, -1):
        j = randint(0, i)
        items[i], items[j] = items[j], items[i]
    return items
