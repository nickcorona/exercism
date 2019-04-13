def is_armstrong(number):
    str_number = str(number)
    length = len(str_number)
    lst = []
    for integer in str_number:
        lst.append(int(integer) ** length)
    if sum(lst) == number:
        return True
    else:
        return False
