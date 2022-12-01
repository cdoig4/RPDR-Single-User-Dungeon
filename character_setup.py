"""
Create the player character and give them the introduction
"""

import json
import random
import challenges


LOOK_QUEEN = {"Charisma": 14, "Uniqueness": 15, "Nerve": 10, "Talent": 10, 'met_rupaul': False,
              "completed_lip_sync": False, "level": 1}
COMEDY_QUEEN = {"Charisma": 15, "Uniqueness": 14, "Nerve": 10, "Talent": 10, 'met_rupaul': False,
                "completed_lip_sync": False, "level": 1}
PERFORMANCE_QUEEN = {"Charisma": 17, "Uniqueness": 12, "Nerve": 10, "Talent": 10, 'met_rupaul': False,
                     "completed_lip_sync": False, "level": 1}
ALTERNATIVE_QUEEN = {'Charisma': 12, 'Uniqueness': 17, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                     "completed_lip_sync": False, "level": 1}
CHARACTER_CLASSES = ['Look Queen', 'Comedy Queen', 'Performance Queen', 'Alternative Queen']


def deliver_introduction(character_dictionary: dict) -> None:
    """
    Deliver introduction to user.

    :param character_dictionary: must be a dictionary representing the user's character with the key 'Name' present
    :precondition: character must be a dictionary
    :postcondition: prints the game introduction
    """
    filename = './json_files/introduction.json'
    with open(filename) as file_object:
        introduction = json.load(file_object)

    print(f"{introduction[0]}ConDRAGulations {character_dictionary['Name']},{introduction[1]}")


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
    answer = challenges.get_challenge_input_from_user(CHARACTER_CLASSES)

    if answer == 'look_queen':
        character = {key: value for key, value in LOOK_QUEEN.items()}
    elif answer == 'comedy_queen':
        character = {key: value for key, value in COMEDY_QUEEN.items()}
    elif answer == 'performance_queen':
        character = {key: value for key, value in PERFORMANCE_QUEEN.items()}
    else:
        character = {key: value for key, value in ALTERNATIVE_QUEEN.items()}

    character['Name'] = character_name
    character.update({'coordinates': None})
    return character


def level_up(character):
    """

    :param character:
    :return:
    """
    character['level'] += 1
    character['Charisma'] += random.randint(20, 30)
    character['Uniqueness'] += random.randint(20, 30)
    character['Nerve'] += random.randint(20, 30)
    print(f"RuPaul's voice echoes: 'ConDRAGulations {character['Name']}, you're a winner baby!'\n"
          f"You feel your inner saboteur melting away.\nYou are now level {character['level']}\n"
          f"Your Charisma increases to {character['Charisma']}!\nYour Uniqueness increases to"
          f" {character['Uniqueness']}!\nYour Nerve increases to {character['Nerve']}"
          f"\nYou are ushered towards the Judge's Panel.")
    return character


def main():
    """Drive the program."""
    new_character = make_character(input('What is the name of your Drag Persona?\n'))
    deliver_introduction(new_character)
    print(new_character)


if __name__ == '__main__':
    main()
