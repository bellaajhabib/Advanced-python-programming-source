"""A small example of object-oriented programming (OOP)."""


class Dog:
    """A class is a blueprint for making dog objects."""

    def __init__(self, name, age):
        # Each object keeps its own data in attributes.
        self.name = name
        self.age = age

    def bark(self):
        # A method is a function that belongs to an object.
        return f"{self.name} says woof!"

    def birthday(self):
        self.age += 1


# These are two separate objects created from the same class.
dog1 = Dog("Buddy", 2)
dog2 = Dog("Luna", 4)

print(dog1.bark())       # Buddy says woof!
print(dog2.bark())       # Luna says woof!
dog1.birthday()
print(dog1.age)          # 3
print(dog2.age)          # 4 (Luna's age did not change)
