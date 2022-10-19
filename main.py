#!/usr/bin/env python3


def read_boards(filename):
    boards = []
    with open(filename, 'r') as f:
        boards = f.readlines()
        boards = [x.split(',')[0] for x in boards]
        return [n.replace('.', '0') for n in boards]


def pretty_print(board):
    # rows
    for i in range(0, 9):
        if i in [3,6]:
            print('------+-------+------')
        
        # cols
        for j in range(0, 9):
            current = board[i*9 + j] + ' '

            if j in [2,5]:
                print(current, end='| ')
            elif j == 8:
                print(current)
            else:
                print(current, end='')



def main():
    boards = read_boards('easy_boards.txt')
    pretty_print(boards[0])

##############################################################################

if __name__ == "__main__":
    main()