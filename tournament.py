from game_engine import OthelloGame, BLACK, WHITE
from ai_agents import RandomAI, HeuristicAI, MinimaxAI, AlphaBetaAI
import numpy as np

def is_game_over(game):
    return not game.get_valid_moves(game.board, BLACK) and not game.get_valid_moves(game.board, WHITE)

def get_winner(game):
    black_score = np.sum(game.board == BLACK)
    white_score = np.sum(game.board == WHITE)
    if black_score > white_score:
        return BLACK
    elif white_score > black_score:
        return WHITE
    return 0

def play_match(AgentClass1, AgentClass2, depth=2):
    game = OthelloGame()
    agent1 = AgentClass1(BLACK) if AgentClass1 in [RandomAI, HeuristicAI] else AgentClass1(BLACK, depth=depth)
    agent2 = AgentClass2(WHITE) if AgentClass2 in [RandomAI, HeuristicAI] else AgentClass2(WHITE, depth=depth)
    
    while not is_game_over(game):
        valid_moves = game.get_valid_moves(game.board, game.current_player)
        if not valid_moves:
            game.current_player = game.get_opponent(game.current_player)
            continue
            
        if game.current_player == BLACK:
            move = agent1.get_move(game)
        else:
            move = agent2.get_move(game)
            
        if move:
            game.play_move(move[0], move[1])
        else:
            game.current_player = game.get_opponent(game.current_player)
            
    return get_winner(game)

if __name__ == "__main__":
    agents = [
        ("Random", RandomAI),
        ("Greedy", HeuristicAI),
        ("Minimax", MinimaxAI),
        ("AlphaBeta", AlphaBetaAI)
    ]
    
    # We will simulate a smaller number of games to save execution time,
    # but normally this would be 100.
    GAMES_PER_MATCHUP = 5 
    
    matrix = np.zeros((len(agents), len(agents)))
    
    print("Running Tournament...")
    for i, (name1, Class1) in enumerate(agents):
        for j, (name2, Class2) in enumerate(agents):
            if i == j:
                matrix[i, j] = 50.0 # 50% against itself
                continue
            
            wins = 0
            for _ in range(GAMES_PER_MATCHUP):
                winner = play_match(Class1, Class2)
                if winner == BLACK:
                    wins += 1
            win_rate = (wins / GAMES_PER_MATCHUP) * 100
            matrix[i, j] = win_rate
            print(f"{name1} vs {name2}: {win_rate:.1f}% win rate")
            
    print("\nTournament Matrix (Row = Player 1, Col = Player 2):")
    print("--------------------------------------------------")
    print(f"{'':>12}", end="")
    for name, _ in agents:
        print(f"{name:>12}", end="")
    print()
    
    for i, (name1, _) in enumerate(agents):
        print(f"{name1:>12}", end="")
        for j in range(len(agents)):
            if i == j:
                print(f"{'--':>12}", end="")
            else:
                print(f"{matrix[i,j]:>11.1f}%", end="")
        print()
