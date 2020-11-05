class Transaction:

    def __init__(self, amount, time_stamp, to_address, from_address, time_delay=0):
        self.amount = amount
        self.time_stamp = time_stamp
        self.to_address = to_address
        self.from_address = from_address
        self.time_delay = time_delay

    def print(self):
        # Used for debugging purposes
        print('Amount: ' + self.amount)
        print('Time stamp: ' + self.time_stamp)
        print('To address: ' + self.to_address)
        if self.from_address:
            print('From address: ' + self.from_address)
        else:
            print('Transaction originated from Jobcoin API.')
        print('Time delay: ' + str(self.time_delay))


class Address:

    def __init__(self, address, balance, transactions):
        self.address = address
        self.balance = balance
        self.transactions = transactions

    def print(self):
        # Used for debugging purposes
        print('Address: ' + self.address)
        print('Balance: ' + self.balance)
        for transaction in self.transactions:
            transaction.print()
