def is_happy(num):
    temp_num = num
    lst = []
    visited = lst

    while temp_num != 1:
        if temp_num in visited:
            return
        visited.append(temp_num)
        total = 0

        while temp_num > 0:
            digit = temp_num % 10
            total = total + digit**2
            temp_num = temp_num // 10
        temp_num = total

    return True


def next_happy_number(n):
    n += 1
    while True:
        if is_happy(n):
            return n
        n += 1


number = int(input("Enter the number: "))
print("Next Happy number is:", next_happy_number(number))