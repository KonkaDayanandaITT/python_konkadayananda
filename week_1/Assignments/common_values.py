numbers_a = [1, 2, 3, 4, 5]

numbers_b = [3, 4, 5, 6, 7]

set_a = set(numbers_a)
set_b = set(numbers_b)

common_values = list(set_a & set_b)
print(common_values)
