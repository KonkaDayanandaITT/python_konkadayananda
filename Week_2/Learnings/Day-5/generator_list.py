squares_a = [x*x for x in range(10)]

squares_b = (x*x for x in range(10))


print(squares_a)
print(squares_b)

print(next(squares_b))
print(next(squares_b))
print(next(squares_b))
print(next(squares_b))
print(next(squares_b))