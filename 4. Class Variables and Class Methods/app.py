class Bank:
    # Class variable
    bank_name = "Default Bank"

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def show_info(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Create instances
customer1 = Bank("Ahmed")
customer2 = Bank("Bilal")

# Show initial info
customer1.show_info()
customer2.show_info()

# Change bank name using class method
Bank.change_bank_name("National Bank")

# Show updated info (affected all instances)
customer1.show_info()
customer2.show_info()
