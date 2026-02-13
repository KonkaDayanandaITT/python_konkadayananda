def is_happy(num):
    temp_num = num
    visited = set()
    
    while temp_num != 1:
        if temp_num in visited:
            return False
        visited.add(temp_num)
        
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
            yield n
        n += 1



if __name__ == "__main__":
    try: 
        number = int(input("Enter the number: "))
        gen = next_happy_number(number) 
        print("Next happy number is:", next(gen))
    except ValueError as e:
        print(f"Error occurred: {e}")
    


