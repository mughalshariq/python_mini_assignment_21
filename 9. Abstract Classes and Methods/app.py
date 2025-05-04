from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Area of a rectangle is width * height
        return self.width * self.height

# Example usage
rect = Rectangle(5, 3)
print(f"Area of Rectangle: {rect.area()}")  # Output: 15
