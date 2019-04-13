import math


class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.food = ['eggs', 'peanuts', 'shellfish',
                     'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
        self.allergies = []
        score = self.score
        while score > 0:
            index = int(math.log2(score))
            score -= 2 ** index
            if index > 7:
                continue
            else:
                self.allergies.append(self.food[index])

    def is_allergic_to(self, item):
        if item in self.allergies:
            return True
        else:
            return False

    @property
    def lst(self):
        return self.allergies
