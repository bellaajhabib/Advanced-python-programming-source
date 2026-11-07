/** A small example of object-oriented programming (OOP). */
public final class Oop {
    /** A class is a blueprint for making dog objects. */
    private static final class Dog {
        // Each object keeps its own data in fields.
        private final String name;
        private int age;

        private Dog(String name, int age) {
            this.name = name;
            this.age = age;
        }

        private String bark() {
            // A method is a function that belongs to an object.
            return name + " says woof!";
        }

        private void birthday() {
            age += 1;
        }
    }

    public static void main(String[] args) {
        // These are two separate objects created from the same class.
        Dog dog1 = new Dog("Buddy", 2);
        Dog dog2 = new Dog("Luna", 4);

        System.out.println(dog1.bark()); // Buddy says woof!
        System.out.println(dog2.bark()); // Luna says woof!
        dog1.birthday();
        System.out.println(dog1.age);    // 3
        System.out.println(dog2.age);    // 4 (Luna's age did not change)
    }
}
