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
    count = 0
    for character in board:
        if character == '!':
            count += 1

    return count




def main(board):
    """
    Drive the program.
    """
    board = read_board(board)
    print(board)
    print(index_board(board))

if __name__ == '__main__':
    main('stage')