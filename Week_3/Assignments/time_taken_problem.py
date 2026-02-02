import time


def timetaken(func):
    def inner(number1, number2):
        start = time.time()
        result = func(number1, number2)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds to execute")
        return result

    return inner


@timetaken
def calculate_multiply(number1, number2):
    return f"Result:{number1*number2}"


print(calculate_multiply(2, 3))