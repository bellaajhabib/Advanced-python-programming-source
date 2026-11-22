/** Demonstrates TypeScript public, protected, and private members. */
class Animal {
    public constructor(
        public name: string,
        protected age: number,
        private password: string,
    ) {}

    showName(): string {
        return `Animal: ${this.name}`;
    }
}

class Dog extends Animal {
    showAge(): string {
        // A child class may access a protected property.
        return `${this.name} is ${this.age} years old.`;
    }

    canAccessPassword(): string {
        // `password` is private to Animal and cannot be read here.
        return "The private password is accessible only inside Animal.";
    }
}

const dog = new Dog("Buddy", 5, "452");
console.log(dog.showName());
console.log(dog.showAge());
console.log(dog.canAccessPassword());
console.log(`Public name from outside: ${dog.name}`);
