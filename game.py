import board
import state

def turn(board):
    return board

def play():
    b = board.init()
    for round in range(1,9):
        b = turn(b)
        board.draw(b)
        c = state.find_cycle(b)
        if c:
            pass
        if state.won(b):
            break
