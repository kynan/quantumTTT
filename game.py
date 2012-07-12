import copy

import board
import state

def playernum(r):
    return (r % 2) + 1

def read_pos(prompt):
    p = int(raw_input(prompt))
    if p in range(9):
        return p
    else:
        print "Illegal input! Valid range: 0-8."
        return read_pos(prompt)

def read_sym(prompt):
    p = raw_input(prompt)
    if p in ['X','O']:
        return p
    else:
        print "Illegal input! Valid inputs: X, O."
        return read_pos(prompt)

def turn(r, board):
    print "Player %d's turn:" % playernum(r)
    p1 = read_pos('Enter first move [0-8] ')
    p2 = read_pos('Enter second move [0-8] ')
    newboard = copy.deepcopy(board)
    try:
        newboard[p1].append(r)
        newboard[p2].append(r)
    except:
        print "Field has already collapsed"
        return turn(r, board)
    return newboard

def prompt_resolve(r, cycle):
    print "Player %d, collapse the following cycle:" % playernum(r+1), cycle
    pos = read_pos("Enter a position ")
    sym = read_sym("Enter a symbol (X/O) ")
    sym_parity = {'X':0 , 'O':1}[sym]
    if not sym_parity in [i % 2 for i in  board[pos]]:
        print 'Illegal choice'
        return prompt_resolve(r, cycle)
    return pos, sym

def play():
    b = board.init()
    for r in range(9):
        b = turn(r, b)
        board.draw(b)
        c = state.find_cycle(b)
        if c:
            pos, symbol = prompt_resolve(r, c)
            b = state.collapse(b, pos, symbol)
        if state.won(b):
            print "Player %d won!" % playernum(r)
            break
