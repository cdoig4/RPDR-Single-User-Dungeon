"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


import boards
import controls
import challenges
import character_setup


def game():
    """

    :return:
    """
    # character = character_setup.make_character(input("What is the name of your Drag Persona?\n"))
    # character_setup.deliver_introduction(character)
    # achieved_goal = False
    #
    # while not achieved_goal:
    #     boards.display_board(character)
    #     controls.move_character(character)
    #     challenges.run_challenges(character)
    #     character_setup.check_for_level_up(character)
    # print('The END.')

"""to test end of lvl 1"""
def game():

    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 40, 'met_rupaul': False,
                 'completed_lip_sync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (0, 4), 'location': 'werk_room'}
    achieved_goal = False
SendTo
    while not achieved_goal:
        boards.display_board(character)
        controls.move_character(character)
        challenges.run_challenges(character)
        character_setup.check_for_level_up(character)
    print('The END.')



"""to test lvl 2"""
# def game():
#
#     character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 40, 'met_rupaul': False,
#                  'completed_lip_sync': False, 'level': 2, 'Name': 'Ginger Snaps',
#                  'coordinates': (0, 5), 'location': 'main_stage'}
#     achieved_goal = False
#
#     while not achieved_goal:
#         boards.display_board(character)
#         controls.move_character(character)
#         challenges.run_challenges(character)
#         character_setup.check_for_level_up(character)
#     print('The END.')


"""to test lvl 3 (judges panel)"""
# def game():
#
#     character = {'Charisma': 80, 'Uniqueness': 80, 'Nerve': 70, 'Talent': 70, 'met_rupaul': False,
#                  'completed_lip_sync': True, 'level': 2, 'Name': 'Ginger Snaps',
#                  'coordinates': (1, 5), 'location': 'judges_panel'}
#     achieved_goal = False
#
#     while not achieved_goal:
#         boards.display_board(character)
#         controls.move_character(character)
#         challenges.run_challenges(character)
#         character_setup.check_for_level_up(character)
#     print('The END.')


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
