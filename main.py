from menu import MENU
from order import Order


def main():

    order = Order()

    print("QUICKBITE MENU")

    for item in MENU:
        print(
            f"{item.number}. "
            f"{item.name} - "
            f"₱{item.price:.2f}"
        )

    while True:

        choice = int(input("Enter item number: "))

        quantity = int(input("Enter quantity: "))

        menu_item = None

        for item in MENU:
            if item.number == choice:
                menu_item = item
                break

        if menu_item:
            order.add_item(menu_item, quantity)
            print("Item added!")

        again = input("Order another? (yes/no): ")

        if again.lower() != "yes":
            break

    print("\nORDER SUMMARY")

    for item in order.items:
        print(
            f"{item.menu_item.name} "
            f"x {item.quantity} = "
            f"₱{item.get_total():.2f}"
        )

    print(f"\nSubtotal: ₱{order.calculate_subtotal():.2f}")
    print(f"Discount: ₱{order.calculate_discount():.2f}")
    print(f"Total: ₱{order.calculate_total():.2f}")


if __name__ == "__main__":
    main()
