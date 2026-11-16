
def translate_customer_data():
    print("\n===== DIGITAL DATA TRANSLATOR =====")

    customer_name = "Victor"
    customer_age = 30
    account_balance = 150000.50
    account_active = True

    print("\nCUSTOMER INFORMATION")

    print(f"Name: {customer_name}")
    print(f"Data type: {type(customer_name).__name__}")

    print(f"\nAge: {customer_age}")
    print(f"Data type: {type(customer_age).__name__}")

    print(f"\nAccount balance: ₦{account_balance:,.2f}")
    print(f"Data type: {type(account_balance).__name__}")

    print(f"\nAccount active: {account_active}")
    print(f"Data type: {type(account_active).__name__}")


if __name__ == "__main__":
    translate_customer_data()
