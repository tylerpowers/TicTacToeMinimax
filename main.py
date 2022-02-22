import pygame as pg
from pygame.draw import *

first = True
user = True
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

pg.init()
pg.display.set_caption('Tic-Tac-Toe')
screen = pg.display.set_mode((800, 800))
screen.fill((250, 250, 250))


def win():  # determines win based on possible board outcomes
    global board
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


def full():
    global board
    for n in range(3):
        for m in range(3):
            if board[n][m] == 0:
                return False
    return True


def clean(pos):
    if pos[0] <= 300:
        u = 0
    elif pos[0] <= 500:
        u = 1
    else:
        u = 2
    if pos[1] <= 300:
        v = 0
    elif pos[1] <= 500:
        v = 1
    else:
        v = 2
    return v, u


def lines():
    pg.draw.line(screen, (0, 0, 0), (100, 300), (700, 300))
    pg.draw.line(screen, (0, 0, 0), (100, 500), (700, 500))
    pg.draw.line(screen, (0, 0, 0), (300, 100), (300, 700))
    pg.draw.line(screen, (0, 0, 0), (500, 100), (500, 700))


def circle(pos):  # draws circle (2) on board
    global board, user
    if board[pos[0]][pos[1]] == 0:
        board[pos[0]][pos[1]] = 2
        if pos[0] == 0:
            y = 200
        elif pos[0] == 1:
            y = 400
        else:
            y = 600
        if pos[1] == 0:
            x = 200
        elif pos[1] == 1:
            x = 400
        else:
            x = 600
        pg.draw.circle(screen, (250, 0, 0), (x, y), 90, 10)
        user = True
        print(x)


def cross(pos):
    global board, user
    if board[pos[0]][pos[1]] == 0:
        board[pos[0]][pos[1]] = 1
        if pos[0] == 0:
            y = 125
        elif pos[0] == 1:
            y = 325
        else:
            y = 525
        if pos[1] == 0:
            x = 125
        elif pos[1] == 1:
            x = 325
        else:
            x = 525
        pg.draw.line(screen, (0, 0, 250), (x, y), (x + 150, y + 150), 10)
        pg.draw.line(screen, (0, 0, 250), (x, y + 150), (x + 150, y), 10)
        user = False
        print(x)


def main():
    global first, board, user
    red = 0
    blue = 0
    while True:
        while not full() and not win():
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.display.quit()
                    exit()
                lines()
                pg.display.update()
                if event.type == pg.MOUSEBUTTONUP:
                    cross(clean(pg.mouse.get_pos())) if user else circle(clean(pg.mouse.get_pos()))
                    # this pos will eventually given by minimax alg                     ^^
                    print(board)
            pg.display.flip()
        if win():
            if user:
                red += 1
                print("Red Wins!")
                break
            else:
                blue += 1
                print("Blue Wins!")
                break
        else:
            print("Tie!")
            break
    exit(0)


if __name__ == "__main__":
    main()
