from random import randint


class Die:
    def __init__(self):
        self._value = 1
        self.roll()

    def get_value(self):
        return self._value

    def roll(self):
        self._value = randint(1, 6)