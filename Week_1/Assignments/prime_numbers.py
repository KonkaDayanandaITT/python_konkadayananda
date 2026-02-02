def prime_check(n):
    if n <= 1:
        return False

    else:
        for divisor in range(2, n):
            if n % divisor == 0:
                return False

        return True


prime_numbers = [x for x in range(1, 11) if prime_check(x)]
print(prime_numbers)
