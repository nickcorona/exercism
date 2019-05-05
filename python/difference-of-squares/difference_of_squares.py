import numpy as np


def square_of_sum(count):
    return sum(np.array(range(1, count + 1))) ** 2


def sum_of_squares(count):
    return sum(np.array(range(1, count + 1)) ** 2)


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
