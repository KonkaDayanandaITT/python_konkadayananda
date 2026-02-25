# n = 10

# try:
#     res = n / 0
    
# except ZeroDivisionError:
#     print("cannot be divisible by Zero")


# print("Hello world")  


# n = 10
# res = n / 0


# try:
#     n = 0
#     res = 100/n
# except ZeroDivisionError:
#     print("Can not divisible by zero")
    
# except ValueError:
#     print("Enter a valid number")
    
# finally:
#     print("Execution complete")

# try:
#     a = int("str")
#     inb = 1/a
    
# except ValueError as e:
#     print("Error occured:", e)
    
# except ZeroDivisionError:
#     print("Zero has no inverse")

# a = ["10", "twenty", 30]

# try:
#     total = int(a[0]) + int(a[1]) + a[2]
    
# except(ValueError, TypeError) as e:
#     print("Error ", e)
# except IndexError:
#     print("index out of range")


# try:
#     res = "100" / 20 
    
# except ArithmeticError:
#     print("Arithmetic problem.")
    
# except Exception as e:
#     print("Something went wrong!", e)

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    
try:
    set(-5)
    
except ValueError as e:
    print("Error ",e)