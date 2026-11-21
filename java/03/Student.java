/** A small OOP example showing independent Student objects. */
public final class Student {
    private final int studentId;
    private String name;

    public Student(int studentId, String name) {
        this.studentId = studentId;
        this.name = name;
    }

    public String showInfo() {
        return "Student ID: " + studentId + " | Student Name: " + name;
    }

    public void rename(String newName) {
        this.name = newName;
    }

    public static void main(String[] args) {
        // These are two independent Student objects.
        Student student1 = new Student(1, "Habib Bellaaj");
        Student student2 = new Student(2, "Maya Chen");

        System.out.println(student1.showInfo());
        System.out.println(student2.showInfo());

        // `this` refers to the current object, like Python's `self`.
        student1.rename("Habib");
        System.out.println("After renaming student1:");
        System.out.println(student1.showInfo());
        System.out.println(student2.showInfo()); // student2 is unchanged.
    }
}
