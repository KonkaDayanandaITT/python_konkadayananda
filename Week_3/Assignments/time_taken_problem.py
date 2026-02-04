import time


def timetaken(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds to execute")
        return result

    return inner


@timetaken
def calculate_multiply(number1, number2):
    return f"Result: {number1*number2}"

if __name__ == "__main__":
    print(calculate_multiply(10,12))