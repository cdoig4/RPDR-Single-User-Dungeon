import itertools
from boards import read_board
from boards import index_board
from boards import display_board

def generate_directional_tools(current_coordinates, board_coordinates):
    """

    :param current_coordinates:
    :param board_coordinates:
    :return:
    """
    board_limits = [key for key in board_coordinates]
    board_limits.sort(reverse=True)
    limit_coordinate = board_limits.pop(0)

    row = current_coordinates[0]
    column = current_coordinates[1]

    pairs = []

    if board_coordinates[current_coordinates] == 'entry':
        pairs.append(('E', 'Enter'))
    if board_coordinates[current_coordinates] == 'exit':
        pairs.append(('E', 'Exit'))
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

    for pair in game_input:
        acceptable_answers += pair[0]
        print(f'{pair[0]}: {pair[1]}')

    answer = input()
    if answer not in acceptable_answers:
        print('That is not an acceptable answer! Please try again:')
    if answer == 'Exit':
        print('Where the hell do you think you\'re going girl? Get your ass back in here!')
        return get_input_from_user(game_input)

    answer_index = acceptable_answers.index(answer)

    return game_input[answer_index][1]


def main():
    """
    Drive the program
    """
    board = read_board('stage')
    print(generate_directional_tools((0, 5), index_board(board)))
    # print(get_input_from_user(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4'])))
    # print(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4']))

if __name__ == '__main__':
    main()
