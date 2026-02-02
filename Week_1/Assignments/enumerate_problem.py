def add_index_to_values(numbers):
    result = []
    for index, value in enumerate(numbers):
        result.append((index, value))
    return result


numbers = [2, 3, 4, 5, 6]
result = add_index_to_values(numbers)
print(result)
