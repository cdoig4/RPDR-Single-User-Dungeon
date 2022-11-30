import itertools
from boards import read_board
from boards import index_board
from boards import clear_board

def generate_directional_tools(current_coordinates, board_name):
    """

    :param current_coordinates:
    :param board_coordinates:
    :return:
    """
    board_coordinates = index_board(board_name)

    board_limits = [key for key in board_coordinates]
    board_limits.sort(reverse=True)
    limit_coordinate = board_limits.pop(0)

    row = current_coordinates[0]
    column = current_coordinates[1]

    pairs = []

    if board_coordinates[current_coordinates] == 'entry':
        pairs.append(('E', 'Enter'))
    if board_coordinates[current_coordinates] == 'exit':
        pairs.append(('Q', 'Exit'))
    if row != 0 and board_coordinates[row - 1, column] != False:
        pairs.append(('W', 'Up'))
    if row != limit_coordinate[0] and board_coordinates[row + 1, column] != False:
        pairs.append(('S', 'Down'))
    if column != 0 and board_coordinates[row, column - 1] != False:
        pairs.append(('A', 'Left'))
    if column != limit_coordinate[1] and board_coordinates[row, column + 1] != False:
        pairs.append(('D', 'Right'))

    return pairs

def generate_challenge_input(answers: list) -> list:
    """
    """
    pairs = []

    for number, answer in enumerate(answers, 1):
        pair = (str(number), answer)
        pairs.append(pair)
    return pairs

def get_input_from_user(game_input: list) -> str:
    """

    :param game_input:
    :return:
    """
    acceptable_answers = []

    print('Controls------------------------------------------------------------------------')

    for pair in game_input:
        acceptable_answers += pair[0]
        print(f'{pair[0]}: {pair[1]}')

    answer = input()
    if answer == 'Q':
        print('Where the hell do you think you\'re going girl? Get your ass back in here!')
        return get_input_from_user(game_input)
    if answer not in acceptable_answers:
        print('That is not an acceptable answer! Please try again:')
        return get_input_from_user(game_input)

    answer_index = acceptable_answers.index(answer)
    answer_string = game_input[answer_index][1]

    return answer_string.lower()

def move_character(character):
    """

    :param current_coordinates:
    :param board_coordinates:
    :param board_name:
    :return:
    """
    current_coordinates = character.get('coordinates')
    board_name = character.get('location')

    inputs = generate_directional_tools(current_coordinates, board_name)
    move_to_coordinates = get_input_from_user(inputs)

    if move_to_coordinates == 'exit':
        move_to_coordinates = board_name
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
                 'coordinates': (0, 4), 'location': 'werkroom'}
    # print(read_board('dressing_room'))
    # print(generate_directional_tools((0, 5), index_board(board)))
    # print(get_input_from_user(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4'])))
    # print(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4']))
    move_character(character)
    move_character(character)

if __name__ == '__main__':
    main()
