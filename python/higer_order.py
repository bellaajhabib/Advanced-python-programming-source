# A higher-order function accepts another function as an argument.
# Here, `sum` holds the function passed in (it is not Python's built-in sum).
def operations(sum, x,y):
    # Call the supplied function with the two values and return its result.
    return sum(x, y)

# This pure function returns the same result for the same inputs,
# without changing anything outside the function.
def add(a, b):
    sum = a + b
    return sum

# Pass `add` itself, without parentheses, so operations can call it.
# operations(add, 3, 4) calls add(3, 4), returns 7, then print displays 7.
print(operations(add, 3, 4))
