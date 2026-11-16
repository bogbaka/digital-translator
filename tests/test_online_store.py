
import unittest
import json
import os
import tempfile

from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

from online_store import place_order


class TestOnlineStore(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_directory = os.getcwd()
        os.chdir(self.temp_dir.name)

    def tearDown(self):
        os.chdir(self.original_directory)
        self.temp_dir.cleanup()

    def run_store(self, inputs):
        output = StringIO()

        with patch("builtins.input", side_effect=inputs):
            with redirect_stdout(output):
                place_order()

        return output.getvalue()

    def test_successful_order(self):
        result = self.run_store([
            "Blessing",
            "Otukpo, Benue State",
            "1",
            "2"
        ])

        self.assertIn("Order placed successfully!", result)
        self.assertIn("Total amount: ₦100,000.00", result)

    def test_order_is_saved_to_json(self):
        self.run_store([
            "Blessing",
            "Otukpo, Benue State",
            "1",
            "2"
        ])

        with open("orders.json", "r", encoding="utf-8") as file:
            orders = json.load(file)

        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["customer_name"], "Blessing")
        self.assertEqual(orders[0]["product"], "Shoes")
        self.assertEqual(orders[0]["quantity"], 2)
        self.assertEqual(orders[0]["total_amount"], 100000)

    def test_multiple_orders_are_saved(self):
        self.run_store([
            "Blessing",
            "Otukpo",
            "1",
            "2"
        ])

        self.run_store([
            "Abraham",
            "Makurdi",
            "2",
            "2"
        ])

        with open("orders.json", "r", encoding="utf-8") as file:
            orders = json.load(file)

        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0]["customer_name"], "Blessing")
        self.assertEqual(orders[1]["customer_name"], "Abraham")

    def test_empty_customer_details_are_rejected(self):
        result = self.run_store([
            "",
            "Otukpo"
        ])

        self.assertIn(
            "Customer name and delivery address are required.",
            result
        )

    def test_invalid_product_selection(self):
        result = self.run_store([
            "Blessing",
            "Otukpo",
            "9"
        ])

        self.assertIn("Invalid product selection.", result)

    def test_invalid_quantity(self):
        result = self.run_store([
            "Blessing",
            "Otukpo",
            "1",
            "Hello"
        ])

        self.assertIn(
            "Invalid quantity. Please enter a whole number.",
            result
        )

    def test_zero_quantity_is_rejected(self):
        result = self.run_store([
            "Blessing",
            "Otukpo",
            "1",
            "0"
        ])

        self.assertIn("Quantity must be greater than zero.", result)


if __name__ == "__main__":
    unittest.main()
