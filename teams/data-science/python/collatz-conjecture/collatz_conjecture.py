def steps(number):
    if number <= 0:
        raise ValueError('number must be greater than 0.')
    if number == 1:
        return 0
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    return 1 + steps(number)
