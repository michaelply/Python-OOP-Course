from item import Item

# Create a Phone class that inherits from the Item class
class Phone(Item):

    def __init__(self, name: str, price: float, quantity = 0, brokenPhones = 0):

        # Inherit attributes from the Item() parent class
        super().__init__(
            name, price, quantity
        )

        # Assign argument to self object
        self.brokenPhones = brokenPhones

