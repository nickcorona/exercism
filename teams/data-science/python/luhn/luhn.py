class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def is_valid(self):
        if not self.card_num.isnumeric() or len(self.card_num) <= 1:
            return False

        card_num_lst = [int(i) for i in self.card_num]
        for index in range(len(card_num_lst) - 2, -1, -2):
            num = card_num_lst[index] * 2
            if num > 9:
                num -= 9
            card_num_lst[index] = num
        if sum(card_num_lst) % 10 == 0:
            return True
        else:
            return False
