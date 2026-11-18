
"""Main entry point for The Digital Translator."""

from breakfast import show_breakfast_instructions
from atm import withdraw_cash
from calculator import run_calculator
from data_translator import translate_customer_data
from online_store import place_order


APP_TITLE = "THE DIGITAL TRANSLATOR"
APP_DESCRIPTION = "Your All-in-One Python Utility Suite"
SEPARATOR = "=" * 52


def display_welcome() -> None:
    """Display the application welcome screen."""
    print(f"\n{SEPARATOR}")
    print(f"{APP_TITLE:^52}")
    print(f"{APP_DESCRIPTION:^52}")
    print(SEPARATOR)


def display_menu() -> None:
    """Display the available application features."""
    print("\nMAIN MENU")
    print("-" * 52)
    print("1. Breakfast Instructions")
    print("2. ATM Simulator")
    print("3. Digital Calculator")
    print("4. Data Translator")
    print("5. Online Store")
    print("6. Exit")
    print("-" * 52)


def get_menu_choice() -> str:
    """Get the user's menu selection."""
    return input("Select an option (1-6): ").strip()


def main() -> None:
    """Run the main application menu."""
    display_welcome()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            show_breakfast_instructions()

        elif choice == "2":
            withdraw_cash()

        elif choice == "3":
            run_calculator()

        elif choice == "4":
            translate_customer_data()

        elif choice == "5":
            place_order()

        elif choice == "6":
            print("\nThank you for using The Digital Translator!")
            print("Goodbye!")
            break

        else:
            print(
                "\nInvalid selection. "
                "Please enter a number between 1 and 6."
            )


def run_application() -> None:
    """Run the application and handle unexpected interruptions."""
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")
    except EOFError:
        print("\n\nInput stream closed. Goodbye!")


if __name__ == "__main__":
    run_application()