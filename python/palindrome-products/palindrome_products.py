from itertools import combinations_with_replacement


def largest_palindrome(min_factor, max_factor):
    palindromes, factors = gen_palindromes(min_factor, max_factor)
    if min_factor > max_factor:
        raise ValueError('Max factor should be greater than min factor.')
    try:
        max_palindrome = max(palindromes)
    except ValueError:
        return None, []
    indices = [i for i, x in enumerate(palindromes) if x == max_palindrome]

    max_palindrome_factors = []
    for index in indices:
        max_palindrome_factors.append(factors[index])
    return max_palindrome, set(max_palindrome_factors)


def smallest_palindrome(min_factor, max_factor):
    palindromes, factors = gen_palindromes(min_factor, max_factor)
    if min_factor > max_factor:
        raise ValueError('Max factor should be greater than min factor.')
    try:
        min_palindrome = min(palindromes)
    except ValueError:
        return None, []
    indices = [i for i, x in enumerate(palindromes) if x == min_palindrome]

    min_palindrome_factors = []
    for index in indices:
        min_palindrome_factors.append(factors[index])
    return min_palindrome, set(min_palindrome_factors)


def gen_palindromes(min_factor, max_factor):
    combination_lst = list(combinations_with_replacement(range(min_factor, max_factor + 1), r=2))
    products = [tup[0] * tup[1] for tup in combination_lst]

    palindromes = []
    factors = []
    for index, combination in enumerate(combination_lst):
        if str(products[index])[::-1] == str(products[index]):
            palindromes.append(products[index])
            factors.append(combination)
    return palindromes, factors

gen_palindromes(1002, 1003)