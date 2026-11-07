class Decorators {
    // Java has no @decorator syntax, so a wrapper adds the extra behavior.
    static Runnable logCall(Runnable function) {
        return () -> { System.out.println("before"); function.run(); System.out.println("after"); };
    }

    public static void main(String[] args) { logCall(() -> System.out.println("Hello!")).run(); }
}
