/** Browser-based interactive version of the TypeScript Dog OOP lesson. */
import "./style.css";

class Dog {
  constructor(public name: string, public age: number) {}

  bark(): string {
    return `${this.name} says woof!`;
  }

  birthday(): void {
    this.age += 1;
  }
}

const dogs: Dog[] = [new Dog("Buddy", 2), new Dog("Luna", 4)];
const list = document.querySelector<HTMLElement>("#dogs")!;
const status = document.querySelector<HTMLElement>("#status")!;
const form = document.querySelector<HTMLFormElement>("#dog-form")!;

function render(): void {
  list.replaceChildren();
  dogs.forEach((dog) => {
    const card = document.createElement("article");
    card.className = "panel dog";
    const details = document.createElement("div");
    const icon = document.createElement("span");
    icon.className = "icon";
    icon.textContent = "🐕";
    const name = document.createElement("h2");
    name.textContent = dog.name;
    const age = document.createElement("p");
    age.textContent = `Age: ${dog.age}`;
    details.append(icon, name, age);

    const actions = document.createElement("div");
    actions.className = "actions";
    const bark = document.createElement("button");
    bark.textContent = "Bark";
    bark.addEventListener("click", () => (status.textContent = dog.bark()));
    const birthday = document.createElement("button");
    birthday.className = "secondary";
    birthday.textContent = "Birthday (+1)";
    birthday.addEventListener("click", () => {
      dog.birthday();
      status.textContent = `Happy birthday, ${dog.name}! Their age is now ${dog.age}.`;
      render();
    });
    actions.append(bark, birthday);
    card.append(details, actions);
    list.append(card);
  });
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const fields = new FormData(form);
  const name = String(fields.get("name") ?? "").trim();
  const age = Number(fields.get("age"));
  if (!name || !Number.isInteger(age) || age < 0) {
    status.textContent = "Enter a name and a whole-number age of 0 or more.";
    return;
  }
  dogs.push(new Dog(name, age));
  form.reset();
  status.textContent = `${name} was added as a new Dog object.`;
  render();
});

render();
