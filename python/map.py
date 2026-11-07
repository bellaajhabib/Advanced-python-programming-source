"""Use map() to subtract 2 from each number in a list."""


def subtract_two(number):
    return number - 2


numbers = [1, 2, 3, 4, 5]

# map() applies subtract_two to each number.
# list() collects the results into a new list.
result = list(map(subtract_two, numbers))

print("Original numbers:", numbers)
print("After subtracting 2:", result)  # [-1, 0, 1, 2, 3]
