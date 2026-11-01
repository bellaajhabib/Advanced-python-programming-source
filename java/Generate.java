import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class Generate {
    // Java has no yield keyword for generators, so this method uses an Iterator.
    static Iterator<Integer> generateSquares(List<Integer> numbers) {
        return new Iterator<Integer>() {
            private int position = 0; // Remembers which number comes next.

            @Override
            public boolean hasNext() {
                return position < numbers.size();
            }

            @Override
            public Integer next() {
                if (!hasNext()) {
                    throw new NoSuchElementException("No more numbers");
                }

                int number = numbers.get(position); // Take the next input number.
                position++;                         // Move to the following number.
                int square = number * number;       // Calculate its square.
                return square;                     // Give back one result.
            }
        };
    }

    public static void main(String[] args) {
        // Start with the numbers 1, 2, and 3.
        Iterator<Integer> generator = generateSquares(List.of(1, 2, 3));

        // hasNext() checks for another result; next() gets it.
        while (generator.hasNext()) {
            System.out.println(generator.next());
        }
    }
}
