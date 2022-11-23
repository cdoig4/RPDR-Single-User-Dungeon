"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


def make_board(rows, columns):
    """

    :param rows:
    :param columns:
    :return:
    """
    pass


def make_character(character_name):
    """

    :param character_name:
    :return:
    """
    pass

def get_user_choice():
    """

    :return:
    """
    pass


def validate_move(board, character, direction):
    """

    :param board:
    :param character:
    :param direction:
    :return:
    """
    pass


def move_character(character):
    """

    :param character:
    :return:
    """
    pass


def describe_current_location(board, character):
    """

    :param board:
    :param character:
    :return:
    """
    pass


def check_for_challenges():
    """

    :return:
    """
    pass


def game(): # called from main
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character("Player name")
    achieved_goal = False
    while not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
        describe_current_location(board, character)
        there_is_a_challenge = check_for_challenges()
        if there_is_a_challenge:
            execute_challenge_protocol(character)
        if character_has_leveled():
            execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, character)
        else:
            print("You have to achieve your goal!")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
