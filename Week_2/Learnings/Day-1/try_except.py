try:
    n = int(input("Enter a number:"))
    print(10/n)

except ZeroDivisionError:
    print("Cannot divisible by zero")

except ValueError:
    print("invalid input")