
def run_calculator():
    print("\n===== DIGITAL CALCULATOR =====")

    # Get the two numbers from the user.
    try:
        number_1 = float(input("Enter the first number: "))
        number_2 = float(input("Enter the second number: "))

    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    # Display the available operations.
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ").strip()

    # Perform the selected operation.
    if choice == "1":
        result = number_1 + number_2
        operation = "Addition"

    elif choice == "2":
        result = number_1 - number_2
        operation = "Subtraction"

    elif choice == "3":
        result = number_1 * number_2
        operation = "Multiplication"

    elif choice == "4":
        if number_2 == 0:
            print("Error: Division by zero is not allowed.")
            return

        result = number_1 / number_2
        operation = "Division"

    else:
        print("Invalid operation selected.")
        return

    # Display the calculation result.
    print(f"\nOperation: {operation}")
    print(f"Result: {result}")


if __name__ == "__main__":
    run_calculator()
