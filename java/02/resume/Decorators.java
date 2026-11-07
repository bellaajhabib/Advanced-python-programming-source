import java.util.function.Supplier;

public class Decorators {
    // Example 1: print a message before and after a function runs.
    static Runnable myDecorator(Runnable func) {
        return () -> {
            System.out.println("before");
            func.run();
            System.out.println("after");
        };
    }

    static void sayHello() {
        System.out.println("Hello!");
    }

    // Example 2: change a function's text result to uppercase.
    static Supplier<String> uppercaseDecorator(Supplier<String> func) {
        return () -> func.get().toUpperCase();
    }

    static String getMessage() {
        return "hello from a decorated function";
    }

    public static void main(String[] args) {
        Runnable wrappedFunction = myDecorator(Decorators::sayHello);
        wrappedFunction.run();

        Supplier<String> uppercaseMessage = uppercaseDecorator(Decorators::getMessage);
        System.out.println(uppercaseMessage.get()); // HELLO FROM A DECORATED FUNCTION
    }
}
