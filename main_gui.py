import tkinter as tk
import time
import numpy as np
from game_engine import OthelloGame, BLACK, WHITE
from ai_agents import RandomAI, HeuristicAI, MinimaxAI, AlphaBetaAI
from ai_heuristics import finalHeuristic

class MainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Othello AI Simulator (TIPE)")
        self.master.geometry("500x600")
        self.master.configure(bg="#2c3e50")
        self.game = OthelloGame()
        self.ai = None
        self.setup_ui()

    def setup_ui(self):
        # Header Frame
        header_frame = tk.Frame(self.master, bg="#2c3e50")
        header_frame.pack(side=tk.TOP, fill=tk.X, pady=15)

        tk.Label(header_frame, text="IA Opponent:", bg="#2c3e50", fg="white", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=10)
        
        self.ai_var = tk.StringVar(value="IA Alpha-Beta")
        options = ["IA Stupide", "IA Moins Stupide", "IA Minimax", "IA Alpha-Beta"]
        self.ai_dropdown = tk.OptionMenu(header_frame, self.ai_var, *options, command=self.set_ai)
        self.ai_dropdown.config(bg="#34495e", fg="white", font=("Arial", 10))
        self.ai_dropdown.pack(side=tk.LEFT, padx=10)

        restart_btn = tk.Button(header_frame, text="Restart Game", command=self.restart_game, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"))
        restart_btn.pack(side=tk.RIGHT, padx=15)

        # Canvas for the Board
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="#27ae60", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.handle_click)

        # Stats Frame (HUD)
        stats_frame = tk.Frame(self.master, bg="#34495e", bd=2, relief=tk.GROOVE)
        stats_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

        # Left Column for HUD
        left_stats = tk.Frame(stats_frame, bg="#34495e")
        left_stats.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.time_label = tk.Label(left_stats, text="⏱️ AI Time: 0 ms", bg="#34495e", fg="#f1c40f", font=("Arial", 11, "bold"))
        self.time_label.pack(anchor="w")
        
        self.nodes_label = tk.Label(left_stats, text="🌳 Nodes Explored: 0", bg="#34495e", fg="#ecf0f1", font=("Arial", 11))
        self.nodes_label.pack(anchor="w")

        # Right Column for HUD
        right_stats = tk.Frame(stats_frame, bg="#34495e")
        right_stats.pack(side=tk.RIGHT, padx=10, pady=10)

        self.score_label = tk.Label(right_stats, text="📊 Board Score: 0", bg="#34495e", fg="#3498db", font=("Arial", 11, "bold"))
        self.score_label.pack(anchor="e")

        self.status_label = tk.Label(right_stats, text="Your Turn (Black)", bg="#34495e", fg="#2ecc71", font=("Arial", 11, "bold"))
        self.status_label.pack(anchor="e")

        self.set_ai()
        self.draw_board()

    def set_ai(self, *args):
        choice = self.ai_var.get()
        if choice == "IA Stupide": self.ai = RandomAI(WHITE)
        elif choice == "IA Moins Stupide": self.ai = HeuristicAI(WHITE)
        elif choice == "IA Minimax": self.ai = MinimaxAI(WHITE, depth=4)
        elif choice == "IA Alpha-Beta": self.ai = AlphaBetaAI(WHITE, depth=4)

    def restart_game(self):
        self.game = OthelloGame()
        self.status_label.config(text="Your Turn (Black)", fg="#2ecc71")
        self.time_label.config(text="⏱️ AI Time: 0 ms")
        self.nodes_label.config(text="🌳 Nodes Explored: 0")
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="#2c3e50", width=2)
                
                piece = self.game.board[row, col]
                if piece == BLACK:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="#111", outline="#000")
                elif piece == WHITE:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="#eee", outline="#ccc")
        
        # Highlight valid moves for current player
        if self.game.current_player == BLACK:
            moves = self.game.get_valid_moves(self.game.board, BLACK)
            for r, c in moves:
                x1, y1 = c * 50, r * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_oval(x1 + 20, y1 + 20, x2 - 20, y2 - 20, fill="#2ecc71", outline="")

        score = finalHeuristic(self.game.board, WHITE)
        self.score_label.config(text=f"📊 Board Score: {score}")
        self.master.update()

    def handle_click(self, event):
        if self.game.current_player == BLACK:
            col = event.x // 50
            row = event.y // 50
            if self.game.play_move(row, col):
                self.status_label.config(text="AI is thinking...", fg="#e67e22")
                self.draw_board()
                
                if self.game.get_valid_moves(self.game.board, WHITE):
                    self.master.after(50, self.ai_move)
                elif self.game.get_valid_moves(self.game.board, BLACK):
                    self.game.current_player = BLACK # White skips
                    self.status_label.config(text="White skipped. Your Turn", fg="#2ecc71")
                    self.draw_board()
                else:
                    self.end_game()

    def ai_move(self):
        start_time = time.time()
        move = self.ai.get_move(self.game)
        elapsed_ms = int((time.time() - start_time) * 1000)
        
        if move:
            self.game.play_move(move[0], move[1])
            self.time_label.config(text=f"⏱️ AI Time: {elapsed_ms} ms")
            
            nodes = getattr(self.ai, 'nodes_explored', 0)
            self.nodes_label.config(text=f"🌳 Nodes Explored: {nodes}")
            
            if self.game.get_valid_moves(self.game.board, BLACK):
                self.status_label.config(text="Your Turn (Black)", fg="#2ecc71")
            else:
                if self.game.get_valid_moves(self.game.board, WHITE):
                    self.game.current_player = WHITE # Black skips
                    self.status_label.config(text="Black skipped. AI Turn", fg="#e67e22")
                    self.master.after(500, self.ai_move)
                else:
                    self.end_game()
            
            self.draw_board()
            
    def end_game(self):
        black_score = np.sum(self.game.board == BLACK)
        white_score = np.sum(self.game.board == WHITE)
        
        if black_score > white_score:
            msg = "You Win! 🎉"
            color = "#2ecc71"
        elif white_score > black_score:
            msg = "AI Wins! 🤖"
            color = "#e74c3c"
        else:
            msg = "It's a Draw! 🤝"
            color = "#f1c40f"
            
        self.status_label.config(text=msg, fg=color)
        print(f"Game Over! Black: {black_score}, White: {white_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
