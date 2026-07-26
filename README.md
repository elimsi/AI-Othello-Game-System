# 🧠 AI Othello Game System

A modular, Python-based testbed for analyzing and comparing Artificial Intelligence strategies in the game of Othello (Reversi). Developed as an independent research project.

## 🎯 Project Goals
This project was built to practically demonstrate the mathematical efficiency and decision-making capabilities of different AI search algorithms. It allows users to play against various AIs and observe their performance metrics in real-time.

## 🚀 Features
- **Modular Architecture**: Clean separation between the core Othello rules, UI rendering, and AI logic.
- **AI Difficulty Selector**: Play against 4 different AI tiers:
  - **IA Stupide**: Plays completely randomly.
  - **IA Moins Stupide**: Uses a greedy 1-ply search with a basic positional heuristic.
  - **IA Minimax**: Searches 4 moves deep using the standard Minimax algorithm.
  - **IA Alpha-Beta**: Searches 4 moves deep using Alpha-Beta pruning for massive performance gains.
- **Real-Time Analytics HUD**:
  - ⏱️ **Execution Time**: Measures how many milliseconds the AI takes to compute its move.
  - 🌳 **Nodes Explored**: Tracks the number of game states evaluated in the search tree (highlighting the pruning efficiency of Alpha-Beta over standard Minimax).
  - 📊 **Board Score**: Displays the AI's internal heuristic evaluation of the current board state.

## 🧩 Code Structure
- `game_engine.py`: Contains the `OthelloGame` class. Handles the pure logic (valid moves, piece flipping, win states).
- `ai_heuristics.py`: Contains the advanced board evaluation functions (`decentHeuristic`, `finalHeuristic`), incorporating edge/corner weights and mobility tracking.
- `ai_agents.py`: Contains the AI decision-making classes (`RandomAI`, `HeuristicAI`, `MinimaxAI`, `AlphaBetaAI`).
- `main_gui.py`: The Tkinter-based graphical user interface that ties the engine and agents together.

## 🎮 How to Run
Ensure you have Python and `numpy` installed.

```bash
pip install numpy
python main_gui.py
```
Enjoy playing against the Alpha-Beta algorithm!
