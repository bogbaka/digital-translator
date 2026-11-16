
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

from calculator import run_calculator


class TestCalculator(unittest.TestCase):

    def run_calculation(self, inputs):
        output = StringIO()

        with patch("builtins.input", side_effect=inputs):
            with redirect_stdout(output):
                run_calculator()

        return output.getvalue()

    def test_addition(self):
        result = self.run_calculation(["20", "5", "1"])
        self.assertIn("Result: 25.0", result)

    def test_subtraction(self):
        result = self.run_calculation(["20", "5", "2"])
        self.assertIn("Result: 15.0", result)

    def test_multiplication(self):
        result = self.run_calculation(["20", "5", "3"])
        self.assertIn("Result: 100.0", result)

    def test_division(self):
        result = self.run_calculation(["20", "5", "4"])
        self.assertIn("Result: 4.0", result)

    def test_division_by_zero(self):
        result = self.run_calculation(["20", "0", "4"])
        self.assertIn("Division by zero is not allowed", result)

    def test_invalid_number(self):
        result = self.run_calculation(["Hello"])
        self.assertIn("Please enter valid numbers", result)

    def test_invalid_operation(self):
        result = self.run_calculation(["20", "5", "9"])
        self.assertIn("Invalid operation selected", result)

    def test_operation_with_extra_spaces(self):
        result = self.run_calculation(["20", "5", " 1 "])
        self.assertIn("Result: 25.0", result)


if __name__ == "__main__":
    unittest.main()
