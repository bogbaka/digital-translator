
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

from atm import withdraw_cash


class TestATM(unittest.TestCase):

    def run_atm(self, inputs):
        output = StringIO()

        with patch("builtins.input", side_effect=inputs):
            with redirect_stdout(output):
                withdraw_cash()

        return output.getvalue()

    def test_successful_withdrawal(self):
        result = self.run_atm(["1234", "20000"])

        self.assertIn("Transaction successful!", result)
        self.assertIn("Remaining account balance: ₦30,000.00", result)
        self.assertIn("Remaining ATM cash: ₦10,000.00", result)

    def test_incorrect_pin_blocks_card(self):
        result = self.run_atm(["1111", "2222", "3333"])

        self.assertIn("Too many incorrect attempts. Card blocked.", result)

    def test_invalid_withdrawal_input(self):
        result = self.run_atm(["1234", "Hello"])

        self.assertIn("Invalid input. Please enter a valid amount.", result)

    def test_zero_withdrawal_amount(self):
        result = self.run_atm(["1234", "0"])

        self.assertIn("Invalid withdrawal amount.", result)

    def test_negative_withdrawal_amount(self):
        result = self.run_atm(["1234", "-5000"])

        self.assertIn("Invalid withdrawal amount.", result)

    def test_insufficient_account_balance(self):
        result = self.run_atm(["1234", "60000"])

        self.assertIn("Insufficient account balance.", result)

    def test_insufficient_atm_cash(self):
        result = self.run_atm(["1234", "40000"])

        self.assertIn("Sorry, the ATM has insufficient cash.", result)


if __name__ == "__main__":
    unittest.main()
