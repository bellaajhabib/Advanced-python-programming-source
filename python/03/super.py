class Parent():
    def __init__(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        print("Child")
        super().__init__()
        print("Constructor of child class")

# object = Child()

class A:
    def show(self):
        print("A class")
class B(A):
    def show(self):
        super().show()
        print("B class")

obj = B()
obj.show()

