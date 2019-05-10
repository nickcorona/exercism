def collatz_steps(number):
    if number <= 0:
        raise ValueError("Number must be positive..")
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        steps += 1
    return steps
