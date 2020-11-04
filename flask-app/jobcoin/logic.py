import math
from random import choice, randint, uniform
from . import api
from . import config
from .coin_classes import Transaction

ROUND_FACTOR = 8
FEE_PCT = .001


def mix_coins(address_list, mixer_address, transactions=None, fee=False):
    # Main function for mixing a users coins.

    # Checks if coins have been added to the mixer's unique address.
    amount_coins_added = api.check_balance(mixer_address)
    if not amount_coins_added:
        return False

    api.transfer_coins(mixer_address, config.MIXER_POOL_ADDRESS, amount_coins_added)
    num_addresses = len(address_list)
    num_transactions = randint(num_addresses, 4 * num_addresses) if not transactions else int(transactions)

    # Creates random amounts of coins to be sent, with random addresses to send them to.
    coin_amounts_list = randomize_coins(num_transactions, amount_coins_added, fee)
    addresses_list = randomize_addresses(num_transactions, address_list)

    assert len(coin_amounts_list) == len(address_list)

    transactions_list = []
    for i in range(num_transactions):
        transaction = Transaction(coin_amounts_list[i], None, addresses_list[i], config.MIXER_POOL_ADDRESS)
        transactions_list.append(transaction)

    if fee:
        fee_amt = calculate_fee(amount_coins_added)
        fee_amt = shift_coin_values(fee_amt)
        fee_transaction = Transaction(str(fee_amt), None, config.MIXER_FEE_ADDRESS, config.MIXER_POOL_ADDRESS)
        transactions_list.append(fee_transaction)

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
        to_address = 'MIXER FEE' if item.to_address == config.MIXER_FEE_ADDRESS else item.to_address
        amount = item.amount
        output_str = to_address + ": " + amount + " coins"
        json_list.append(output_str)

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


def randomize_coins(num_buckets, balance, fee):
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

    if fee:
        fee_amt = calculate_fee(balance)
        top_bucket = (int(balance) * (10 ** ROUND_FACTOR)) - fee_amt
        bucket_dist.append(top_bucket)
    else:
        bucket_dist.append(int(balance) * (10 ** ROUND_FACTOR))

    bucket_dist.append(int(0))
    bucket_dist.sort()

    for i in range(1, len(bucket_dist)):
        tmp = int(bucket_dist[i] - bucket_dist[i-1])
        sum += tmp
        tmp = shift_coin_values(tmp)
        buckets.append(tmp)

    print("TOTAL: " + str(sum/(10**ROUND_FACTOR)))

    return buckets


def shift_coin_values(value):
    # This exists because after doing my integer math I need to put decimal places in my equations.
    # Doing so could cause me to have more floating point errors - so I do it as a string.

    value = str(value)
    value = value.zfill(8)
    value = value[:-ROUND_FACTOR] + "." + value[-ROUND_FACTOR:]

    return value


def shuffle(items):
    print("items: " + ' '.join(map(str, items)))
    # Fisher-Yates shuffle
    n = len(items)
    for i in range(n-1, 0, -1):
        j = randint(0, i)
        items[i], items[j] = items[j], items[i]
    return items


def calculate_fee(balance):
    # Used for calculating a mixer fee. I don't really plan on using this.
    balance = round(balance, ROUND_FACTOR)
    balance *= (10 ** ROUND_FACTOR)

    fee = math.floor(balance * FEE_PCT)

    return fee
