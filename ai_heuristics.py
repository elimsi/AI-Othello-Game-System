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
                    add = sideVal
                else:
                    add = -adjacentVal
            elif (x == 7 and y == 6) or (x == 6 and 6 <= y <= 7):
                if array[7][7] == colour:
                    add = sideVal
                else:
                    add = -adjacentVal
                    
            # Edge tiles
            elif (x == 0 and 1 < y < 6) or (x == 7 and 1 < y < 6) or (y == 0 and 1 < x < 6) or (y == 7 and 1 < x < 6):
                add = sideVal
                
            # Corner tiles
            elif (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                add = cornerVal

            if array[x][y] == colour:
                score += add
            elif array[x][y] == opponent:
                score -= add

    return score

def get_mobility(board, player):
    opponent = 1 if player == 2 else 2
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    valid_count = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] != 0: continue
            valid = False
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                    while 0 <= r < 8 and 0 <= c < 8:
                        r += dr
                        c += dc
                        if r < 0 or r >= 8 or c < 0 or c >= 8 or board[r][c] == 0:
                            break
                        if board[r][c] == player:
                            valid = True
                            break
                    if valid: break
            if valid:
                valid_count += 1
    return valid_count

def finalHeuristic(array, player):
    # Determine the current move number by counting pieces on board
    # Game starts with 4 pieces
    pieces_count = np.count_nonzero(array)
    moves = pieces_count - 4

    if moves <= 8:
        numMoves = get_mobility(array, player)
        return numMoves + decentHeuristic(array, player)
    elif moves <= 52:
        return decentHeuristic(array, player)
    elif moves <= 58:
