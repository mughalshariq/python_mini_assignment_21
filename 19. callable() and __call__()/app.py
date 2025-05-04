class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor
    
    def __call__(self, x):
        """Make instances callable like functions"""
        return x * self.factor

# Create multiplier objects
double = Multiplier(2)
triple = Multiplier(3)

# Test if objects are callable
print("Is double callable?", callable(double))  # True
print("Is triple callable?", callable(triple))  # True

# Call objects like functions
print("Double of 5:", double(5))    # 10
print("Triple of 5:", triple(5))    # 15
print("Double of 3.14:", double(3.14))  # 6.28

# Can still access attributes normally
print("Multiplication factor:", triple.factor)  # 3