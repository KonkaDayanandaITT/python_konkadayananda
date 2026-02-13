def fibonacci(n):
    prev = 0
    curr = 1
    count = 0
    while count < n:
        yield prev
        prev, curr = curr, prev + curr
        count += 1


for num in fibonacci(10):
    print(num)