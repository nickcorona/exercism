def score(x, y):
    form = (x ** 2 + y ** 2) ** (1 / 2)
    if form <= 1:
        return 10
    elif form <= 5:
        return 5
    elif form <= 10:
        return 1
    else:
        return 0
