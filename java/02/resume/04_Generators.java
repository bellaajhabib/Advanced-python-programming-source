import java.util.Iterator;
import java.util.List;

class Generators {
    // Java uses Iterator for one-at-a-time processing.
    static Iterator<Integer> numbers(List<Integer> values) { return values.iterator(); }

    public static void main(String[] args) {
        Iterator<Integer> generator = numbers(List.of(1, 2, 3));
        while (generator.hasNext()) System.out.println(generator.next());
    }
}
