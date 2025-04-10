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

class HeuristicAI(AIAgent):
    # Uses slightlyLessDumbScore to greedily pick the best immediate move (1-ply)
    def get_move(self, game_state):
        moves = game_state.get_valid_moves(game_state.board, self.color)
        if not moves: return None
        best_score = float('-inf')
        best_move = None
        for r, c in moves:
            new_board = game_state.apply_move(game_state.board, self.color, r, c)
            score = slightlyLessDumbScore(new_board, self.color)
            if score > best_score:
                best_score = score
                best_move = (r, c)
        return best_move

class MinimaxAI(AIAgent):
    def __init__(self, color, depth=4):
        super().__init__(color)
        self.depth = depth
        self.nodes_explored = 0

    def get_move(self, game_state):
        self.nodes_explored = 0
        _, best_move = self.minimax(game_state, game_state.board, self.depth, self.color, True)
        return best_move

    def minimax(self, game_state, board, depth, player, is_maximizing):
