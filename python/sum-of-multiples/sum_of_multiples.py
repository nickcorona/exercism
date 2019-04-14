def sum_of_multiples(limit, multiples):
    multiple_set = set()
    for multiple in multiples:
        try:
            multiple_set.update(list(range(multiple, limit, multiple)))
        except ValueError:
            continue

    return sum(multiple_set)
