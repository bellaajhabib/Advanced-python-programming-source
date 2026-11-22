/** Demonstrates calling an overridden parent method with super. */
public class SuperExample {
    static class A {
        void show() {
            System.out.println("A.show()");
        }
    }

    static class B extends A {
        @Override
        void show() {
            super.show();
            System.out.println("B.show()");
        }
    }

    public static void main(String[] args) {
        new B().show();
    }
}
