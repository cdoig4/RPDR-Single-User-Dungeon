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


def filter_no_delta(structure):
    """

    :param structure:
    :return:
    """
    if structure[1] != 0:
        return structure[0]


def apply_power_up(stat, value):
    """
    """
    return {stat[0]: stat[1] + value}


def power_up(character, values):
    """
    """
    stat_names = ['Charisma', 'Uniqueness', 'Nerve', 'Talent']
    stats = [(stat, value) for stat, value in character.items() if stat in stat_names]
    new_pairs = list(map(apply_power_up, stats, values))

    for pair in new_pairs:
        character.update(pair)

    filtered_pairs = list(filter(filter_no_delta, list(zip(new_pairs, values))))
    print(filtered_pairs)
    for pair in filtered_pairs:
        key = list(pair[0].keys())
        print(f'Your {key[0]} has decreased by {pair[1]} to {pair[0].get(key[0])}!')

    return character


def you_win(character, enemy, challenge_name):
    """
    """
    if challenge_name == 'fight':
        print(f"{enemy['Name']} slinks away, clearly feeling the shade of it all.\n")
        increase = random.randint(8, 12)
        return power_up(character, [0, 0, 0, increase])


def check_for_level_up(character):
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


def check_if_dead(character):
    """

    :param character:
    :return:
    """
    if character['Nerve'] <= 0:
        print(f"\nYou hear RuPaul's voice:\n\"{character['Name']}, thank you for bringing your Charisma, Uniqueness, "
              f"Nerve, and Talent to the competition. But this is not your time.\n"
              f"Now.... Sashay Away.\n"
              f"--------------------------------------------------------------------------------")
        character = make_character(input("What is the name of your Drag Persona?\n"))
        deliver_introduction(character)
    return character

def main():
    """Drive the program."""
    # new_character = make_character(input('What is the name of your Drag Persona?\n'))
    # deliver_introduction(new_character)
    # print(new_character)
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lipsync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (6, 8), 'location': 'main_stage'}
    you_win(character, {'Name': 'test'}, 'fight')
    print(character)
    # print(power_up(character, [0, 0, 0, 8]))


if __name__ == '__main__':
    main()
