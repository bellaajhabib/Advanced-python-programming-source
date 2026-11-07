/** A small example of object-oriented programming (OOP). */
class Dog {
    /** A class is a blueprint for making dog objects. */
    constructor(
        // Each object keeps its own data in properties.
        public name: string,
        public age: number,
    ) {}

    bark(): string {
        // A method is a function that belongs to an object.
        return `${this.name} says woof!`;
    }

    birthday(): void {
        this.age += 1;
    }
}

// These are two separate objects created from the same class.
const dog1 = new Dog("Buddy", 2);
const dog2 = new Dog("Luna", 4);

console.log(dog1.bark()); // Buddy says woof!
console.log(dog2.bark()); // Luna says woof!
dog1.birthday();
console.log(dog1.age);    // 3
console.log(dog2.age);    // 4 (Luna's age did not change)
