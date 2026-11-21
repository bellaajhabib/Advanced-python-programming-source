"""Demonstrate when __del__ runs as object references are removed."""


class IntDel:
    """A small object used to observe object lifetime."""

    def __init__(self, number: int) -> None:
        self.number = number
        print(f"Created IntDel({self.number})")

    def show_double(self) -> int:
        """Return twice the stored number."""
        return self.number * 2

    def __del__(self) -> None:
        """Usually called when this object is about to be discarded."""
        print(f"__del__: IntDel({self.number}) is being finalized")


if __name__ == "__main__":
    print("1. Create an object and a second reference to it")
    first_reference = IntDel(10)
    second_reference = first_reference
    print(f"Double: {first_reference.show_double()}")

    print("\n2. Delete only the first variable")
    del first_reference
    print("No __del__ message yet: second_reference still points to the object")

    print("\n3. Delete the last reference")
    del second_reference
    print("In CPython, __del__ normally runs here because no references remain")

    print("\nImportant: __del__ timing is not guaranteed across Python implementations")
