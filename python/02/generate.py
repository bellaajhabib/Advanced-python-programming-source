# This function gives back the square of each number, one at a time.
def generate_squares(numbers):
    for number in numbers:          # Take each number from the input list.
        square = number * number    # Calculate its square.
        yield square               # Give back the square, then pause.


# Start with the numbers 1, 2, and 3.
generator = generate_squares([1, 2, 3])

# Each next() asks the generator for one more square.
# print(next(generator))  # 1 * 1 = 1
# print(next(generator))  # 2 * 2 = 4
# print(next(generator))  # 3 * 3 = 9

def infinite_numbers():
    number = 0
    while True:

        number += 1
        yield number

gen = infinite_numbers()

print(next(gen))
