"""Combine a list of colors into one string using reduce."""

# In Python 3, reduce must be imported from functools.
from functools import reduce


def combine_colors(combined, next_color):
    """Add the next color to the string built so far."""
    return combined + " - " + next_color


colors = ["pink", "yellow", "black"]

# With no initial value, reduce starts with the first color:
# 1. combine_colors("pink", "yellow") -> "pink - yellow"
# 2. combine_colors("pink - yellow", "black") -> "pink - yellow - black"
# Each returned value becomes the first argument in the next step.
# This version requires a nonempty iterable.
result = reduce(combine_colors, colors)

print(result)  # Output: pink - yellow - black

# For simply joining strings, " - ".join(colors) is more direct.
