def fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


for num in fibonacci(10):
    print(num)