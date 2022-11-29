import sys

def get_starting_coordinates(character):
    """

    :param character:
    :return:
    """
    board_name = character.get('location')

    if board_name == 'werkroom':
        starting_coordinates = (0, 4)
    elif board_name == 'stage':
        get_starting_coordinates(0, 5)
    elif board_name == 'judges_panel':
        get_starting_coordinates(1, 6)
    elif board_name == 'dressing_room':
        get_starting_coordinates(1, 5)

    return starting_coordinates

def read_board(board_name):
    """

    :param board_name:
    :return:
    """
    try:
        with open(f'./boards/{board_name}.txt') as file_object:
            file_object.read()
    except FileNotFoundError:
        print("File not found.")

    with open(f'./boards/{board_name}.txt') as file_object:
        return file_object.read()

def index_board(board_name):
    """

    :param board_name:
    :return:
    """
    board = read_board(board_name)

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

def place_character_in_board(board, current_coordinates):
    """

    :param board:
    :param current_coordinates:
    :return:
    """
    rows = [row for row in board if row == '$']
    columns = [column for column in board if column == '#']

    row = current_coordinates[0]
    column = current_coordinates[1]

    marked_board = board.replace('!', 'x')
    marked_board = marked_board.replace('E', 'x')
    marked_board = marked_board.replace('e', 'x')

    location = row * len(columns) + column

    for _ in range(location):
        next_marker = marked_board.find('x')
        marked_board = marked_board[0: next_marker] + ' ' + marked_board[next_marker + 1:]

    location_marker = marked_board.find('x')
    marked_board = marked_board[0: location_marker] + '&' + marked_board[location_marker + 1:]
    marked_board = marked_board.replace('x', ' ')

    return marked_board

def clear_board(board):
    """

    :param board:
    :return:
    """

    cleared_board = board.replace('#', ' ')
    cleared_board = cleared_board.replace('$', ' ')
    cleared_board = cleared_board.replace('x', ' ')
    cleared_board = cleared_board.replace('!', ' ')
    cleared_board = cleared_board.replace('E', ' ')
    cleared_board = cleared_board.replace('e', ' ')
    return cleared_board

def display_board(board, current_coordinates):
    """

    :param board:
    :param current_coordinates:
    :return:
    """
    opened_board = read_board(board)
    marked_board = place_character_in_board(opened_board, current_coordinates)

    return clear_board(marked_board)


def main():
    """
    Drive the program.
    """
    # print(board)
    print(index_board('stage'))
    # print(clear_board(board))
    # print(display_board('stage', (4, 6)))

if __name__ == '__main__':
    main()