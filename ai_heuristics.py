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

    for x in range(8):
        for y in range(8):
            add = 1
            if (x == 0 and 1 < y < 6) or (x == 7 and 1 < y < 6) or (y == 0 and 1 < x < 6) or (y == 7 and 1 < x < 6):
                add = 3
            elif (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                add = 5

            if array[x][y] == colour:
                score += add
            elif array[x][y] == opponent:
                score -= add
    return score

def decentHeuristic(array, player):
    score = 0
    cornerVal = 25
    adjacentVal = 5
    sideVal = 5

    colour = player
    opponent = 1 if player == 2 else 2

    for x in range(8):
        for y in range(8):
            add = 1
            
            # Corner adjacent penalties
            if (x == 0 and y == 1) or (x == 1 and 0 <= y <= 1):
                if array[0][0] == colour:
                    add = sideVal
                else:
                    add = -adjacentVal
            elif (x == 0 and y == 6) or (x == 1 and 6 <= y <= 7):
                if array[0][7] == colour:
                    add = sideVal
                else:
                    add = -adjacentVal
            elif (x == 7 and y == 1) or (x == 6 and 0 <= y <= 1):
                if array[7][0] == colour:
