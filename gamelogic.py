from typing import List

class CannotPlayHere(Exception):

    def __init__(self, x, y):
        super().__init__(f"Cannot play here: {x},{y}")

class PlayerWon(Exception):

    def __init__(self, player, a, b, c, symbol):
        super().__init__(f"Player {player} won")
        self.a = a
        self.b = b
        self.c = c
        self.symbol = symbol

class GameLogic:

    def __init__(self):
        self.board: List[List] = [[-1, -1, -1],
                                  [-1, -1, -1],
                                  [-1, -1, -1]]
        self.current_player = 0

    def play(self, x, y):
        if self.board[y][x] != -1:
            raise CannotPlayHere(x, y)

        current_player = self.current_player
        self.board[y][x] = current_player
        self.check_win()
        self.change_players()
        self.print_board()
        return self.player_to_symbol(current_player)

    def change_players(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0

    def check_win(self):
        n = self.current_player
        symbol = self.player_to_symbol(n)
        # ver por linha

        for y in range(len(self.board)):
            if self.board[y] == [n, n, n]:
                raise PlayerWon(self.current_player, (0, y),
                                (1, y), (2, y), symbol)

        for x in range(len(self.board)):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] == self.current_player:
                raise PlayerWon(
                    self.current_player, (x, 0), (x, 1), (x, 2), symbol)

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            raise PlayerWon(self.current_player,
                            (0, 0), (1, 1), (2, 2), symbol)

        if self.board[2][0] == self.board[1][1] == self.board[0][2] == self.current_player:
            raise PlayerWon(self.current_player,
                            (0, 2), (1, 1), (2, 0), symbol)

    @classmethod
    def player_to_symbol(cls, player):
        if player == 0:
            return "O"
        elif player == 1:
            return "X"
        else:
            return " "

    def print_board(self):
        for y in self.board:
            for x in y:
                print(x, end="")
            print()
