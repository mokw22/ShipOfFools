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
        self._locked = [False] * 5


class ShipOfFoolsGame:
    def __init__(self):
        self._cup = DiceCup()
        self.wining_score = 0

    def turn(self):
        six = False
        five = False
        four = False
        count = 0
        self._cup.release_all()
        for _ in range(3):
            for i in range(5):
                self._cup.roll()
                if not six and self._cup.die_value(i) == 6:
                    self._cup.bank(i)
                    six = True
                if six and not five and self._cup.die_value(i) == 5:
                    self._cup.bank(i)
                    five = True
                if six and five and not four and self._cup.die_value(i) == 4:
                    self._cup.bank(i)
                if six and five and four:
                    for j in range(5):
                        if not self._cup.is_banked(j):
                            count += self._cup.die_value(j)
        return count


class Player:
    def __init__(self, name='Bot', score=0):
        self._name = name
        self._score = score

    def current_score(self):
        return self._score

    def get_name(self):
        return self._name

    def reset_score(self):
        self._score = 0

    def play_turn(self, ShipOfFools):
        pass


class PlayRoom:
    def __init__(self):
        self._game = ShipOfFoolsGame()
        self._players = [Player()]
        self._winner = None
    
    def set_game(self, game):
        pass

    def add_player(self, player):
        pass

    def reset_scores(self):
        pass

    def play_round(self):
        pass

    def game_finished():
        pass

    def print_scores():
        pass

    def print_winner():
        pass


print(DiceCup())
