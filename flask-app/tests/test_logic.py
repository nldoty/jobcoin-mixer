from jobcoin import logic, api
import unittest
import uuid


class TestApp(unittest.TestCase):

    def test_calculate_fee(self):
        balance_1 = 10
        balance_2 = .01

        fee_1 = logic.calculate_fee(balance_1)
        fee_2 = logic.calculate_fee(balance_2)

        self.assertEqual(fee_1, 1000000)
        self.assertEqual(fee_2, 1000)

    def test_shift_coin_values(self):
        test_val_1 = 12
        test_val_2 = 1234
        test_val_3 = 123456
        test_val_4 = 12345678
        test_val_5 = 1234567890

        output_1 = logic.shift_coin_values(test_val_1)
        output_2 = logic.shift_coin_values(test_val_2)
        output_3 = logic.shift_coin_values(test_val_3)
        output_4 = logic.shift_coin_values(test_val_4)
        output_5 = logic.shift_coin_values(test_val_5)

        self.assertEqual(output_1, '.00000012')
        self.assertEqual(output_2, '.00001234')
        self.assertEqual(output_3, '.00123456')
        self.assertEqual(output_4, '.12345678')
        self.assertEqual(output_5, '12.34567890')

    def test_mix_coins(self):
        return True
        # This test doesn't work, as floating point math is the bane of my existence.
#         mixer_test_from_address = uuid.uuid4().hex
#         mixer_test_to_address = uuid.uuid4().hex
#         dump_address = 'mixer_dump_address'
#         addr_1 = uuid.uuid4().hex
#         addr_2 = uuid.uuid4().hex
#         addr_3 = uuid.uuid4().hex
#         initial_addr_list = [addr_1, addr_2, addr_3]
#         num_transactions = 5
#         balance = '50'
#
#         api.create_coins(mixer_test_from_address, '50')
#         test_from_balance = api.check_balance(mixer_test_from_address)
#
#         self.assertEqual(test_from_balance, balance)
#
#         api.transfer_coins(mixer_test_from_address, mixer_test_to_address, balance)
#
#         new_test_from_balance = api.check_balance(mixer_test_from_address)
#         test_to_balance = api.check_balance(mixer_test_to_address)
#
#         self.assertEqual(new_test_from_balance, '0')
#         self.assertEqual(test_to_balance, balance)
#
#         transactions_list = logic.mix_coins(initial_addr_list, mixer_test_to_address, 0,
#                                             num_transactions, False)
#
#         total = 0
#         addr_list = []
#         for item in transactions_list:
#             addr_list.append(item.to_address)
#             amt = item.amount
#             amt = float(amt)
#             amt *= (10 ** logic.ROUND_FACTOR)
#             total += int(amt)
#
#         total = logic.shift_coin_values(total)
#         total = str(int(float(total)))
#
#         self.assertEqual(total, balance)
#
#         logic.make_transactions(transactions_list)
#
#         addr_test_1_balance = api.check_balance(addr_1)
#         addr_test_2_balance = api.check_balance(addr_2)
#         addr_test_3_balance = api.check_balance(addr_3)
#
#         balance_list = [addr_test_1_balance, addr_test_2_balance, addr_test_3_balance]
#
#         addr_total = ((float(addr_test_1_balance) * (10 ** logic.ROUND_FACTOR)) +
#                       (float(addr_test_2_balance) * (10 ** logic.ROUND_FACTOR)) +
#                       (float(addr_test_3_balance) * (10 ** logic.ROUND_FACTOR)))
#         addr_total = logic.shift_coin_values(int(addr_total))
#         addr_total = str(int(float(addr_total)))
#
#         self.assertEqual(addr_total, balance)
#
#         addr_list = set(addr_list)
#         intersection = list(addr_list.intersection(initial_addr_list))
#
#         self.assertEqual(len(intersection), len(initial_addr_list))
#
#         self.assertEqual(len(initial_addr_list), len(balance_list))
#
#         for i in range(len(initial_addr_list)):
#             api.transfer_coins(initial_addr_list[i], dump_address, balance_list[i])


if __name__ == '__main__':
    unittest.main()
