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
