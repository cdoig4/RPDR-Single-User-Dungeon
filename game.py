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
    character = character_setup.make_character(input("What is the name of your Drag Persona?\n"))
    character_setup.deliver_introduction(character)
    achieved_goal = False

    while not achieved_goal:
        if character.get('location') is None:
            boards.set_board(character)
        boards.display_board(character)
        controls.move_character(character)
        challenges.run_challenges(character)
        if character['location'] == 'werk_room' and character['Talent'] >= 40:
            character_setup.check_for_level_up(character)
            print(f"RuPaul's voice echoes through the room. \"{character['Name']}, "
                  f"please make your way to the Main Stage. You have been chosen to take part in a Lip Sync "
                  f"for Your Legacy!\"\nYou hear the door at the South side of the room open.")
        if character['location'] == 'main_stage' and challenges.run_challenges(character):
            character_setup.check_for_level_up(character)
        if character['met_rupaul']:
            print(f"RuPaul's face breaks into a smile. \"ConDRAGulations {character['Name']}"
                  f"you're the winner baby!\"\nTriumphant music starts up as confetti begins to "
                  f"fall from the ceiling.\n\"You are now the Queen of the Mother Tucking "
                  f"UNIVERSE!\" Mother continues as she places a massive bejeweled crown upon your"
                  f" head and a matching scepter in your hand.\nYou sob with happiness as you"
                  f"know that this... is the beginning of the rest of your life.\nEND.")
            achieved_goal = True


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
