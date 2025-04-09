import random
from game_engine import BLACK, WHITE
from ai_heuristics import finalHeuristic, slightlyLessDumbScore

class AIAgent:
    def __init__(self, color):
        self.color = color

    def get_move(self, game_state):
        pass

class RandomAI(AIAgent):
    def get_move(self, game_state):
        moves = game_state.get_valid_moves(game_state.board, self.color)
        if moves:
            return random.choice(moves)
        return None

