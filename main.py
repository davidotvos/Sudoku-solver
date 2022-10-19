#!/usr/bin/env python3

"""
Reads sudoku inputs from a file
:param: the name of the file
:return: list of ints
"""
def read_boards(filename):
    boards = []
    with open(filename, 'r') as f:
        boards = f.readlines()
        boards = [x.split(',')[0] for x in boards]
        return [n.replace('.', '0') for n in boards]


"""
Prints out a board in a readable format
:param board: list of ints
"""
def pretty_print(board):
    # rows
    for i in range(9):
        if i in [3,6]:
            print('------+-------+------')
        
        # cols
        for j in range(9):
            current = board[i*9 + j] + ' '

            if j in [2,5]:
                print(current, end='| ')
            elif j == 8:
                print(current)
            else:
                print(current, end='')


def row_valid(pos, board, input):
    row = pos // 9
    start_pos = row*9
    for i in range(start_pos, start_pos + 9):
        if board[i] == input:
            return False
    
    return True

def col_valid(pos, board, input):
    col = pos % 9
    for i in range(0, 9, 9):
        pass
    pass

def valid(board, pos, num):
    row = pos // 9
    col = pos % 9
    
    # check row
    currentRow = board[row*9: row*9+9]
    if str(num) in currentRow:
        return False

    
    # check column
    currentColumn = []
    for i in range(9):
        currentColumn.append(board[col + i*9])
    
    if str(num) in currentColumn:
        return False


def solve(pos, value):
    
    
    pass



def main():
    boards = read_boards('easy_boards.txt')
    pretty_print(boards[0])

##############################################################################

if __name__ == "__main__":
    main()