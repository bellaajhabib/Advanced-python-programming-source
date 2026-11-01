"""A decorator adds behavior around another function."""
from functools import wraps
from time import perf_counter


def log_execution_time(func):
    @wraps(func)  # Preserve the original function's name and documentation.
    def wrapper(*args, **kwargs):
        # Forward positional and named arguments to the original function.
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {perf_counter() - start:.6f} seconds")
        return result
    return wrapper


@log_execution_time
def count_words(text):
    return len(text.split())


print(count_words("Python and Django"))  # Timing message, then 3
# @log_execution_time means count_words = log_execution_time(count_words).
# Exercise: decorate a function that adds two numbers and returns the sum.
