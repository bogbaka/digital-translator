
import unittest
from io import StringIO
from contextlib import redirect_stdout

from breakfast import show_breakfast_instructions


class TestBreakfast(unittest.TestCase):

    def get_instructions(self):
        output = StringIO()

        with redirect_stdout(output):
            show_breakfast_instructions()

        return output.getvalue()

    def test_breakfast_title_is_displayed(self):
        result = self.get_instructions()

        self.assertIn("BREAKFAST INSTRUCTIONS", result)

    def test_ingredients_are_displayed(self):
        result = self.get_instructions()

        self.assertIn("two eggs", result)
        self.assertIn("two slices of bread", result)

    def test_preparation_steps_are_displayed(self):
        result = self.get_instructions()

        self.assertIn("Crack the eggs into a clean bowl.", result)
        self.assertIn("Toast the bread.", result)
        self.assertIn("Serve the breakfast on a clean plate.", result)

    def test_completion_message_is_displayed(self):
        result = self.get_instructions()

        self.assertIn(
            "Breakfast preparation instructions completed.",
            result
        )


if __name__ == "__main__":
    unittest.main()
