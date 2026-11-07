import java.util.*;
import java.util.function.Supplier;
import java.util.stream.Collectors;

/** Resume keyword matcher. Compile with: javac ResumeMatcher.java */
public class ResumeMatcher {
    static String normalize(String text) {
        return text.toLowerCase().replaceAll("[^a-z0-9\\s]", " ").replaceAll("\\s+", " ").trim();
    }

    /** Java's Supplier provides one resume at a time, similar to a generator. */
    static Iterator<String> resumeIterator(List<String> resumes) {
        Iterator<String> source = resumes.iterator();
        return new Iterator<>() {
            public boolean hasNext() { return source.hasNext(); }
            public String next() { return normalize(source.next()); }
        };
    }

    static List<String> extractKeywords(String resume, List<String> keywords) {
        return keywords.stream()
                .filter(keyword -> (" " + resume + " ").contains(" " + keyword + " "))
                .collect(Collectors.toList());
    }

    static List<Result> processResumes(List<String> resumes, List<String> keywords) {
        List<String> cleanKeywords = keywords.stream().map(ResumeMatcher::normalize).distinct().toList();
        List<Result> results = new ArrayList<>();
        Iterator<String> iterator = resumeIterator(resumes);
        int number = 1;

        while (iterator.hasNext()) {
            List<String> matched = extractKeywords(iterator.next(), cleanKeywords);
            int score = matched.stream().mapToInt(keyword -> 1).reduce(0, Integer::sum);
            results.add(new Result(number++, matched, score));
        }
        results.sort(Comparator.comparingInt(Result::score).reversed());
        return results;
    }

    record Result(int resume, List<String> keywords, int score) {}

    public static void main(String[] args) {
        List<String> resumes = List.of(
                "Experienced Python developer with Django, Flask, and REST APIs.",
                "Front-end engineer skilled in HTML, CSS, JavaScript, and React.",
                "Data analyst proficient in Python, Pandas, NumPy, and machine learning.",
                "Software engineer with C++, Java, and system programming."
        );
        List<String> keywords = List.of("python", "pandas", "numpy", "django", "machine learning", "flask");

        for (Result result : processResumes(resumes, keywords)) {
            System.out.printf("Resume %d | Score: %d | Keywords: %s%n",
                    result.resume(), result.score(), result.keywords());
        }
    }
}
