class Dog:
    def __init__(self, name, breed):
        self.name = name    # Instance variable
        self.breed = breed  # Instance variable
    
    def bark(self):         # Instance method
        print(f"{self.name} the {self.breed} says: Woof!")

# Creating instances
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Calling instance methods
dog1.bark()
dog2.bark()