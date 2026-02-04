def power(num, exp):
    for i in range(exp + 1):
        yield num**i


if __name__ == "__main__":
    try:
        num = int(input("Enter the base number:"))
        exp = int(input("Enter the exponent:"))
    
        if num < 0 or exp < 0:
            raise ValueError("Error: Enter a proper number")
    
        print(f"Powers of {num} up to exponent {exp}:")
        for res in power(num, exp):
            print(res)
    except ValueError as e:
        print(f"Error occurred: {e}")
