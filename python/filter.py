"""Use filter() to keep only even numbers."""


def is_even(number):
    # An even number has no remainder when divided by 2.
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter() keeps numbers for which is_even() returns True.
# list() collects those numbers into a new list.
even_numbers = list(filter(is_even, numbers))

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)  # [2, 4, 6, 8, 10]
