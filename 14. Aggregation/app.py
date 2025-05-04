# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")

# Department class (Aggregation)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: has a reference to an Employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Accessing method from independent Employee object

# Example usage
emp1 = Employee("Ahsan")              # Independent Employee object
dept1 = Department("IT", emp1)        # Aggregation: Department has a reference

dept1.show_details()
