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