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
        self.wining_score = 50

    def turn(self):
        value = self._cup.die_value
        six = False
        five = False
        four = False
        six2 = False
        six3 = False
        count = 0
        self._cup.release_all()
        for _ in range(3):
            for i in range(5):
                self._cup.roll()
                if not six and value(i) == 6:
                    self._cup.bank(i)
                    six = True
                if six and not five and value(i) == 5:
                    self._cup.bank(i)
                    five = True
                if six and five and not four and value(i) == 4:
                    self._cup.bank(i)
                    four = True
                if six and five and four:
                    for j in range(5):
                        if not self._cup.is_banked(j):
                            if not six2 and value(j) == 6:
                                count += value(j)
                                self._cup.bank(j)
                                six2 = True
                            elif six2 and not six3 and value(j) == 6:
                                count += value(j)
                                self._cup.bank(j)
                                six3 = True
                            else:
                                count += value(j)
                    return count
        return count


class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    def current_score(self):
        return self._score

    def get_name(self):
        return self._name

    def reset_score(self):
        self._score = 0

    def play_turn(self, game):
        score = game.turn()
        self._score += score


class PlayRoom:
    def __init__(self):
        self._game = ShipOfFoolsGame()
        self._players = []
        self._winner = None

    def set_game(self, game):
        self._game = game

    def add_player(self, player):
        self._players.append(player)

    def reset_scores(self):
        for player in self._players:
            player.reset_score()

    def game_finished(self):
        game_finished = True
        for player in self._players:
            if self.current_score() >= self._game.wining_score:
                self._winner = player
                return game_finished
        return False

    def play_round(self):
        for player in self._players:
            player.play_turn(game)
        self.game_finished()

    def print_scores(self):
        for player in self._players:
            print(player.get_name()+':'+str(player.current_score()+'points!'))
            print()

    def print_winner(self):
        if self._winner:
            print('The winner is '+self._winner.get_name()+('!'))


game = ShipOfFoolsGame()
score = game.turn()
print(score)
