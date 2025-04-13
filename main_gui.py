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

