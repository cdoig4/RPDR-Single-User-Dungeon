"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


def read_board(board_name: str) -> str:
    """

    :param board_name:
    :return:
    """
    try:
        with open(f'./txt_files/{board_name}.txt') as file_object:
            file_object.read()
    except FileNotFoundError:
        print("File not found.")

    with open(f'./txt_files/{board_name}.txt') as file_object:
        return file_object.read()


def index_board(board_name: str) -> dict:
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
            location_type += ['enter']
        if character == 'E':
            location_type += ['exit']

    described_coordinates = dict(zip(coordinates, location_type))

    return described_coordinates


def set_board(character):
    """

    :param character:
    :return:
    """
    if character.get('met_rupaul'):
        character.update({'location': 'dressing_room'})
        character.update({'coordinates': (1, 5)})
    elif character.get('completed_lip_sync'):
        character.update({'location': 'judges_panel'})
        character.update({'coordinates': (1, 6)})
    elif character.get('level') == 2:
        character.update({'location': 'main_stage'})
        character.update({'coordinates': (0, 5)})
    else:
        character.update({'location': 'werk_room'})
        character.update({'coordinates': (0, 4)})
    return character


def place_character_in_board(board: str, current_coordinates: tuple) -> str:
    """

    :param board:
    :param current_coordinates:
    :return:
    """
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


def clear_board(board: str) -> str:
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


def display_board(character: dict) -> None:
    """

    :param character:
    :return:
    """
    board_name = character.get('location')
    display_name = board_name.title().replace('_', ' ')

    print(f'Location: {display_name}')
    current_coordinates = character.get('coordinates')

    marked_board = place_character_in_board(read_board(board_name), current_coordinates)

    return print(clear_board(marked_board))


def main():
    """
    Drive the program.
    """
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lipsync': False, 'level': 1, 'Name': 'Ginger Snaps',
                 'coordinates': (0, 4), 'location': 'werk_room'}
    # print(board)
    # print(index_board('main_stage'))
    # print(clear_board(board))
    display_board(character)


if __name__ == '__main__':
    main()
