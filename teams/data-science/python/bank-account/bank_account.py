class BankAccount(object):
    def __init__(self):
        self.money = 0
        self.closed = True

    def get_balance(self):
        if not self.closed:
            return self.money
        else:
            raise ValueError("Account closed.")

    def open(self):
        if not self.closed:
            raise ValueError("Can't open an account twice.")
        else:
            self.closed = False

    def deposit(self, amount):
        if not self.closed:
            if amount < 0:
                raise ValueError("Can't deposit negative funds.")
            else:
                self.money += amount
        else:
            raise ValueError("Can't deposit into closed account.")

    def withdraw(self, amount):
        if not self.closed:
            if self.money - amount < 0:
                raise ValueError("Not enough funds.")
            elif amount < 0:
                raise ValueError("Can't withdraw negative funds.")
            else:
                self.money -= amount
        else:
            raise ValueError("Can't withdraw from closed account.")

    def close(self):
        if self.closed:
            raise ValueError("Account isn't open.")
        else:
            self.closed = True
            self.money = 0

