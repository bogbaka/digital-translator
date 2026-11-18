
"""Tests for the main Digital Translator application."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import main


class TestMainMenu(unittest.TestCase):

    def test_welcome_screen_displays_application_title(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main.display_welcome()

        self.assertIn("THE DIGITAL TRANSLATOR", output.getvalue())
        self.assertIn(
            "Your All-in-One Python Utility Suite",
            output.getvalue()
        )

    def test_menu_displays_all_six_options(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main.display_menu()

        for option in [
            "Breakfast Instructions",
            "ATM Simulator",
            "Digital Calculator",
            "Data Translator",
            "Online Store",
            "Exit",
        ]:
            self.assertIn(option, output.getvalue())

    @patch("builtins.input", return_value=" 3 ")
    def test_menu_choice_removes_extra_spaces(self, mock_input):
        choice = main.get_menu_choice()

        self.assertEqual(choice, "3")
        mock_input.assert_called_once()

    @patch("main.show_breakfast_instructions")
    @patch("main.withdraw_cash")
    @patch("main.run_calculator")
    @patch("main.translate_customer_data")
    @patch("main.place_order")
    @patch("builtins.input", side_effect=["1", "2", "3", "4", "5", "6"])
    def test_menu_calls_all_five_modules(
        self,
        mock_input,
        mock_place_order,
        mock_translate,
        mock_calculator,
        mock_atm,
        mock_breakfast,
    ):
        with redirect_stdout(io.StringIO()):
            main.main()

        mock_breakfast.assert_called_once()
        mock_atm.assert_called_once()
        mock_calculator.assert_called_once()
        mock_translate.assert_called_once()
        mock_place_order.assert_called_once()

    @patch("builtins.input", side_effect=["9", "6"])
    def test_invalid_selection_displays_error(self, mock_input):
        output = io.StringIO()

        with redirect_stdout(output):
            main.main()

        self.assertIn("Invalid selection", output.getvalue())

    @patch("builtins.input", return_value="6")
    def test_exit_displays_goodbye_message(self, mock_input):
        output = io.StringIO()

        with redirect_stdout(output):
            main.main()

        self.assertIn(
            "Thank you for using The Digital Translator!",
            output.getvalue()
        )
        self.assertIn("Goodbye!", output.getvalue())

    @patch("main.main", side_effect=KeyboardInterrupt)
    def test_keyboard_interrupt_displays_message(self, mock_main):
        output = io.StringIO()

        with redirect_stdout(output):
            main.run_application()

        self.assertIn(
            "Application interrupted. Goodbye!",
            output.getvalue()
        )
        mock_main.assert_called_once()

    @patch("main.main", side_effect=EOFError)
    def test_eof_error_displays_message(self, mock_main):
        output = io.StringIO()

        with redirect_stdout(output):
            main.run_application()

        self.assertIn(
            "Input stream closed. Goodbye!",
            output.getvalue()
        )
        mock_main.assert_called_once()

if __name__ == "__main__":
    unittest.main()
