"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


import boards
import controls
import challenges
import character_setup_and_intro


def game():
    """

    :return:
    """
    character = character_setup_and_intro.make_character(input("What is the name of your Drag Persona?\n"))
    character_setup_and_intro.deliver_introduction(character)
    achieved_goal = False

    while not achieved_goal:
        if character.get('location') is None:
            boards.set_board(character)
        boards.display_board(character)
        controls.move_character(character)
        challenges.run_challenges(character)
        # if character_has_leveled():
        #     execute_glow_up_protocol()
        #     achieved_goal = check_if_goal_attained(board, character)
        # else:
        #     print('You have to achieve your goal!')


"""to test lvl 2"""
# def game():
#
#     character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
#                  'completed_lipsync': False, 'level': 2, 'Name': 'Ginger Snaps',
#                  'coordinates': (0, 5), 'location': 'main_stage'}
#     achieved_goal = False
#
#     while not achieved_goal:
#         if character.get('location') is None:
#             boards.set_board(character)
#         boards.display_board(character)
#         controls.move_character(character)
#         challenges.run_challenges(character)
#         # if character_has_leveled():
#         #     execute_glow_up_protocol()
#         #     achieved_goal = check_if_goal_attained(board, character)
#         # else:
#         #     print('You have to achieve your goal!')

def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
