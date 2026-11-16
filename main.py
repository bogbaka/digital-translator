
from breakfast import show_breakfast_instructions
from atm import withdraw_cash
from calculator import run_calculator
from data_translator import translate_customer_data
from online_store import place_order


def main():
    while True:
        print("\n================================")
        print("       THE DIGITAL TRANSLATOR")
        print("================================")
        print("1. Breakfast Instructions")
        print("2. ATM Simulator")
        print("3. Digital Calculator")
        print("4. Data Translator")
        print("5. Online Store")
        print("6. Exit")
        print("================================")

        choice = input("Select an option (1-6): ").strip()

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
            print("Thank you for using The Digital Translator!")
            break

        else:
            print("Invalid selection. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
