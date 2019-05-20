from random import choices
from math import floor


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return sum(sorted(choices(population=range(1, 7), k=4)[1:4]))


def modifier(constitution):
    return floor((constitution - 10) / 2)
