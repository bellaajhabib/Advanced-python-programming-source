"""A pure function returns a result without changing its input."""
import re


def normalize(text):
    # Keep letters and numbers; replace punctuation with spaces.
    # This basic rule is suitable for our sample keywords, not C++ or C#.
    return " ".join(re.sub(r"[^a-z0-9\s]", " ", text.lower()).split())


def has_keyword(text, keyword):
    # Padding prevents "java" from matching inside "javascript".
    return f" {normalize(keyword)} " in f" {normalize(text)} "


if __name__ == "__main__":
    original = "  PYTHON, Django!  "
    print(normalize(original))                  # python django
    print(original)                            # Original stays unchanged
    print(has_keyword("JavaScript", "java"))   # False
    print(has_keyword("Machine-learning", "machine learning"))  # True
    # Exercise: try extra spaces, punctuation, and uppercase letters.
