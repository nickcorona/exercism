from itertools import combinations_with_replacement


def largest_palindrome(max_factor, min_factor):
    pass


def smallest_palindrome(max_factor, min_factor):
    pass


max_factor = 9
min_factor = 1

combination_lst = combinations_with_replacement(range(min_factor, max_factor + 1), r=2)
[tup[0] * tup[1] for tup in combination_lst]


