try:
    n = int(input("Enter a number:"))
    print(10/n)

except ZeroDivisionError:
    print("cannot divisible by zero")

else:
    print("Execution successfull")