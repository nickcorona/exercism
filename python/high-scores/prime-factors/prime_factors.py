def prime_factors(natural_number):
    number_left = natural_number
    prime_factors = []
    divisor = 2
    while number_left > 1:
        if number_left % divisor == 0:
            prime_factors.append(divisor)
            number_left = number_left / divisor
        else:
            divisor += 1
    return prime_factors
