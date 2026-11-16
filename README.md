# Py-SECTION 1 MISSION PROJECT — THE DIGITAL TRANSLATOR

**Mission:** Mission 03
**Squad:** Solo 380
**Language:** Python
**Python Version:** 3.8+

## Project Overview

The Digital Translator is a beginner-friendly Python project that demonstrates how real-world tasks can be translated into executable instructions and programs.

The project contains five tiers covering basic instructions, decision-making, calculations, data types, user input, validation, and data storage.

## Project Features

### Tier 1 — Literal Assistant: Breakfast Instructions
- Displays clear, step-by-step breakfast preparation instructions.
- Demonstrates how everyday tasks can be translated into executable instructions.

### Tier 2 — ATM Simulator
- Verifies a customer's PIN.
- Allows up to three PIN attempts.
- Validates withdrawal amounts.
- Checks account balance and available ATM cash.
- Updates balances after successful withdrawals.

### Tier 3 — Digital Calculator
- Supports addition, subtraction, multiplication, and division.
- Handles invalid numeric input.
- Prevents division by zero.
- Displays calculation results.

### Tier 4 — Data Translator
- Demonstrates Python's four basic data types:
  - `str` — String
  - `int` — Integer
  - `float` — Floating-point number
  - `bool` — Boolean

### Tier 5 — Digital Online Store
- Collects customer and delivery information.
- Displays available products and prices.
- Validates product selection and quantity.
- Calculates order totals.
- Saves orders in a JSON file.
- Preserves previously saved orders.

## Project Structure

```text
mission-03/
│
├── main.py
├── breakfast.py
├── atm.py
├── calculator.py
├── data_translator.py
├── online_store.py
├── README.md
├── .gitignore
│
└── tests/
    ├── __init__.py
    ├── test_breakfast.py
    ├── test_atm.py
    ├── test_calculator.py
    ├── test_data_translator.py
    └── test_online_store.py
```

`orders.json` is generated automatically when orders are placed. It is excluded from version control because it contains runtime order records.

## Requirements

- Python 3.8 or later.
- No third-party Python packages are required.

The project uses Python's built-in libraries.

## How to Run the Project

1. Clone the repository.
2. Open the project directory.
3. Run the main application:

```bash
python3 main.py
```

4. Select an option from the main menu to explore the five tiers.

## Running the Automated Tests

The project includes automated tests using Python's built-in `unittest` framework.

Run all tests:

```bash
python3 -m unittest discover -s tests -v
```

Run an individual test module:

```bash
python3 -m unittest tests.test_calculator -v
```

## Test Results

All five tiers have automated tests.

**Total automated tests: 30**

**Result: 30 passed, 0 failed.**

## Important Notes

- The ATM is an educational simulation, not a real banking system. Its PIN and balances are defined in the program.
- The online store saves order records locally in `orders.json`.
- This project is intended for Python learning and demonstration purposes.

## Author

**Blessing Ogbaka Onyemowo**

## Mission Objective

To demonstrate the ability to translate real-world instructions and processes into working Python programs using fundamental programming concepts.