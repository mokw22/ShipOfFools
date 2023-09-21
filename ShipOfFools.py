from random import randint


class Die:
    """Represent a six-sided die with numbers 1-6
       Attrinutes: _value(int) gives the current value of the die.
    """
    def __init__(self):

        self._value = 1
        self.roll()

    def get_value(self):
        """Get the value of the die.
           Return the value of the die.
        """
        return self._value

    def roll(self):
        """Generate a random value between 1 and 6."""
        self._value = randint(1, 6)


class DiceCup:
    """Represent a cup containing 5 Die objects
       Attributes: _dice(list): A list of 5 Die objects
                   _locked(list): A list of 5 False boolean values indicating
                                  that each Die is not locked.
    """
    def __init__(self):
        self._dice = []
        for _ in range(5):
            self._dice.append(Die())
        self._locked = [False] * 5

    def roll(self):
        """Roll the Die object if not locked"""
        for i in range(5):
            if not self._locked[i]:
                self._dice[i].roll()

    def die_value(self, index):
        """Return the value of a specific Die index from the list"""
        return self._dice[index].get_value()

    def bank(self, index):
        """Lock a Die when it's index has a True value"""
        self._locked[index] = True

    def release(self, index):
        """Unlock a Die when it's index has a False value"""
        self._locked[index] = False

    def is_banked(self, index):
        """Retuen the boolean value of a specific index from the list"""
        return self._locked[index]

    def release_all(self):
        """Unlock all dice"""
        self._locked = [False] * 5


class ShipOfFoolsGame:
    """Represent a game of shipoffools
       Attributes: _cup(Dicecup): The cup of Dice used in the game
                   winning_score(int): The score needed to win the game
    """
    def __init__(self):

        self._cup = DiceCup()
        self.wining_score = 50

    def turn(self):
        """Throws the cup 3 rounds. Lock respective dice with value
           6,5,4. IF not these values return 0. IF first case lock 2 sixes on
           the other two dice until last round and give the sum 12. If not
           unlock only these two dice and sum their value."""
        value = self._cup.die_value
        six = False
        five = False
        four = False
        six2 = False
        six3 = False
        count = 0
        six_count = 0
        self._cup.release_all()
        for round_number in range(3):
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
                                six_count += 1
                                self._cup.bank(j)
                                six2 = True
                            elif six2 and not six3 and value(j) == 6:
                                count += value(j)
                                six_count += 1
                                self._cup.bank(j)
                                six3 = True
                            elif round_number == 1 and six_count < 2:
                                self._cup.release(j)
                            else:
                                count += value(j)
                    return count
        return count


class Player:
    """Represent a player in the shipoffoolsgame
       Attributes: _name(str): Name of the player
                   _score(int): player's score is 0"""
    def __init__(self, name):
        self._name = name
        self._score = 0

    def current_score(self):
        """Return the current score"""
        return self._score

    def get_name(self):
        """Return the name"""
        return self._name

    def reset_score(self):
        """Reset the score to 0"""
        self._score = 0

    def play_turn(self, game):
        """Increase player score after each shipoffools turn"""
        score = game.turn()
        self._score += score


class PlayRoom:
    """Represent a room where the game is running
       Attributes: _game(shipoffoolsgame) the game in the room
                   _players(list): a list of player in the room
                   _winner(player): the winner
    """
    def __init__(self):
        self._game = ShipOfFoolsGame()
        self._players = []
        self._winner = None

    def set_game(self, game):
        """Add the game"""
        self._game = game

    def add_player(self, player):
        """Add players to the list"""
        self._players.append(player)

    def reset_scores(self):
        """Reset all players score in the list"""
        for player in self._players:
            player.reset_score()

    def game_finished(self):
        """Check for a winner by comparing player's score
           in the list with the winning score '50'
        """
        game_finished = True
        for player in self._players:
            if player.current_score() >= self._game.wining_score:
                self._winner = player
                return game_finished
        return False

    def play_round(self):
        """All players in the list playing each round until
           a player rach or have more than 50 points"""
        for player in self._players:
            player.play_turn(ShipOfFoolsGame())
        self.game_finished()

    def print_scores(self):
        """Print each player's name and its current score in the list"""
        for player in self._players:
            print(player.get_name() + ':', player.current_score(),
                  'points!')
            print()

    def print_winner(self):
        """Print the name of the winner"""
        if self._winner:
            print('The winner is ' + self._winner.get_name() + ('!'))


if __name__ == "__main__":
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player('Noora'))
    room.add_player(Player('Ali'))
    room.add_player(Player('Sidra'))
    room.add_player(Player('Rasmus'))
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()
