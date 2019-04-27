# Score categories
# Change the values as you see fit
from collections import Counter

YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"


def score(dice, category):
    if category == "yacht":
        if Counter(dice).most_common()[0][1] == 5:
            return 50
        else:
            return 0
    elif category == "ones":
        return sum([roll for roll in dice if roll == 1])
    elif category == "twos":
        return sum([roll for roll in dice if roll == 2])
    elif category == "threes":
        return sum([roll for roll in dice if roll == 3])
    elif category == "fours":
        return sum([roll for roll in dice if roll == 4])
    elif category == "fives":
        return sum([roll for roll in dice if roll == 5])
    elif category == "sixes":
        return sum([roll for roll in dice if roll == 6])
    elif category == "full_house":
        most_common = Counter(dice).most_common()
        if most_common[0][1] == 3 and most_common[1][1] == 2:
            return most_common[0][0] * 3 + most_common[1][0] * 2
        else:
            return 0
    elif category == "four_of_a_kind":
        if Counter(dice).most_common()[0][1] >= 4:
            return Counter(dice).most_common()[0][0] * 4
        else:
            return 0
    elif category == "little_straight":
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    elif category == "big_straight":
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    elif category == "choice":
        return sum(dice)