def color_code(color):
    color_num_dict = dict(zip(colors(), range(0, len(colors()))))
    return color_num_dict[color]


def colors():
    colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    return colors
