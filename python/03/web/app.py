"""Small Flask web app demonstrating the Dog OOP lesson."""

from flask import Flask, redirect, render_template, request, url_for


class Dog:
    """A dog object keeps its own name and age."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says woof!"

    def birthday(self) -> None:
        self.age += 1


app = Flask(__name__)
dogs = [Dog("Buddy", 2), Dog("Luna", 4)]
messages: dict[int, str] = {}


def dog_at(index: str) -> tuple[int, Dog] | None:
    try:
        dog_index = int(index)
        return (dog_index, dogs[dog_index]) if 0 <= dog_index < len(dogs) else None
    except (ValueError, TypeError):
        return None


@app.get("/")
def index():
    return render_template("index.html", dogs=dogs, messages=messages)


@app.post("/dogs")
def add_dog():
    name = request.form.get("name", "").strip()
    try:
        age = int(request.form.get("age", ""))
        if age < 0:
            raise ValueError
    except ValueError:
        return render_template("index.html", dogs=dogs, messages=messages, error="Age must be a whole number that is 0 or greater."), 400
    if not name:
        return render_template("index.html", dogs=dogs, messages=messages, error="Name is required."), 400
    dogs.append(Dog(name, age))
    return redirect(url_for("index"))


@app.post("/dogs/<int:index>/bark")
def bark(index: int):
    if 0 <= index < len(dogs):
        messages[index] = dogs[index].bark()
    return redirect(url_for("index"))


@app.post("/dogs/<int:index>/birthday")
def birthday(index: int):
    if 0 <= index < len(dogs):
        dog = dogs[index]
        dog.birthday()
        messages[index] = f"Happy birthday, {dog.name}! They are now {dog.age}."
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Bind to all container interfaces so a Dev Container tool can forward port 5000.
    app.run(host="0.0.0.0", port=5000, debug=False)
