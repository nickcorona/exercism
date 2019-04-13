def slices(series, length):
    lst = []
    if len(series) < length:
        raise ValueError('Length is too long.')
    elif length <= 0:
        raise ValueError('Length cannot be less than or equal to 0.')
    for i in range(0, length + 1):
        sub_string = series[i:length + i]
        if len(sub_string) == length:
            lst.append(sub_string)
    return lst
