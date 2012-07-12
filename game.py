import board
import state

def play():
    b = board.init()
    for round in range(1,9):
        if state.won(b):
            break
