import numpy as np

EMPTY = 0
BLACK = 1
WHITE = 2
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

class OthelloGame:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)
        self.board[3, 3] = self.board[4, 4] = WHITE
        self.board[3, 4] = self.board[4, 3] = BLACK
        self.current_player = BLACK

    def get_opponent(self, player):
        return BLACK if player == WHITE else WHITE

    def is_valid_move(self, board, player, row, col):
        if board[row, col] != EMPTY:
            return False
