from jobcoin import logic
import unittest


class TestLogic(unittest.TestCase):

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
        mixer_test_from_address = 'mixer_test_from_address'
        mixer_test_pool_address = 'mixer_test_pool_address'
        mixer_test_to_address = 'mixer_test_to_address'

        transactions_list = logic.mix(['mix_test_1', 'mix_test_2', 'mix_test_3'],

        )


if __name__ == '__main__':
    unittest.main()