"""
Colin Doig A01334230
Kelly Hagg A01324804

Main game file.
"""


import boards
import controls
import challenges
import character_setup


def game():
    """
    Run RuPaul's (Text-Based) Drag Race!
    """
    character = character_setup.make_character(input("What is the name of your Drag Persona?\n"))
    character_setup.deliver_introduction(character)

    while not character['achieved_goal']:
        boards.display_board(character)
        controls.move_character(character)
        challenges.run_challenges(character)
    return print('The END.')


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
