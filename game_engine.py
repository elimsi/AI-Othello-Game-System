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
        opponent = self.get_opponent(player)
        for dr, dc in DIRECTIONS:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and board[r, c] == opponent:
                while 0 <= r < 8 and 0 <= c < 8:
                    r += dr
                    c += dc
                    if r < 0 or r >= 8 or c < 0 or c >= 8 or board[r, c] == EMPTY:
                        break
                    if board[r, c] == player:
                        return True
        return False

    def get_valid_moves(self, board, player):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(board, player, row, col):
                    valid_moves.append((row, col))
        return valid_moves
