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
