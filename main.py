# Import the libraries
from item import Item
from phone import Phone

# Instantiate a list of Item() objects reading from the csv file
Item.instantiate_from_csv("items.csv")
print(Item.all)

# Item() class methods
item1 = Item("Monitor", 400, 3)
print(f"Total price is {item1.calculate_total_price()}")

# Apply price increment (changes the price attribute)
item1.apply_increment(0.2)
print(f"Item price is {item1.price}")

# Apply new discount (without changing the price attribute)
item1.discount_rate = 0.5
print(f"Price after discount is {item1.apply_discount()}")
print(f"Item price is {item1.price}")

# Phone() class methods
phone1 = Phone("iPhone13", 1300)

# Inherit from item() parent class
print(phone1.all)

# Access the broken_phone attribute
print(f"The number of broken phone is {phone1.broken_phones}")