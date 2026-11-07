import java.util.List;

class Functional {
    public static void main(String[] args) {
        List<Integer> numbers = List.of(1, 2, 3, 4);
        System.out.println("Squares: " + numbers.stream().map(number -> number * number).toList());
        System.out.println("Even numbers: " + numbers.stream().filter(number -> number % 2 == 0).toList());
        System.out.println("Total: " + numbers.stream().reduce(0, Integer::sum));
    }
}
