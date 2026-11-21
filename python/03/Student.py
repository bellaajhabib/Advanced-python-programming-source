"""Learn how ``self`` connects a method call to one specific Student object."""


class Student:
    """A student stores an ID and name on its own instance."""

    def __init__(self, student_id: int, name: str) -> None:
        # self refers to the new object being initialized.
        self.student_id = student_id
        self.name = name

    def show_info(self) -> str:
        """Build a description using this object's attributes."""
        return f"Student ID: {self.student_id} | Student Name: {self.name}"

    def rename(self, new_name: str) -> None:
        """Change the name belonging to this particular student."""
        self.name = new_name


if __name__ == "__main__":
    # These calls create two independent Student objects.
    student1 = Student(1, "Habib Bellaaj")
    student2 = Student(2, "Maya Chen")

    print(student1.show_info())
    print(student2.show_info())

    # Calling rename on student1 passes student1 as self.
    student1.rename("Habib")
    print("After renaming student1:")
    print(student1.show_info())
    print(student2.show_info())  # student2 is unchanged.
