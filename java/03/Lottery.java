import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** Console version of the Turtle lottery example. */
public class Lottery {
    static List<Integer> drawNumbers(int count, int maximum) {
        List<Integer> pool = new ArrayList<>();
        for (int number = 1; number <= maximum; number++) {
            pool.add(number);
        }
        Collections.shuffle(pool);
        return pool.subList(0, count);
    }

    public static void main(String[] args) {
        List<Integer> numbers = drawNumbers(6, 49);
        Collections.sort(numbers);
        System.out.println("Lottery numbers: " + numbers);
    }
}
