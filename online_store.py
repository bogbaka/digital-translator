
import json


def place_order():
    print("\n===== DIGITAL ONLINE STORE =====")

    products = {
        "1": {"name": "Shoes", "price": 50000},
        "2": {"name": "Bags", "price": 25000},
        "3": {"name": "Watches", "price": 15000}
    }

    customer_name = input("Enter your name: ").strip()
    delivery_address = input("Enter your delivery address: ").strip()

    if not customer_name or not delivery_address:
        print("Customer name and delivery address are required.")
        return

    print("\nAVAILABLE PRODUCTS")

    for number, product in products.items():
        print(f"{number}. {product['name']} - ₦{product['price']:,.2f}")

    choice = input("\nSelect a product (1-3): ").strip()

    if choice not in products:
        print("Invalid product selection.")
        return

    quantity_text = input("Enter quantity: ")

    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    selected_product = products[choice]
    total_amount = selected_product["price"] * quantity

    order = {
        "customer_name": customer_name,
        "delivery_address": delivery_address,
        "product": selected_product["name"],
        "quantity": quantity,
        "total_amount": total_amount,
        "status": "Pending"
    }

    try:
        with open("orders.json", "r", encoding="utf-8") as file:
            orders = json.load(file)

    except FileNotFoundError:
        orders = []

    except json.JSONDecodeError:
        print("Error: The existing orders file contains invalid JSON.")
        return

    orders.append(order)

    with open("orders.json", "w", encoding="utf-8") as file:
        json.dump(orders, file, indent=4)

    print("\n===== ORDER SUMMARY =====")
    print(f"Customer: {customer_name}")
    print(f"Product: {selected_product['name']}")
    print(f"Quantity: {quantity}")
    print(f"Delivery address: {delivery_address}")
    print(f"Total amount: ₦{total_amount:,.2f}")
    print("Order placed successfully!")
    print("Order saved successfully!")


if __name__ == "__main__":
    place_order()
