import math

"""

No algorithm yet LOL

minimax(state, depth, player)

if (player = max) then
    best = [null, -infinity]
else
    best = [null, +infinity]

if (depth = 0 or gameover) then
    score = evaluate this state for player
    return [null, score]

for each valid move m for player in state s do
    execute move m on s
    [move, score] = minimax(s, depth - 1, -player)
    undo move m on s

    if (player = max) then
        if score > best.score then best = [move, score]
    else
        if score < best.score then best = [move, score]

return best
end
"""


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
    # upon call, depth should be _ and player should be False
    moves = []
    if player:
        best = [None, -math.inf]
    else:
        best = [None, math.inf]
    if depth == 0:
        if win(board) and player:
            return [None, -1]
        elif win(board) and not player:
            return [None, 1]
        else:
            return [None, 0]

    u = -1
    for row in board:
        u += 1
        v = -1
        for space in row:
            v += 1
            if space == 0:
                moves.append([u, v])
    for move in moves:
        attempt = board
        if player:  # adds a cross (1) to the board
            attempt[move[0]][move[1]] = 1
        else:  # adds a cross (1) to the board
            attempt[move[0]][move[1]] = 2
        print(attempt)
        [move, score] = minimax(attempt, depth - 1, False if player else True)
        print(move)

        if player and score > best[1]:
            best = [move, score]
        if not player and score < best[1]:
            best = [move, score]

    return best
