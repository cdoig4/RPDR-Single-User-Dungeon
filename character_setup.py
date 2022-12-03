"""
Create the player character and give them the introduction
"""

import json
import random
import challenges
from game import game


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
    if stat[1] + value < 0:
        return {stat[0]: 0}
    return {stat[0]: stat[1] + value}


def power_up_or_down(character, values, is_queen):
    """
    """
    stat_names = ['Charisma', 'Uniqueness', 'Nerve', 'Talent']
    stats = [(stat, value) for stat, value in character.items() if stat in stat_names]
    new_pairs = list(map(apply_power_up, stats, values))

    for pair in new_pairs:
        character.update(pair)

    filtered_pairs = list(filter(filter_no_delta, list(zip(new_pairs, values))))
    for pair in filtered_pairs:
        key = list(pair[0].keys())

        if pair[1] < 0:
            up_or_down = 'decreased'
        else:
            up_or_down = 'increased'

        if is_queen:
            name = character['Name']
            print(f'{name} {key[0]} has {up_or_down} by {abs(pair[1])} to {pair[0].get(key[0])}!')
        else:
            print(f'Your {key[0]} has {up_or_down} by {abs(pair[1])} to {pair[0].get(key[0])}!')

    return character


def you_win(character, enemy_name, challenge_name):
    """
    """
    if challenge_name == 'fight':
        print(f"{enemy_name} slinks away, clearly feeling the shade of it all.\n"
              f"You regain composure after all the reads. You return to full Nerve.")
        increase = random.randint(8, 12)
        print('You win!')
        return power_up_or_down(character, [0, 0, 0, increase], True)
    if challenge_name == 'makeover_challenge':
        print(f"She says: ConDRAGulations {character['Name']} and {enemy_name}, you are the"
              f" winners of this mini challenge!\"\n")
        increase = random.randint(10, 15)
        print('You win!')
        return power_up_or_down(character, [0, increase, 0, increase], True)
    if challenge_name == 'werk_room':
        print(f"RuPaul's voice echoes through the room. \"{character['Name']}, "
              f"please make your way to the Main Stage. You have been chosen to take part in a Lip Sync "
              f"for Your Legacy!\"\nYou quickly make your way to the stage, the potential lip sync songs spinning"
              f" through your head")
        print("You are now level 2!")
        return power_up_or_down(character, [random.randint(30, 40), random.randint(30, 40),
                                            random.randint(30, 40), 0], False)
    if challenge_name == 'lipsync':
        print(f"RuPaul's voice echoes: 'ConDRAGulations {character['Name']}, you're a winner baby!'\n"
              f"You feel your inner saboteur melting away.")
        print("You are now level 3!")
        return power_up_or_down(character, [random.randint(30, 40), random.randint(30, 40),
                                            random.randint(30, 40), 0], False)
    if challenge_name == 'rupaul':
        print(f"RuPaul's face breaks into a smile. \"ConDRAGulations {character['Name']}"
              f"you're the winner baby!\"\nTriumphant music starts up as confetti begins to "
              f"fall from the ceiling.\n\"You are now the Queen of the Mother Tucking "
              f"UNIVERSE!\" Mother continues as she places a massive bejeweled crown upon your"
              f" head and a matching scepter in your hand.\nYou sob with happiness as you"
              f"know that this... is the beginning of the rest of your life.\n")
        game.achieved_goal = True


def check_for_level_up(character):
    """

    :param character:
    :return:
    """
    if character['location'] == 'werk_room' and character['Talent'] >= 40:
        character['level'] += 1
        you_win(character, None, 'werk_room')
    return character


def check_if_dead(character):
    """

    :param character:
    :return:
    """
    if character['Nerve'] <= 0:
        print(f"\nYou hear RuPaul's voice:\n\n\"{character['Name']},\nThank you for bringing your "
              f"Charisma, Uniqueness, Nerve, and Talent to the\ncompetition. "
              f"But this is not your time.\nNow.... Sashay Away.\"\n"
              f"--------------------------------------------------------------------------------")
        character.clear()
        game()
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
