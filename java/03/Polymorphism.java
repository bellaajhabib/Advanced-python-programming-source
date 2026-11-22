/** A method can use any object that implements the same interface. */
public class Polymorphism {
    interface AnimalSound {
        String sound();
    }

    static class DogSound implements AnimalSound {
        public String sound() {
            return "Woof";
        }
    }

    static class CatSound implements AnimalSound {
        public String sound() {
            return "Meow";
        }
    }

    static void introduce(AnimalSound animal) {
        System.out.println("The animal says: " + animal.sound());
    }

    public static void main(String[] args) {
        introduce(new DogSound());
        introduce(new CatSound());
    }
}
