import math


def full(board):  # returns true if the board is full
    for n in range(3):
        for m in range(3):
            if board[n][m] == 0:
                return False
    return True


def win(board):  # determines win based on possible board outcomes
    for row in board:  # horizontals
        if row[0] == row[1] == row[2]:
            if row[0] != 0:
                return True
    for n in range(3):  # verticals
        if board[0][n] == board[1][n] == board[2][n]:
            if board[0][n] != 0:
                return True
    if board[0][0] == board[1][1] == board[2][2]:  # diagonal 1
        if board[1][1] != 0:
            return True
    if board[0][2] == board[1][1] == board[2][0]:  # diagonal 2
        if board[1][1] != 0:
            return True
    return False


def zeros(board):
    z = 0
    for row in board:
        for space in row:
            if space == 0:
                z += 1
    return z


def minimax(board, depth, player):
    if player:  # should initially be false
        best = -math.inf
    else:
        best = math.inf  # set best as a low/high number to see if it will be beaten

    if win(board):
        return (-10 - depth) if player else (10 + depth)

    if full(board):
        return 0

    if depth == 0:
        return 0

    # iterates through board
    for u in range(3):
        for v in range(3):
            if board[u][v] == 0:
                board[u][v] = 1 if player else -1
                score = minimax(board, depth - 1, not player)
                board[u][v] = 0
                best = max(best, score) if player else min(best, score)

    return best


def bestMove(board, depth):
    play = [-1, -1, 20]
    for u in range(3):
        for v in range(3):
            if board[u][v] == 0:
                board[u][v] = -1
                score = minimax(board, depth, True)
                print(score)
                board[u][v] = 0
                if score < play[2]:
                    play = [u, v, score]
    return play
