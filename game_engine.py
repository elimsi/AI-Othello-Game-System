import numpy as np

EMPTY = 0
BLACK = 1
WHITE = 2
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

class OthelloGame:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)
