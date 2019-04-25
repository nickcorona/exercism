def is_paired(input_string):
    open_brackets = 0
    input_string = input_string.replace(" ", "")
    for bracket in input_string:
        if bracket in ["[", "(", "{"]:
            open_brackets += 1
        else:
            open_brackets -= 1
        if open_brackets < 0:
            return False
    if (
        (input_string.count("{") == input_string.count("}"))
        and (input_string.count("(") == input_string.count(")"))
        and (input_string.count("[") == input_string.count("]"))
    ):
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
