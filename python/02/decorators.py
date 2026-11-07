# Example 1: print a message before and after a function runs.
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper


def say_hello():
    print("Hello!")


# Wrap say_hello with the decorator, then call the wrapped function.
wrapped_function = my_decorator(say_hello)
wrapped_function()


# Example 2: change a function's text result to uppercase.
def uppercase_decorator(func):
    def wrapper():
        message = func()
        return message.upper()

    return wrapper


def get_message():
    return "hello from a decorated function"


# The decorator adds uppercase behavior to get_message.
uppercase_message = uppercase_decorator(get_message)
print(uppercase_message())  # HELLO FROM A DECORATED FUNCTION
