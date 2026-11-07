"""Square each number using map() and a lambda function."""


def main() -> None:
    numbers = [1, 2, 3]

    # map() applies the lambda to each number.
    # The lambda returns the number multiplied by itself (its square).
    # list() collects the results from map() into a new list.
    squared_numbers = list(map(lambda number: number * number, numbers))

    print(f"Original numbers: {numbers}")
    print(f"Squared numbers: {squared_numbers}")


# Run the example only when this file is executed directly.
if __name__ == "__main__":
    main()
