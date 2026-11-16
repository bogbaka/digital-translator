
def withdraw_cash():
    correct_pin = "1234"
    account_balance = 50000
    atm_cash = 30000
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == correct_pin:
            print("PIN verified successfully!")
            break

        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempt(s) remaining.")

    else:
        print("Too many incorrect attempts. Card blocked.")
        return

    try:
        withdrawal_amount = float(input("Enter withdrawal amount: ₦"))

    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return

    if withdrawal_amount <= 0:
        print("Invalid withdrawal amount.")
        return

    if withdrawal_amount > account_balance:
        print("Insufficient account balance.")
        return

    if withdrawal_amount > atm_cash:
        print("Sorry, the ATM has insufficient cash.")
        return

    account_balance -= withdrawal_amount
    atm_cash -= withdrawal_amount

    print("\nTransaction successful!")
    print(f"Please collect your ₦{withdrawal_amount:,.2f}")
    print(f"Remaining account balance: ₦{account_balance:,.2f}")
    print(f"Remaining ATM cash: ₦{atm_cash:,.2f}")


if __name__ == "__main__":
    withdraw_cash()
