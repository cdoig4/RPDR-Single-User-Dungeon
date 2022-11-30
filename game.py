"""
Colin Doig A01334230
Kelly Hagg A01324804
"""
import character_setup_and_intro

import boards
import controls

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
        character.update({'location': 'stage'})
        character.update({'coordinates': (0, 5)})
    else:
        character.update({'location': 'werkroom'})
        character.update({'coordinates': (0, 4)})
    return character


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


def game():
    character = character_setup_and_intro.make_character(input("What is the name of your Drag Persona?\n"))
    character_setup_and_intro.deliver_introduction(character)
    achieved_goal = False

    while not achieved_goal:
        if character.get('location') == None:
            set_board(character)
        boards.display_board(character)
        controls.move_character(character)
        # describe_current_location(board, character)
        # direction = get_user_choice()
        # valid_move = validate_move(board, character, direction)
        # if valid_move:
        #     move_character(character)
        # describe_current_location(board, character)
        # there_is_a_challenge = check_for_challenges()
        # if there_is_a_challenge:
        #     execute_challenge_protocol(character)
        # if character_has_leveled():
        #     execute_glow_up_protocol()
        #     achieved_goal = check_if_goal_attained(board, character)
        # else:
        #     print('You have to achieve your goal!')


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
