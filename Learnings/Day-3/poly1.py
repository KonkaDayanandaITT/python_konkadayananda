class Calculator:
    def multiply(self,a = 1, b = 1 , *args):
        result = a*b
        for num in args:
            result = result * num

        return result

cal = Calculator()

print(cal.multiply())
print(cal.multiply(2,3,4,5))