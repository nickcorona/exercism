def triplets_with_sum(sum_of_triplet):
    triplets = triplets_in_range(1, sum_of_triplet)

    triplets_equal_to_sum = []
    for triple in triplets:
        if sum(triple) == sum_of_triplet:
            triplets_equal_to_sum.append(triple)
    return triplets_equal_to_sum


def triplets_in_range(range_start, range_end):
    triplets = []
    for n in range(range_start, range_end + 1):
        for m in range(n + 1, range_end + 1):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2

            if c > range_end:
                return triplets
            triplets.append([a, b, c])
    return triplets


def is_triplet(triplet):
    a, b, c = triplet
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False