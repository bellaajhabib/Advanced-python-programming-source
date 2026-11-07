"""Interactive Tkinter desktop app demonstrating the Dog OOP lesson."""

import tkinter as tk
from tkinter import messagebox, ttk


class Dog:
    """A dog object keeps its own name and age."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says woof!"

    def birthday(self) -> None:
        self.age += 1


class DogApp(tk.Tk):
    """A small GUI that lets the user create and interact with Dog objects."""

    def __init__(self) -> None:
        super().__init__()
        self.title("OOP Dogs — Desktop")
        self.geometry("520x430")
        self.minsize(420, 360)

        self.dogs: list[Dog] = [Dog("Buddy", 2), Dog("Luna", 4)]
        self.status = tk.StringVar(value="Create a dog or choose one from the list.")

        self._build_ui()
        self._refresh_dogs()

    def _build_ui(self) -> None:
        frame = ttk.Frame(self, padding=18)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Dog OOP playground", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(frame, text="Each dog is a separate object with its own name and age.").pack(anchor="w", pady=(2, 14))

        form = ttk.LabelFrame(frame, text="Create a Dog object", padding=10)
        form.pack(fill="x")
        ttk.Label(form, text="Name").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(form)
        self.name_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        ttk.Label(form, text="Age").grid(row=0, column=1, sticky="w")
        self.age_entry = ttk.Entry(form, width=8)
        self.age_entry.grid(row=1, column=1, sticky="ew", padx=(0, 10))
        ttk.Button(form, text="Add dog", command=self.add_dog).grid(row=1, column=2)
        form.columnconfigure(0, weight=1)

        ttk.Label(frame, text="Dog objects").pack(anchor="w", pady=(14, 4))
        self.dog_list = tk.Listbox(frame, height=7, exportselection=False)
        self.dog_list.pack(fill="both", expand=True)
        self.dog_list.bind("<<ListboxSelect>>", self._show_dog)

        actions = ttk.Frame(frame)
        actions.pack(fill="x", pady=10)
        ttk.Button(actions, text="Bark", command=self.bark).pack(side="left")
        ttk.Button(actions, text="Birthday (+1 age)", command=self.birthday).pack(side="left", padx=8)
        ttk.Label(frame, textvariable=self.status, wraplength=470).pack(anchor="w")

    def _refresh_dogs(self, selected: int | None = None) -> None:
        self.dog_list.delete(0, tk.END)
        for dog in self.dogs:
            self.dog_list.insert(tk.END, f"{dog.name} — age {dog.age}")
        if self.dogs:
            index = 0 if selected is None else selected
            self.dog_list.selection_set(index)
            self.dog_list.activate(index)
            self._show_dog()

    def _selected_dog(self) -> Dog | None:
        selection = self.dog_list.curselection()
        return self.dogs[selection[0]] if selection else None

    def _show_dog(self, _event: tk.Event | None = None) -> None:
        dog = self._selected_dog()
        if dog:
            self.status.set(f"Selected object: Dog(name={dog.name!r}, age={dog.age})")

    def add_dog(self) -> None:
        name = self.name_entry.get().strip()
        try:
            age = int(self.age_entry.get())
            if age < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid age", "Enter a whole number that is 0 or greater.")
            return
        if not name:
            messagebox.showerror("Missing name", "Enter a name for the dog.")
            return

        self.dogs.append(Dog(name, age))
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self._refresh_dogs(len(self.dogs) - 1)

    def bark(self) -> None:
        dog = self._selected_dog()
        if dog:
            self.status.set(dog.bark())

    def birthday(self) -> None:
        dog = self._selected_dog()
        if dog:
            dog.birthday()
            index = self.dog_list.curselection()[0]
            self._refresh_dogs(index)
            self.status.set(f"Happy birthday, {dog.name}! The object's age is now {dog.age}.")


if __name__ == "__main__":
    DogApp().mainloop()
