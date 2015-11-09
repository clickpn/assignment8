import unittest
from unittest import TestCase
import Investment_account
# DS-GA 1007
# HW8
# Author: Sida Ye
# test file

"""tests for hw8"""

class hw8_unittest(unittest.TestCase):

    def setUp(self):
        pass


    def test_investment_acct1(self):
    	a = Investment_account.Investment_account(1000)
        self.assertEqual(a.purchase_value, 1000)


    def test_investment_acct2(self):
        with self.assertRaises(ValueError) as cm:
            Investment_account.Investment_account(-1)
        the_exception = cm.exception
        self.assertEquals(str(the_exception), 'Value must be greater than 0!')


if __name__ == '__main__':
    unittest.main()
