"""A pure function returns the same result for the same inputs.

It does not change external state or its inputs.
"""


def add(a: int, b: int) -> int:
    """Return the sum without any side effects."""
    return a + b


if __name__ == "__main__":
    # Printing is a side effect, so it stays outside the pure function.
    print(add(2, 3))  # 5
    print(add(2, 3))  # 5 again: same inputs, same result
