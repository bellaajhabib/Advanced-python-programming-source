"""Use reduce to combine the elements of an iterable into a single value.

In Python 3, reduce is imported from functools; it is not a built-in function.
It can combine elements from lists, tuples, and other iterables.
"""

from functools import reduce


def add(total, number):
    return total + number


numbers = [1, 2, 3, 4, 5]

# Start with 0 and add each number: 0 + 1 + 2 + 3 + 4 + 5 = 15.
result = reduce(add, numbers, 0)

print(result)  # Output: 15
