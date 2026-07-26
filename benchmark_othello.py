import matplotlib.pyplot as plt
from game_engine import OthelloGame, BLACK, WHITE
from ai_agents import MinimaxAI, AlphaBetaAI
import numpy as np

def is_game_over(game):
    return not game.get_valid_moves(game.board, BLACK) and not game.get_valid_moves(game.board, WHITE)

def run_benchmark(num_games=5, depth=4):
    minimax_nodes = []
    alphabeta_nodes = []
    
    for i in range(num_games):
        game = OthelloGame()
        moves_played = 0
        
        while not is_game_over(game) and moves_played < 20: # Just sample 20 moves per game
            valid_moves = game.get_valid_moves(game.board, game.current_player)
            if not valid_moves:
                game.current_player = game.get_opponent(game.current_player)
                continue
                
            # Both evaluate the exact same state
            if game.current_player == WHITE:
                ai_mm = MinimaxAI(WHITE, depth=depth)
                ai_ab = AlphaBetaAI(WHITE, depth=depth)
                
                # Ask both what they think about WHITE's turn
                move_mm = ai_mm.get_move(game)
                nodes_mm = ai_mm.nodes_explored
                
                move_ab = ai_ab.get_move(game)
                nodes_ab = ai_ab.nodes_explored
                
                minimax_nodes.append(nodes_mm)
                alphabeta_nodes.append(nodes_ab)
                
            # Actually play AlphaBeta to advance the game quickly
            ab_player = AlphaBetaAI(game.current_player, depth=depth)
            move = ab_player.get_move(game)
            if move:
                game.play_move(move[0], move[1])
            else:
                game.current_player = game.get_opponent(game.current_player)
                
            moves_played += 1
            if game.current_player == BLACK: # Because it switched after play_move
                print(f"Game {i+1}, Move {moves_played}: Minimax={minimax_nodes[-1] if minimax_nodes else 0}, AB={alphabeta_nodes[-1] if alphabeta_nodes else 0}")

    avg_mm = np.mean(minimax_nodes)
    avg_ab = np.mean(alphabeta_nodes)
    
    print(f"Average Minimax nodes/move: {avg_mm:.0f}")
    print(f"Average Alpha-Beta nodes/move: {avg_ab:.0f}")
    print(f"Reduction factor: {avg_mm / avg_ab:.1f}x")
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(["Minimax", "Alpha-Beta"], [avg_mm, avg_ab], color=["#e74c3c", "#2ecc71"])
    plt.title(f"Average Nodes Explored Per Move (Depth {depth})", fontsize=14)
    plt.ylabel("Nodes Explored", fontsize=12)
    
    # Add text labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + (avg_mm*0.02), f"{yval:,.0f}", ha='center', va='bottom', fontsize=12, fontweight='bold')
        
    plt.text(0.5, avg_mm * 0.8, f"🔥 {avg_mm/avg_ab:.1f}x Reduction", ha='center', fontsize=16, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

    plt.tight_layout()
    plt.savefig("nodes_chart.png", dpi=150)
    print("Saved nodes_chart.png")

if __name__ == "__main__":
    run_benchmark(num_games=3, depth=4)
