class Strings {
    static String normalize(String text) {
        return text.toLowerCase().replaceAll("[^a-z0-9\\s]", " ").replaceAll("\\s+", " ").trim();
    }

    public static void main(String[] args) {
        System.out.println(normalize(" Java, Spring! "));
    }
}
