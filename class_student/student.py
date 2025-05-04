class Student:
    def __init__(self, name, marks):
        self.name = name    # Initialize name using self
        self.marks = marks  # Initialize marks using self
    
    def display(self):
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Shariq", 85)
student1.display()