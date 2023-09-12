from random import randint


class Die:
    def __init__(self):
        self._value = 1
        self.roll()

    def get_value(self):
        return self._value

    def roll(self):
        self._value = randint(1, 6)


class DiceCup:
    def __init__(self):
        self._dice = []
        for _ in range(5):
            self._dice.append(Die())
        self._locked = [False] * 5

    def roll(self):
        for i in range(5):
            if not self._locked[i]:
                self._dice[i].roll()

    def die_value(self, index):
        return self._dice[index].get_value()

    def bank(self, index):
        self._locked[index] = True

    def release(self, index):
        self._locked[index] = False

    def is_banked(self, index):
        return self._locked[index]

    def release_all(self):
        self._locked[False] * 5
