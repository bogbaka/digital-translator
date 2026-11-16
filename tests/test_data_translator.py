
import unittest
from io import StringIO
from contextlib import redirect_stdout

from data_translator import translate_customer_data


class TestDataTranslator(unittest.TestCase):

    def get_customer_data(self):
        output = StringIO()

        with redirect_stdout(output):
            translate_customer_data()

        return output.getvalue()

    def test_customer_name_is_displayed_as_string(self):
        result = self.get_customer_data()

        self.assertIn("Name: Victor", result)
        self.assertIn("Data type: str", result)

    def test_customer_age_is_displayed_as_integer(self):
        result = self.get_customer_data()

        self.assertIn("Age: 30", result)
        self.assertIn("Data type: int", result)

    def test_account_balance_is_displayed_as_float(self):
        result = self.get_customer_data()

        self.assertIn("Account balance: ₦150,000.50", result)
        self.assertIn("Data type: float", result)

    def test_account_status_is_displayed_as_boolean(self):
        result = self.get_customer_data()

        self.assertIn("Account active: True", result)
        self.assertIn("Data type: bool", result)


if __name__ == "__main__":
    unittest.main()
