def add_greeting(cls):
    """Class decorator that adds a greet() method"""
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add the new method to the class
    return cls  # Return the modified class

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test the decorated class
p = Person("Shariq")
print(p.greet())  # Calls the decorator-added method
print(p.name)     # Original class functionality remains