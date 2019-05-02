class Phone(object):
    def __init__(self, phone_number):
        self.number = phone_number

        characters_replace = "()- .+"
        for c in characters_replace:
            self.number = self.number.replace(c, "")

        if len(self.number) > 11:
            raise ValueError("Phone number cannot be greater than 11 digits.")

        if len(self.number) == 11:
            if self.number[0] == "1":
                self.number = self.number[1:]
            else:
                raise ValueError("Country code must be 1.")
        self.area_code = self.number[0:3]

        if int(self.number[0]) < 2 or int(self.number[3]) < 2:
            raise ValueError("First and fourth digits must be greater than 1.")

    def pretty(self):
        return "(" + self.area_code + ") " + self.number[3:6] + "-" + self.number[6:]
