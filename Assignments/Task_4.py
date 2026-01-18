#decimal to octal
num = int(input("Enter decimal number:"))

octal =""

while num > 0:
    rem = num % 8
    octal = str(rem)+octal
    num = num // 8

print("octal:",octal)

#octal to decimal

octal = input("Enter octal number:")

dec = 0
power = 0
for dig in octal[::-1]:
    dec += int(dig)*(8**power)
    power=power+1

print("decimal:",dec)