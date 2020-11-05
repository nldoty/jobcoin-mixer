import math
from random import choice, randint, uniform
from . import api
from . import config
from .coin_classes import Transaction

ROUND_FACTOR = 8
FEE_PCT = .001


def mix_coins(address_list, mixer_address, timeout=None, transactions=None, fee=False):
    # Main function for mixing a users coins.

    # Checks if coins have been added to the mixer's unique address.
    amount_coins_added = api.check_balance(mixer_address)
    if not amount_coins_added:
        return False

    # Transfers coins from the unique address to the mixer, then
    api.transfer_coins(mixer_address, config.MIXER_POOL_ADDRESS, amount_coins_added)
    num_addresses = len(address_list)
    num_transactions = randint(num_addresses, 4 * num_addresses) if not transactions else int(transactions)

    # Creates random amounts of coins to be sent, with random addresses to send them to.
    coin_amounts_list = randomize_coins(num_transactions, amount_coins_added, fee)
    addresses_list = randomize_addresses(num_transactions, address_list)

    # Creates a random list of timeouts
    timeouts = randomize_timeouts(num_transactions, timeout)

    # Checks that the number of coin dividends is the same as the number of addresses to send to.
    assert len(coin_amounts_list) == len(addresses_list)

    # Creates the list of transactions
    transactions_list = []
    for i in range(num_transactions):
        transaction = Transaction(coin_amounts_list[i], None, addresses_list[i], config.MIXER_POOL_ADDRESS, timeouts[i])
        transactions_list.append(transaction)

    # Adds the fee to the transaction
    if fee:
        fee_amt = calculate_fee(amount_coins_added)
        fee_amt = shift_coin_values(fee_amt)
        fee_transaction = Transaction(str(fee_amt), None, config.MIXER_FEE_ADDRESS, config.MIXER_POOL_ADDRESS, 0)
        transactions_list.append(fee_transaction)

    return transactions_list


def make_transactions(transactions_list):
    # Completes the transaction from one address to another
    for transaction in transactions_list:
        amount = transaction.amount
        to_address = transaction.to_address
        from_address = transaction.from_address
        time_delay = transaction.time_delay
        api.transfer_coins(from_address, to_address, amount, time_delay)


def convert_transactions_list_to_json(transactions_list):
    # Creates JSON to send back to the web app, to display transactions.
    json_list = []

    for item in transactions_list:
        to_address = 'MIXER FEE' if item.to_address == config.MIXER_FEE_ADDRESS else item.to_address
        amount = item.amount
        output_str = to_address + ": " + amount + " coins"
        json_list.append(output_str)

    return {
        'transactions': json_list
    }


def randomize_addresses(num_transactions, addresses):
    # Takes a list of addresses and randomizes them
    # This was a fun bug to discover.
    new_address_list = addresses[:]

    for i in range(len(addresses), num_transactions):
        tmp_address = choice(addresses)
        new_address_list.append(tmp_address)

    new_address_list = shuffle(new_address_list)
    return new_address_list


def randomize_timeouts(num_addresses, timeout):
    # Takes the max timeout and randomizes them
    new_timeout_list = []
    if timeout:
        timeout = int(timeout)
        for i in range(num_addresses):
            new_timeout_list.append(randint(0, timeout))
    else:
        new_timeout_list = [0] * num_addresses

    return new_timeout_list


def randomize_coins(num_buckets, balance, fee):
    # Creates random amounts of coins to send to the addresses.
    bucket_dist = []
    buckets = []
    sum = 0
    for i in range(num_buckets-1):
        # This is here because doing floating point math on financial transactions can cause precision issues.
        # Instead, I round to a fixed amount, then multiply by the fixed amount to achieve an integer.
        # Later, once the math is done, I convert to a str and add a decimal place in, so no rounding errors take place.
        tmp = round(uniform(0, float(balance)), ROUND_FACTOR)

        tmp *= (10 ** ROUND_FACTOR)
        bucket_dist.append(int(tmp))

    if fee:
        fee_amt = calculate_fee(balance)
        top_bucket = int(float(balance) * (10 ** ROUND_FACTOR)) - fee_amt
        bucket_dist.append(top_bucket)
    else:
        bucket_dist.append(int(float(balance) * (10 ** ROUND_FACTOR)))

    bucket_dist.append(int(0))
    bucket_dist.sort()

    for i in range(1, len(bucket_dist)):
        tmp = int(bucket_dist[i] - bucket_dist[i-1])
        sum += tmp
        tmp = shift_coin_values(tmp)
        buckets.append(tmp)

    return buckets


def shift_coin_values(value):
    # This exists because after doing my integer math I need to put decimal places in my equations.
    # Doing so could cause me to have more floating point errors - so I do it as a string.

    value = str(value)
    value = value.zfill(8)
    value = value[:-ROUND_FACTOR] + "." + value[-ROUND_FACTOR:]

    return value


def shuffle(items):
    # Fisher-Yates shuffle
    n = len(items)
    for i in range(n-1, 0, -1):
        j = randint(0, i)
        items[i], items[j] = items[j], items[i]
    return items


def calculate_fee(balance):
    # Used for calculating a mixer fee. I don't really plan on using this.
    balance = round(float(balance), ROUND_FACTOR)
    balance *= (10 ** ROUND_FACTOR)

    fee = math.floor(int(balance) * FEE_PCT)

    return fee
