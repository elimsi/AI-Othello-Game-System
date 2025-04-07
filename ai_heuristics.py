import numpy as np

def dumbScore(array, player):
    score = 0
    colour = player
    opponent = 1 if player == 2 else 2

    for x in range(8):
        for y in range(8):
            if array[x][y] == colour:
                score += 1
            elif array[x][y] == opponent:
                score -= 1
    return score

def slightlyLessDumbScore(array, player):
    score = 0
    colour = player
    opponent = 1 if player == 2 else 2

