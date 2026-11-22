/**
 * Java has no reliable equivalent of Python's __del__. Use AutoCloseable for
 * deterministic cleanup of resources such as files, sockets, or databases.
 */
public class IntDel {
    static class NumberResource implements AutoCloseable {
        private final int number;

        NumberResource(int number) {
            this.number = number;
            System.out.println("Created NumberResource(" + number + ")");
        }

        int doubleValue() {
            return number * 2;
        }

        @Override
        public void close() {
            System.out.println("close(): cleaned up NumberResource(" + number + ")");
        }
    }

    public static void main(String[] args) {
        try (NumberResource resource = new NumberResource(10)) {
            System.out.println("Double: " + resource.doubleValue());
        }
        System.out.println("Cleanup happened when the try-with-resources block ended.");
    }
}
