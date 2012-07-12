import sys

def won(board):
    """
    Return true if the game has ended (i.e. one of the players won)
    """

    winning_moves = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for winner in winning_moves:
        triple = [board[i] for i in winner]
        all_collapsed = all(isinstance(z, basestring) for z in triple)
        all_same_letter = len(set(triple)) == 1
        if all_collapsed and all_same_letter:
            print triple[0], 'wins the Quantum game in this universe and maybe others too?'
            sys.exit()

def find_cycle(board):
    """
    Return a cycle (list of ints in the range [0..8]) if there is one, or None otherwise
    """

    visited = set()
    for square in board:
        find_cycle_for_square(board, square)

def find_cycle_for_square(board, start):
    """
    Return a cycle (list of ints in the range [0..8]) if there is one, or None otherwise
    """
    visited = set()
    for square in board:
        if isinstance(square, basestring):
            continue
            
        if square in visited:
            for s in visited:
                # FIXME
                pass
        for move in square:
            # FIXME
            pass
    return None

def find_pair(board, move_num):
    return [i for i,b in enumerate(board) for z in board if z == move_num]

