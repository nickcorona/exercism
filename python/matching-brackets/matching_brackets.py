def is_paired(input_string):
    open_square = 0
    open_round = 0
    open_curly = 0
    for bracket in input_string:
        if bracket == '[':
            open_square += 1
        elif bracket == '(':
            open_round += 1
        elif bracket == '{':
            open_curly += 1
        elif bracket == ']':
            open_square -= 1
        elif bracket == ')':
            open_round -= 1
        elif bracket == '}':
            open_curly -= 1
        if open_square < 0 or open_round < 0 or open_curly < 0:
            return False
    open_brackets = open_square + open_round + open_curly
    if open_brackets == 0:
        return True
    else:
        return False

# brackets = '[]'

# open_brackets = 0
# for bracket in brackets:
#     if bracket == '[' or bracket == '(' or bracket == '{':
#         open_brackets += 1
#     else:
#         open_brackets -= 1