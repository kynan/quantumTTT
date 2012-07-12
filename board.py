import string

faux_board = [
    [],
    [],
    [0, 2],
    [0],
    [1, 2],
    [1],
    [],
    [],
    []
]

def draw(board):
    line = []
    for i in range(9):
        value = board[i]
        if not value:
            val_to_display = ' '
        elif isinstance(value, str):
            val_to_display = ' %s ' % value
        else:
            vals = []
            for v in value:
                token = 'X'
                if v % 2:
                    token = 'O'
                vals.append('%s%d' % (token, v))
            val_to_display = ', '.join(vals)
        line.append(string.center(val_to_display, 16))
        if i in [2, 5]:
            line.append('\n-----------------------------------------------------------\n')
        elif i < 8:
            line.append(' || ')
    print ''.join(line)

def init():
    return [[]]*9
