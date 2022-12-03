"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


import json


def read_board(board_name: str) -> str:
    """
    Read JSON file representing game board.

    :param board_name: must be a string representing the name of the desired game board
    :precondition: board_name must be a string
    :postcondition: opens and reads JSON file of the desired board title
    :return: string representing the correct board that has been read from the JSON file
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
        if character == 'X':
            location_type += [True]
        if character == 'x':
            location_type += [False]
        if character == 'e':
            location_type += ['enter']
        if character == 'E':
            location_type += ['exit']
        if character == 'Q':
            location_type += ['queen']
        if character == 'R':
            location_type += ['queen']

    described_coordinates = dict(zip(coordinates, location_type))

    return described_coordinates


def set_board(character):
    """
    Set correct values into player character dictionary to represent where they are in the game.

    :param character: must be a dictionary representing the player character with the keys
    'met_rupaul', 'location', 'coordinates', and 'level' present, the value of 'met_rupaul' must be
    a Boolean, the value of 'location' must be a string, the value of 'coordinates' must be a tuple
    containing two positive integers, and the value of 'level' must be a positive integer
    :precondition: character must be a dictionary
    :postcondition: if player has met_rupaul their location is updated with values representing the
    dressing room :postcondition: if player has completed_lip_sync their location is updated with
    values representing the judges panel
    :postcondition: if the player character's level is 2 their location is updated with values
    representing the main stage
    :return: dictionary with 'location' and 'coordinates' values updated to reflect correct player
    position
    """
    if character['met_rupaul']:
        character.update({'location': 'dressing_room', 'coordinates': (1, 5)})
    elif character['completed_lip_sync']:
        character.update({'location': 'judges_panel', 'coordinates': (1, 6)})
    elif character['level'] == 2:
        character.update({'location': 'main_stage', 'coordinates': (0, 5)})
    return character


def place_character_in_board(board: str, current_coordinates: tuple) -> str:
    """
    Create representation of player character in correct location on the game board.

    :param board: must be a string representing the board of the current location of the user
    :param current_coordinates: must be a tuple representing the current location of the user on
    the board using two positive integers
    :precondition: board must be a string and current_coordinates must be a tuple
    :postcondition: calculates the current location of the user on the game board
    :postcondition: places player symbol ('&') in the correct location on the game board
    :return: string representing the correctly marked board with the correct current location of
    the user shown
    """
    columns = [column for column in board if column == '#']

    row = current_coordinates[0]
    column = current_coordinates[1]

    location = row * len(columns) + column

    marked_board = board.replace('!', 'x')
    marked_board = marked_board.replace('E', 'x')
    marked_board = marked_board.replace('e', 'x')
    marked_board = marked_board.replace('R', 'x')
    marked_board = marked_board.replace('Q', 'x')
    marked_board = marked_board.replace('X', 'x')

    for _ in range(location):
        next_marker = marked_board.find('x')
        marked_board = marked_board[0: next_marker] + ' ' + marked_board[next_marker + 1:]

    location_marker = marked_board.find('x')
    marked_board = marked_board[0: location_marker] + '&' + marked_board[location_marker + 1:]
    marked_board = marked_board.replace('x', ' ')

    return marked_board


def clear_board(board: str) -> str:
    """
    Clear game board.

    :param board: must be a string representing board of the current location of the player
    character
    :precondition: board must be a string
    :return: board string that has been cleared of all symbols
    """

    cleared_board = board.replace('#', ' ')
    cleared_board = cleared_board.replace('$', ' ')
    cleared_board = cleared_board.replace('x', ' ')
    cleared_board = cleared_board.replace('!', ' ')
    cleared_board = cleared_board.replace('E', ' ')
    cleared_board = cleared_board.replace('e', ' ')
    return cleared_board


def format_board(board: str, character: dict) -> str:
    """
    Format game board for player.

    :param board: must be a string representing the name of the current board
    :param character: must be a dictionary representing the player character with the key 'location'
    present
    whose value must be a string
    :precondition: board must be a string and character must be a dictionary
    :postcondition: formats correct board based on the current location of the player character
    :return: string representing the board of the current location of the user
    """
    location = character['location']

    if location == 'werk_room':
        return board[:231] + 'Q' + board[232:299] + 'Q' + board[300:407] + 'Q' + \
               board[408:475] + 'Q' + board[476:]
    elif location == 'dressing_room':
        return board[:118] + 'R' + board[119:]
    elif location == 'main_stage':
        return board[:544] + 'Q' + board[545:568] + 'X' + board[569:]
    return board


def display_board(character: dict) -> None:
    """
    Display game board of current location for the player.

    :param character: must be a dictionary representing the player character with the keys
    'location' and 'coordinates' present and the value of 'location' must be a string while the
    value of 'coordinates' must be a tuple containing two positive integers that represent the
    coordinates of the player
    :precondition: character must be a dictionary
    :postcondition: passes correct board into the format_board function
    :postcondition: creates string representing correctly formatted board
    :return: print statement containing the correctly formatted board string to be displayed to the
    player
    """
    board_name = character.get('location')
    current_coordinates = character.get('coordinates')
    board_indices = index_board(board_name)

    filename = './json_files/location_descriptions.json'
    with open(filename) as file_object:
        location_descriptions = json.load(file_object)

    descriptions = location_descriptions.get(board_name)

    print(f'---------------------------------------------------'
          f'-----------------------------\n{descriptions[0]}')

    if board_indices.get(current_coordinates) == 'exit':
        print(descriptions[1])

    marked_board = place_character_in_board(read_board(board_name), current_coordinates)
    formatted_board = format_board(marked_board, character)

    return print(clear_board(formatted_board))


def main():
    """
    Drive the program.
    """
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lip_sync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (0, 4), 'location': 'werk_room'}
    # board = read_board('dressing_room')

    # print(board[:118] + 'R' + board[119:])
    # print(clear_board(board))
    display_board(character)


if __name__ == '__main__':
    main()
