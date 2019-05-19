from itertools import combinations, starmap, takewhile


def triplets_with_sum(sum_of_triplet):
    triplets_with_sum = []
    pythagorean_triplets = triplets_in_range(1, sum_of_triplet)
    for triplet in pythagorean_triplets:
        a, b, c = triplet
        if a + b + c == sum_of_triplet:
            triplets_with_sum.append(triplet)
    return set(triplets_with_sum)


def triplets_in_range(range_start, range_end):
    pythagorean_triplets = []
    for triplet in combinations(range(range_start, range_end), r=3):
        if is_triplet(triplet):
            pythagorean_triplets.append(triplet)
    return pythagorean_triplets


def is_triplet(triplet):
    a, b, c = triplet
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


starmap(sum, combinations(range(1, 10), r=3))
