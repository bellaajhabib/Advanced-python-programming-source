"""A first, simple regular-expression example."""

import re


# r"..." is a raw string. \d means "one digit".
pattern = r"\d+"

values = ["123", "hello", "42abc"]

for value in values:
    # fullmatch checks that the complete value matches the pattern.
    if re.fullmatch(pattern, value):
        print(f"{value!r} contains only digits")
    else:
        print(f"{value!r} does not contain only digits")
