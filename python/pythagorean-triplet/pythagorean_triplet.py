def triplets_with_sum(sum_of_triplet):
    triplets = triplets_in_range(1, sum_of_triplet)
    triplets_equal_to_sum = []
    for triplet in triplets:
        if sum(triplet) == sum_of_triplet:
            triplets_equal_to_sum.append(triplet)
    return set(triplets_equal_to_sum)


def triplets_in_range(range_start, range_end):
    m = 2
    c = 0
    triplets = []
    while c < range_end:
        for n in range(range_start, m + 1):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if c > range_end:
                break
            if (a == 0 or b == 0 or c == 0):
                break
            triplets.append((a, b, c))
        m = m + 1
    return triplets


def is_triplet(triplet):
    a, b, c = triplet
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

triplets_in_range(1, 90)
triplets_with_sum(90)