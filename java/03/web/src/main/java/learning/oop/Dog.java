package learning.oop;

/** A dog object owns its state and the behavior that changes it. */
public class Dog {
    private final long id;
    private final String name;
    private int age;

    public Dog(long id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    public long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String bark() {
        return name + " says woof!";
    }

    public void birthday() {
        age++;
    }
}
