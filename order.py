from menu import MenuItem


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_total(self):
        return self.menu_item.price * self.quantity


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        for item in self.items:

            if item.menu_item.number == menu_item.number:
                item.quantity += quantity
                return

        self.items.append(
            OrderItem(menu_item, quantity)
        )

    def calculate_subtotal(self):
        subtotal = 0

        for item in self.items:
            subtotal += item.get_total()

        return subtotal

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()

        if subtotal >= 1000:
            return subtotal * 0.10

        elif subtotal >= 500:
            return subtotal * 0.05

        return 0

    def calculate_total(self):
        return (
            self.calculate_subtotal()
            - self.calculate_discount()
        )
