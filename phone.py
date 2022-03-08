# Import the Item() parent class
from item import Item

# Create a Phone class that inherits from the Item class (Inheritance)
class Phone(Item):

    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):

        # Inherit attributes from the Item() parent class
        super().__init__(
            name, price, quantity
        )

        # Assign argument to self object
        self.broken_phones = broken_phones

