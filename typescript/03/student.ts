/** A student keeps its own ID and name. */
class Student {
    constructor(
        // These parameter properties become fields on each object.
        public studentId: number,
        public name: string,
    ) {}

    showInfo(): string {
        return `Student ID: ${this.studentId} | Student Name: ${this.name}`;
    }

    rename(newName: string): void {
        this.name = newName;
    }
}

// These are two independent Student objects.
const student1 = new Student(1, "Habib Bellaaj");
const student2 = new Student(2, "Maya Chen");

console.log(student1.showInfo());
console.log(student2.showInfo());

// `this` in TypeScript plays the same role as Python's `self`.
student1.rename("Habib");
console.log("After renaming student1:");
console.log(student1.showInfo());
console.log(student2.showInfo()); // student2 is unchanged.
