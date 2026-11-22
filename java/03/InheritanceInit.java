/** Shows constructor order in an inheritance hierarchy. */
public class InheritanceInit {
    static class ParentMessage {
        ParentMessage() {
            System.out.println("Parent constructor");
        }
    }

    static class ChildMessage extends ParentMessage {
        ChildMessage() {
            super();
            System.out.println("Child constructor");
        }

        void showMessage() {
            System.out.println("I inherit behavior from ParentMessage.");
        }
    }

    public static void main(String[] args) {
        ChildMessage child = new ChildMessage();
        child.showMessage();
    }
}
