class A:
    def show(self):
        print("Show from Class A")

class B(A):
    def show(self):
        print("Show from Class B")

class C(A):
    def show(self):
        print("Show from Class C")

class D(B, C):  # Inherits from B and C (diamond shape)
    pass

# Create object of D
d = D()
d.show()

# To display the MRO
print(D.__mro__)
