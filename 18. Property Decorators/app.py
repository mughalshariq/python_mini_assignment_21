class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute with underscore

    @property
    def price(self):
        """Getter for price"""
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price"""
        print(f"Setting price to {value}...")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price

# Create a product
product = Product("Laptop", 999.99)

# Use the property getter
print(f"{product.name} costs ${product.price}")  # Calls @property

# Use the property setter
product.price = 899.99  # Calls @price.setter
print(f"New price: ${product.price}")

# Try setting invalid price
try:
    product.price = -100  # Will raise ValueError
except ValueError as e:
    print(f"Error: {e}")

# Use the deleter
del product.price  # Calls @price.deleter

# Verify deletion
try:
    print(product.price)  # Will raise AttributeError
except AttributeError:
    print("Price attribute was deleted")