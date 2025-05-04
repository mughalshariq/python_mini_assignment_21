class Person:
    def __init__(self, name):
        self.name = name  # Initialize name attribute

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent class constructor using super()
        self.subject = subject  # Add subject attribute
        
    def display(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
teacher1 = Teacher("Mr. Arif", "Mathematics")
teacher1.display()