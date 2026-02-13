print("----Sorting a list----")

def sort_numbers(numbers):
    length = len(numbers)

    for pass_index in range(length):
        for current_index in range(length - 1):
            if numbers[current_index] > numbers[current_index + 1]:
                temp = numbers[current_index]
                numbers[current_index] = numbers[current_index + 1]
                numbers[current_index + 1] = temp

numbers = [6, 4, 8, 3, 9, 10]
sort_numbers(numbers)
print(numbers)


# Dict
print("----Sorting Dictionary----")
marks = {"Vishnu": 90, "Ram": 95, "Laxman": 80, "Varun": 96}

pairs = []

for key in marks:
    pairs.append((key, marks[key]))

length = len(pairs)

for pass_index in range(length):
    for current_index in range(length - 1):
        if pairs[current_index][1] > pairs[current_index + 1][1]:
            temp = pairs[current_index]
            pairs[current_index] = pairs[current_index + 1]
            pairs[current_index + 1] = temp

sorted_marks = {}
for key, value in pairs:
    sorted_marks[key] = value

print(sorted_marks)
