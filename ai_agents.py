import random
from game_engine import BLACK, WHITE
from ai_heuristics import finalHeuristic, slightlyLessDumbScore

class AIAgent:
    def __init__(self, color):
        self.color = color

    def get_move(self, game_state):
