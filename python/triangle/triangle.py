def is_equilateral(sides):
    sorted_sides = sorted(sides)
    if sum(sides) == 0:
        return False
    if sorted_sides[0] + sorted_sides[1] < sorted_sides[2]:
        return False
    if sides[0] == sides[1] == sides[2]:
        return True
    else:
        return False


def is_isosceles(sides):
    sides_sorted = sorted(sides)
    if sum(sides) == 0:
        return False
    if sides_sorted[0] + sides_sorted[1] < sides_sorted[2]:
        return False
    for side in sides:
        if sides.count(side) >= 2:
            return True
    return False


def is_scalene(sides):
    sides_sorted = sorted(sides)
    if sum(sides) == 0:
        return False
    if sides_sorted[0] + sides_sorted[1] < sides_sorted[2]:
        return False
    if sides[0] != sides[1] != sides[2]:
        return True
    else:
        return False
