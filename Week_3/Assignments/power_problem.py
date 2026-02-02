def power(num, exp):
    for i in range(exp + 1):
        yield num**i


num = int(input("Enter the base number:"))
exp = int(input("Enter the exponent:"))
print(f"Powers of {num} up to expotent {exp}:")

for res in power(num, exp):
    print(res)