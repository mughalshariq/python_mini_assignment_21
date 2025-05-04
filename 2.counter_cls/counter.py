class Counter:
    # Class variable to store the count of objects
    object_count = 0

    def __init__(self):
        # Increment the count whenever a new object is created
        Counter.object_count += 1

    @classmethod
    def display_count(cls):
        # Use cls to access the class variable
        print("Total objects created:", cls.object_count)

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()
