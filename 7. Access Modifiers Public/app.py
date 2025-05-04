class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name               # Public
        self._salary = salary          # Protected
        self.__ssn = ssn               # Private

    # Getter for _salary (protected)
    def get_salary(self):
        return self._salary

    # Setter for _salary
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Invalid salary amount!")

    # Getter for __ssn (private)
    def get_ssn(self):
        return self.__ssn

    # Setter for __ssn
    def set_ssn(self, new_ssn):
        if isinstance(new_ssn, str) and len(new_ssn) == 11:
            self.__ssn = new_ssn
        else:
            print("Invalid SSN format!")


# Example usage
emp = Employee("Shariq Mughal", 50000, "123-45-6789")

# Access public variable directly
print("Name:", emp.name)

# Access and modify protected variable using getter/setter
print("Salary:", emp.get_salary())
emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())

# Access and modify private variable using getter/setter
print("CNIC:", emp.get_ssn())
emp.set_ssn("987-65-4321")
print("Updated CNIC:", emp.get_ssn())
