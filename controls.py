"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from boards import index_board


def show_score(character: dict) -> None:
    """

    :param character:
    :return:
    """
    charisma = character.get('Charisma')
    uniqueness = character.get('Uniqueness')
    nerve = character.get('Nerve')
    talent = character.get('Talent')

    return print(f'Stats: [Charisma: {charisma}, Uniqueness: {uniqueness}, '
                 f'Nerve: {nerve}, Talent: {talent}]')


def generate_challenge_input(answers: list) -> list:
    """
    """
    pairs = []

    for number, answer in enumerate(answers, 1):
        pair = (str(number), answer)
        pairs.append(pair)
    return pairs


def generate_directional_tools(current_coordinates, board_name):
    """

    :param current_coordinates:
    :param board_name:
    :return:
    """
    board_coordinates = index_board(board_name)

    board_limits = [key for key in board_coordinates]
    board_limits.sort(reverse=True)
    limit_coordinate = board_limits.pop(0)

    row = current_coordinates[0]
    column = current_coordinates[1]

    pairs = []

    if board_coordinates[current_coordinates] == 'enter':
        pairs.append(('E', 'Enter'))
    if board_coordinates[current_coordinates] == 'exit':
        pairs.append(('Q', 'Exit'))
    if row != 0 and board_coordinates[row - 1, column] is not False:
        pairs.append(('W', 'Up'))
    if row != limit_coordinate[0] and board_coordinates[row + 1, column] is not False:
        pairs.append(('S', 'Down'))
    if column != 0 and board_coordinates[row, column - 1] is not False:
        pairs.append(('A', 'Left'))
    if column != limit_coordinate[1] and board_coordinates[row, column + 1] is not False:
        pairs.append(('D', 'Right'))
    pairs.append(('0', 'Stats'))

    return pairs


def get_input_from_user(game_input: list, character: dict) -> str:
    """

    :param game_input:
    :return:
    """
    acceptable_answers = ['0']

    print('Controls------------------------------------------------------------------------')

    for pair in game_input:
        acceptable_answers += pair[0]
        print(f'{pair[0]}: {pair[1]}')

    answer = input()
    
    if answer == '0':
        show_score(character)
    if answer == 'Q':
        print('Where the hell do you think you\'re going girl? Get your ass back in here!')
        return get_input_from_user(game_input, character)
    if answer not in acceptable_answers:
        print('That is not an acceptable answer! Please try again:')
        return get_input_from_user(game_input, character)

    answer_index = acceptable_answers.index(answer)
    answer_string = game_input[answer_index][1]

    return answer_string.lower()


def move_character(character):
    """

    :param character:
    :return:
    """
    current_coordinates = character.get('coordinates')
    board_name = character.get('location')

    game_input = generate_directional_tools(current_coordinates, board_name)
    move_to_coordinates = get_input_from_user(game_input, character)

    if move_to_coordinates == 'enter':
        move_to_coordinates = current_coordinates
        print('Not until you level up, girl.')
    elif move_to_coordinates == 'up':
        move_to_coordinates = (current_coordinates[0] - 1, current_coordinates[1])
    elif move_to_coordinates == 'down':
        move_to_coordinates = (current_coordinates[0] + 1, current_coordinates[1])
    elif move_to_coordinates == 'left':
        move_to_coordinates = (current_coordinates[0], current_coordinates[1] - 1)
    elif move_to_coordinates == 'right':
        move_to_coordinates = (current_coordinates[0], current_coordinates[1] + 1)

    return character.update({'coordinates': move_to_coordinates})


def main():
    """
    Drive the program
    """
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lipsync': False, 'level': 1, 'Name': 'Ginger Snaps',
                 'coordinates': (3, 3), 'location': 'werk_room'}
    # print(read_board('dressing_room'))
    # print(generate_directional_tools((0, 5), index_board(board)))
    # print(get_input_from_user(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4'])))
    # print(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4']))
    move_character(character)
    move_character(character)


if __name__ == '__main__':
    main()
