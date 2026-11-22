/** Demonstrates Java public, protected, and private members. */
public class AccessSpecifiers {
    static class Animal {
        public final String name;
        protected final int age;
        private final String password;

        Animal(String name, int age) {
            this.name = name;
            this.age = age;
            this.password = "452";
        }

        public String showName() {
            return name;
        }
    }

    static class Dog extends Animal {
        Dog(String name, int age) {
            super(name, age);
        }

        int showAge() {
            return age; // protected: available in a subclass
        }

        boolean canAccessPassword() {
            // password is private to Animal, so it is not available here.
            return false;
        }
    }

    public static void main(String[] args) {
        Dog dog = new Dog("Buddy", 5);
        System.out.println("Public name: " + dog.showName());
        System.out.println("Protected age through Dog: " + dog.showAge());
        System.out.println("Can Dog access Animal's private password? " + dog.canAccessPassword());
    }
}
