# Score categories
# Change the values as you see fit
from collections import Counter
YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full_house'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'


def score(dice, category):
    if category == 'yacht':
        return 50
    elif category == 'ones':
        return sum([roll for roll in dice if roll == 1])
    elif category == 'twos':
        return sum([roll for roll in dice if roll == 2])
    elif category == 'threes':
        return sum([roll for roll in dice if roll == 3])
    elif category == 'fours':
        return sum([roll for roll in dice if roll == 4])
    elif category == 'fives':
        return sum([roll for roll in dice if roll == 5])
    elif category == 'sixes':
        return sum([roll for roll in dice if roll == 6])
    elif category == 'full_house':
        if (Counter(dice)[0] == 3 and Counter(dice)[1] == 2) or (Counter(dice)[0] == 2 and Counter(dice)[1] == 3):
            return sum(dice)
        else:
            return 0
    elif category == 'four_of_a_kind':
        if Counter(dice)[0] >= 4 or Counter(dice)[1] >= 4:
            for roll, number in Counter(dice).items():
                if number == 4:
                    print(roll * 4)
        else:
            return 0
    elif category == 'little_straight':
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    elif category == 'big_straight':
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    elif category == 'choice':
        return sum(dice)


# if category == 'yacht':
#     print(50)
# elif category == 'ones':
#     print(sum([roll for roll in dice if roll == 1]))
# elif category == 'twos':
#     print(sum([roll for roll in dice if roll == 2]))
# elif category == 'threes':
#     print(sum([roll for roll in dice if roll == 3]))
# elif category == 'fours':
#     print(sum([roll for roll in dice if roll == 4]))
# elif category == 'fives':
#     print(sum([roll for roll in dice if roll == 5]))
# elif category == 'sixes':
#     print(sum([roll for roll in dice if roll == 6]))
# elif category == 'full_house':
#     if (Counter(dice)[0] == 3 and Counter(dice)[1] == 2) or (Counter(dice)[0] == 2 and Counter(dice)[1] == 3):
#         print(sum(dice))
#     else:
#         print(0)
# elif category == 'four_of_a_kind':
#     if Counter(dice)[0] == 4 or Counter(dice)[1] == 4:
#         for roll, number in Counter(dice).items():
#             if number == 4:
#                 print(roll * 4)
#     else:
#         print(0)
# elif category == 'little_straight':
#     if sorted(dice) == [1, 2, 3, 4, 5]:
#         print(30)
#     else:
#         print(0)
# elif category == 'big_straight':
#     if sorted(dice) == [2, 3, 4, 5, 6]:
#         print(30)
#     else:
#         print(0)
# elif category == 'choice':
#     print(sum(dice))
#
