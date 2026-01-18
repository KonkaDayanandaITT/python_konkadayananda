def prime(n):
    if n <= 1:
        return False

    else:
        for i in range(2,n):
            if n % i == 0:
                return False

        return True

prime_numbers = [x for x in range(1,10) if(prime(x))]
print(prime_numbers)