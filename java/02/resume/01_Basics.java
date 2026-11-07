import java.util.List;
import java.util.Map;

class Basics {
    static String describe(Map<String, Object> candidate) {
        @SuppressWarnings("unchecked")
        List<String> skills = (List<String>) candidate.get("skills");
        return candidate.get("name") + " knows " + String.join(", ", skills);
    }

    public static void main(String[] args) {
        Map<String, Object> candidate = Map.of("name", "Alice", "skills", List.of("Java", "Spring"), "years", 3);
        System.out.println(describe(candidate));
    }
}
