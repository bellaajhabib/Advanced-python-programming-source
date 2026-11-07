/** Interactive Electron renderer demonstrating the Dog OOP lesson. */
export {};

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
  dogs.forEach((dog, index) => {
    const card = document.createElement("article");
    card.className = "panel dog";
    const details = document.createElement("div");
    details.innerHTML = `<span class="icon">🐕</span><h2></h2><p>Age: <strong>${dog.age}</strong></p>`;
    details.querySelector("h2")!.textContent = dog.name;
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
  const nameInput = form.elements.namedItem("name") as HTMLInputElement;
  const ageInput = form.elements.namedItem("age") as HTMLInputElement;
  const name = nameInput.value.trim();
  const age = Number(ageInput.value);
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
