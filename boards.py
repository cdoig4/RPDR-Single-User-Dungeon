import sys


def read_board(board):
    """

    :param board:
    :return:
    """
    try:
        with open(f'./boards/{board}.txt') as file_object:
            file_object.read()
    except FileNotFoundError:
        print("File not found.")

    with open(f'./boards/{board}.txt') as file_object:
        return file_object.read()

def index_board(board):
    """

    :param board:
    :return:
    """
    rows = [row for row in board if row == '$']
    columns = [column for column in board if column == '#']

    coordinates = []
    location_type = []

    for row in range(len(rows)):
        for column in range(len(columns)):
            coordinates += [(row, column)]

    for character in board:
        if character == '!':
            location_type += [True]
        if character == 'x':
            location_type += [False]
        if character == 'e':
            location_type += ['entry']
        if character == 'E':
            location_type += ['exit']

    described_coordinates = dict(zip(coordinates, location_type))

    return described_coordinates

def display_board(board):
    """

    :param board:
    :return:
    """
    cleared_board = board.replace('#', ' ')
    cleared_board = cleared_board.replace('$', ' ')
    cleared_board = cleared_board.replace('x', ' ')
    cleared_board = cleared_board.replace('!', ' ')
    return cleared_board

def main(board):
    """
    Drive the program.
    """
    board = read_board(board)
    print(board)
    print(index_board(board))
    print(display_board(board))

if __name__ == '__main__':
    main('stage')