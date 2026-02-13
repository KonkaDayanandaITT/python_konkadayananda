# decimal to octal


def decimal_to_octal(number):
    if number == 0:
        return "0"

    octal = ""

    while number > 0:
        remainder = number % 8
        octal = str(remainder) + octal
        number = number // 8

    return octal


number = int(input("Enter decimal number:"))
result = decimal_to_octal(number)
print(result)


# octal to decimal

def octal_to_decimal(octal):

    decimal = 0
    power = 0
    
    for digit in octal[::-1]:
        if digit < '0' or digit > '7':
            print("invalid octal digit: " + digit)
            return None
        decimal += int(digit) * (8**power)
        power = power + 1
           
    return decimal

octal = input("Enter octal number:")
result_decimal = octal_to_decimal(octal)

if result_decimal is not None:
    print(result_decimal)


