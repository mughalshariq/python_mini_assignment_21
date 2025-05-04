# Define custom exception
class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    def __init__(self, age):
        self.age = age
        super().__init__(f"Age {age} is invalid. Must be 18 or older")

# Age validation function
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print(f"Age {age} is valid - access granted")

# Test cases
ages = [15, 20, 17, 25]

for age in ages:
    try:
        check_age(age)
    except InvalidAgeError as e:
        print(f"Error: {e}")
        # Can also access the age directly: e.age