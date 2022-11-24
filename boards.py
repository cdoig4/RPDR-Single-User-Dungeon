import sys


def read_board(board):
    """

    :param board:
    :return:
    """
    try:
        with open(f'./maps/{board}.txt') as file_object:
            file_object.read()
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    with open(f'./maps/{board}.txt') as file_object:
        return file_object.read()

def index_board(board):
    """

    :param board:
    :return:
    """
    rows = [row for row in board if row == '$']
    columns = [column for column in board if column == '#']

    coordinates = {}

    for row in range(len(rows)):
        for column in range(len(columns)):
            coordinates[(row, column)] = [None]

    return coordinates




def main(board):
    """
    Drive the program.
    """
    board = read_board(board)
    print(board)
    print(index_board(board))

if __name__ == '__main__':
    main('stage')