import copy

import board
import state

def turn(board):
    p1 = raw_input('Enter first move [0-8] ')
    p2 = raw_input('Enter second move [0-8] ')
    newboard = copy.deepcopy(board)
    try:
        newboard[p1].append(r)
        newboard[p2].append(r)
    except:
        print "Field has already collapsed"
        return turn(r, board)
    return newboard

def collapse(board, cycle):
    return board

def play():
    b = board.init()
    for r in range(1,9):
        b = turn(r, b)
        board.draw(b)
        c = state.find_cycle(b)
        if c:
            b = collapse(board, cycle)
        if state.won(b):
            print "Player %d won!" % ((round % 2) + 1)
            break
