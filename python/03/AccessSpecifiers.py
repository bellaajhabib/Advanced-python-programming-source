class Test:
    id = 100
    name = "JafriCode"
    def _info(self):
        print(self.id)
        print(self.name)
    def show(self):
        self._info()

# object =  Test()
# object.show()

class Animal:
    def __init__(self,name):
        self.name="Dog"
        self.age=5
        self._password="452"

    def show(self):
        print(self.name)

class Dog(Animal):
    def show_info(self):
        print(self.name)
    def show_info2(self):
        print(self._password)

dog = Dog(Animal)
dog.show_info()
dog.show_info2()

