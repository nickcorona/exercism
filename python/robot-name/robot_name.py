import random


class Robot(object):
    names = []
    alphabet = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        name = (
            random.choice(self.alphabet)
            + random.choice(self.alphabet)
            + str(random.choice(self.integers))
            + str(random.choice(self.integers))
            + str(random.choice(self.integers))
        )
        self.names.append(name)
        return name

    def reset(self):
        name = self.generate_name()

        while name in self.names:
            name = self.generate_name()
        self.name = name