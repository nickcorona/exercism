import numpy as np

grains_per_tile = np.array([2 ** i for i in range(0, 65)])
total_grains_per_tile = np.cumsum(grains_per_tile)


def on_square(integer_number):
    if 0 < integer_number < 65:
        return grains_per_tile[integer_number - 1]
    else:
        raise ValueError('There are 1 to 64 squares on a chessboard.')


def total_after(integer_number):
    if 0 < integer_number < 65:
        return total_grains_per_tile[integer_number - 1]
    else:
        raise ValueError('There are 1 to 64 squares on a chessboard.')
