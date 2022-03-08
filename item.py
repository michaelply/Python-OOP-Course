import csv

class Item:
    discountRate = 0.8
    allItems = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations on received arguments
        assert price >= 0, f"Price {price} is less than 0"
        assert quantity >= 0, f"Quantity {quantity} is less than 0"

        # Assign arguments to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.allItems.append(self)

    @property
    # Property Decorator to create read-only attribute
    def name(self):
        return self.__name

    @name.setter
    # Change value of the read-only attribute
    def name(self, value):
        self.__name = value

    def calculateTotalPrice(self):
        return self.price * self.quantity

    def applyDiscount(self):
        return self.price * self.discountRate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    # Create instance on items listed in the csv file
    def instantiateFromCSV(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity"))
            )

    @staticmethod
    # Check if the floats are point zero (ex. 3.0)
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
