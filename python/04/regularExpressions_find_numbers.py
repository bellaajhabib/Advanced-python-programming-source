"""A simple regular-expression example using re.findall()."""

import re


text = "Sara has 3 books, 12 pencils, and 1 laptop."

# \d+ means: one or more digits.
numbers = re.findall(r"\d+", text)

print(f"Text: {text}")
print(f"Numbers found: {numbers}")

# findall returns strings, so convert them before doing arithmetic.
total = sum(int(number) for number in numbers)
print(f"Total: {total}")
