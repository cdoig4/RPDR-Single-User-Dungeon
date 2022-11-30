"""
Create the player character and give them the introduction
"""
LOOK_QUEEN = {"Charisma": 14, "Uniqueness": 15, "Nerve": 10, "Talent": 10, 'met_rupaul': False,
              "completed_lip_sync": False, "level": 1}
COMEDY_QUEEN = {"Charisma": 15, "Uniqueness": 14, "Nerve": 10, "Talent": 10, 'met_rupaul': False,
                "completed_lip_sync": False, "level": 1}
PERFORMANCE_QUEEN = {"Charisma": 17, "Uniqueness": 12, "Nerve": 10, "Talent": 10, 'met_rupaul': False,
                     "completed_lip_sync": False, "level": 1}
ALTERNATIVE_QUEEN = {'Charisma': 12, 'Uniqueness': 17, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                     "completed_lip_sync": False, "level": 1}
CHARACTER_CLASSES = ['Look Queen', 'Comedy Queen', 'Performance Queen', 'Alternative Queen']


def make_character(character_name: str) -> dict:
    """
    Create character of desired name and class.

    :param character_name: must be a string containing only alphabetic characters or spaces
    :precondition: character_name must be a string
    :postcondition: asks the user for input to determine class stats
    :postcondition: creates character dictionary containing name and stats of desired class
    :return: a dictionary representing the user's character
    """
    print("What type of queen are you?")
    for pair in list(enumerate(CHARACTER_CLASSES)):
        print(f'{pair[0]}: {pair[1]}')

    answer = int(input())
    if answer == 0:
        character = {key: value for key, value in LOOK_QUEEN.items()}
    elif answer == 1:
        character = {key: value for key, value in COMEDY_QUEEN.items()}
    elif answer == 2:
        character = {key: value for key, value in PERFORMANCE_QUEEN.items()}
    else:
        character = {key: value for key, value in ALTERNATIVE_QUEEN.items()}

    character['Name'] = character_name
    character.update({'coordinates': None})
    return character


def deliver_introduction(character_dictionary: dict) -> None:
    """
    Deliver introduction to user.

    :param character_dictionary: must be a dictionary representing the user's character with the key 'Name' present
    :precondition: character_dictionary must be a dictionary
    :postcondition: prints the game introduction
    """
    print(f"ConDRAGulations {character_dictionary['Name']}, you have been selected to compete on the new season "
          f"of Rupaul's Drag Race!\nThis season will operate a little differently...\nTo obtain the title of "
          f"'Greatest Queen of All Time', you must first win the right to lipsync on the Main Stage by proving "
          f"your mettle against some fellow queens in the Werk Room.\nIf you win the Lip Sync for your Legacy, you "
          f"will be invited to RuPaul's dressing room where you will LIP SYNC FOR YOUR LIFE against Mother herself.\n"
          f"Good luck, and DON'T fuck it up.")
    print('As you get settled in the Werk Room you hear "Ooh girl!" and you see RuPaul appear on a TV screen on'
          ' the side of the room. She says')
    print(f'To be invited to compete in a Lip Sync for your Legacy you must first prove that you are'
          f' literate. Read enough of your fellow queens for filth and you will be called to the'
          f' main stage.')


def main():
    """Drive the program."""
    new_character = make_character(input('What is the name of your Drag Persona?\n'))
    deliver_introduction(new_character)
    print(new_character)


if __name__ == '__main__':
    main()
