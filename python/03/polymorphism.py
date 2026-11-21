class A:
    def show(self):
        print("Jafricode from A class")

class B(A):
    def show(self):
        super().show()
        print("Jafricode from B class")


a = A()
b = B()

print(a.show())
print(b.show())