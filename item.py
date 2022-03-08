import csv

class Item:
    # Declare class variables
    discount_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations on received arguments
        assert price >= 0, f"Price {price} is less than 0"
        assert quantity >= 0, f"Quantity {quantity} is less than 0"

        # Assign arguments to self object (__ to make it private)
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        # Actions to execute when creating an instance
        # Add to the object lists
        Item.all.append(self)

    @property
    # Property Decorator to create read-only attribute (encapsulation)
    def name(self):
        return self.__name

    @name.setter
    # Change value of the read-only attribute (encapsulation)
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_increment(self, incrementValue):
        self.__price += self.__price * incrementValue

    def calculate_total_price(self):
        return self.__price * self.__quantity

    def apply_discount(self):
        return self.__price * self.discount_rate

    # Change the representation of an object instance (instead of displaying memory address)
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.__quantity})"

    @classmethod
    # Create instances on items listed in the csv file
    def instantiate_from_csv(cls, csv_file_name):
        with open(csv_file_name, "r") as f:
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
