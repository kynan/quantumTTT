import board
import state

def turn(board):
    return board

def collapse(board, cycle):
    return board

def play():
    b = board.init()
    for round in range(1,9):
        b = turn(b)
        board.draw(b)
        c = state.find_cycle(b)
        if c:
            b = collapse(board, cycle)
        if state.won(b):
            print "Player %d won!" % ((round % 2) + 1)
            break
