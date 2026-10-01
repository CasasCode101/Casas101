class MenuItem:
    def __init__(self, number, name, price):
        self.number = number
        self.name = name
        self.price = price


MENU = [
    MenuItem(1, "Burger", 50.00),
    MenuItem(2, "Cheese Burger", 120.00),
    MenuItem(3, "Chicken Meal", 150.00),
    MenuItem(4, "French Fries", 65.00),
    MenuItem(5, "Spaghetti", 85.00),
    MenuItem(6, "Soft Drink", 45.00),
    MenuItem(7, "Burger Steak", 190.00)
]
