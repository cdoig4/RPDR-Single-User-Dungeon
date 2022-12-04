"""
Colin Doig A01334230
Kelly Hagg A01324804

Create the player character and give them the introduction
"""


import json
import random
import boards
import challenges
from game import game


def deliver_introduction(character_dictionary: dict) -> None:
    """
    Deliver introduction to player.

    :param character_dictionary: must be a dictionary representing the player's character with the
    key 'Name' present
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
    :return: a dictionary representing the player's character
    """
    character = {'met_rupaul': False, "completed_lip_sync": False, "level": 1,
                 'achieved_goal': False, 'location': 'werk_room', 'coordinates': (0, 4)}
    queen_types = ['Look Queen', 'Comedy Queen', 'Performance Queen', 'Alternative Queen']
    stat_names = ["Charisma", "Uniqueness", "Nerve", "Talent"]

    base_value = 10
    queen_add_ons = ((4, 5, 0, 0), (5, 4, 0, 0), (7, 2, 0, 0), (2, 7, 0, 0))

    print("What type of queen are you?")
    answer = challenges.get_challenge_input_from_user(queen_types)
    if answer == 'look_queen':
        stat_values = [value + base_value for value in queen_add_ons[0]]
    elif answer == 'comedy_queen':
        stat_values = [value + base_value for value in queen_add_ons[1]]
    elif answer == 'performance_queen':
        stat_values = [value + base_value for value in queen_add_ons[2]]
    else:
        stat_values = [value + base_value for value in queen_add_ons[3]]

    named_stats = list(zip(stat_names, stat_values))
    stats = {stat: value for stat, value in named_stats}

    character['Name'] = character_name
    character.update(stats)
    return character


def filter_no_delta(structure):
    """


    :param structure:
    :return:
    """
    if structure[1] != 0:
        return structure[0]


def apply_power_up(stat: tuple, value: int) -> dict:
    """
    Calculate new value to be assigned to a stat.

    :param stat: must be a tuple containing a string representing the name of a stat and an integer
    representing the value assigned to that stat
    :param value: must be an integer
    :precondition: stat must be a tuple and value must be an integer
    :postcondition: calculate the new value of the second element in the stat tuple after the
    addition of value
    :return: a dictionary with a key which is equal to the first element of the stat tuple with a
    value of 0 if adding the value parameter to it would have made it negative, else a dictionary
    with a key which is equal to the first element of the stat tuple with a value that is equal to
    the second element of the stat tuple with the value parameter added to it
    >>> apply_power_up(('Charisma', 15), 34)
    {'Charisma': 49}
    >>> apply_power_up(('Nerve', 4), -4)
    {'Nerve': 0}
    >>> apply_power_up(('Uniqueness', 12), -20)
    {'Uniqueness': 0}
    """
    try:
        stat[1] + value
        if stat[1] + value < 0:
            return {stat[0]: 0}
        return {stat[0]: stat[1] + value}
    except IndexError:
        print("Stat must have two elements!")


def power_up_or_down(character: dict, values: list, is_queen: bool) -> dict:
    """
    Inform player of changes to stats for either themselves or the enemy.

    :param character: must be a dictionary representing a game character, either player or
    non-player
    :param values: a list containing four integers
    :param is_queen: a Boolean representing whether the dictionary represents the player character
    or not
    :postcondition: adjusts values stored inside character dictionary either up or down depending
    on whether the integers in values are positive or negative
    :return: dictionary representing a game character
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
            print(f'{name}\'s {key[0]} has {up_or_down} by {abs(pair[1])} to '
                  f'{pair[0].get(key[0])}!')
        else:
            print(f'Your {key[0]} has {up_or_down} by {abs(pair[1])} to {pair[0].get(key[0])}!')

    return character


def you_win(character: dict, enemy_name: str or None, challenge_name: str) -> dict or None:
    """
    Perform win events for player.

    :param character: must be a dictionary representing the player character with the keys 'Name'
    and 'completed_lip_sync' present, with the value assigned to 'Name' being a string and the
    value assigned to 'completed_lip_sync' being a Boolean
    :param enemy_name: must be a non-empty string representing an NPC name or None if there is no NPC
    :param challenge_name: must be a non-empty string
    :precondition: character must be a dictionary, enemy_name must be either a string or None, and challenge_name must
    be a string
    :postcondition: prints specified win statements depending on the string passed as challenge_name
    :postcondition: changes achieved_goal value to True if challenge_name is equal to 'rupaul'
    :return: function to alter stats stored within character dictionary if challenge_name is equal
    to 'read_battle' or
    'makeover_challenge', function to change the board the player is on if challenge_name is equal
    to 'werk_room',
    else print statement introducing the judges panel location if challenge_name is equal to
    'lip_sync'
    """
    if challenge_name == 'read_battle':
        print('You win!')
        print(f"{enemy_name} slinks away, clearly feeling the shade of it all.")
        print('You regain composure after all the reads.')
        increase = random.randint(8, 12)
        return power_up_or_down(character, [0, 0, 2, increase], False)
    if challenge_name == 'makeover_challenge':
        print(f"\n\"ConDRAGulations {character['Name']} and {enemy_name},\nyou are the"
              f" winners of this mini challenge!\"\n")
        increase = random.randint(10, 15)
        return power_up_or_down(character, [0, increase, 0, increase], False)
    if challenge_name == 'werk_room':
        print("\nYou are now level 2!")
        power_up_or_down(character, [random.randint(30, 40), random.randint(30, 40),
                                     random.randint(30, 40), 15], False)
        print(f"\nRuPaul's voice echoes through the room: \n\n\"{character['Name']}, "
              f"please make your way to the Main Stage. "
              f"\nYou have been chosen to take part in a Lip Sync for Your Legacy!\"\n"
              f"\nYou quickly make your way to the stage, \nthe potential lip sync songs spinning"
              f" through your head.")
        return boards.set_board(character)
    if challenge_name == 'lip_sync':
        print(f"RuPaul's voice echoes: 'ConDRAGulations {character['Name']}, "
              f"you're a winner baby!'\nYou feel your inner saboteur melting away.")
        print("\nYou are now level 3!")
        character['completed_lip_sync'] = True
        power_up_or_down(character, [random.randint(30, 40), random.randint(30, 40),
                                     random.randint(30, 40), 20], False)
        boards.set_board(character)
        return print(f"\nYou are ushered towards the Judge's Panel.")
    if challenge_name == 'rupaul':
        print(f"\nRuPaul's face breaks into a smile. \"ConDRAGulations {character['Name']}, "
              f"you're the winner baby!\"\nTriumphant music starts up as confetti begins to "
              f"fall from the ceiling.\n\nRuPaul says,\"You are now the Queen of the Mother Tucking"
              f" UNIVERSE!\"\n\nMother continues as she places a massive bejeweled crown upon your"
              f" head and a\nmatching scepter in your hand.\nYou sob with happiness.\nYou"
              f"know that this... is the beginning of the rest of your life.\n")
        character['achieved_goal'] = True


def check_for_level_up(character: dict) -> dict:
    """
    Determine whether the player character has leveled up.

    :param character: must be a dictionary representing the player character with the keys
    'location', 'Talent', and 'level' present, with the value assigned to 'location' being a string
    and the values assigned to 'Talent' and 'level' being positive integers
    :precondition: character must be a dictionary
    :postcondition: determines whether the player character has leveled up based on the values
    currently assigned to the 'location' and 'Talent' keys
    :postcondition: passes character dictionary to function which levels up the character if the
    conditions are met
    :return: dictionary representing the player character
    """
    if character['location'] == 'werk_room' and character['Talent'] >= 40:
        character['level'] += 1
        you_win(character, None, 'werk_room')
    return character


def check_if_dead(character: dict) -> dict:
    """
    Determine whether player character has lost all of their health ('Nerve')

    :param character: must be a dictionary with the keys 'Nerve' and 'Name' present, with the value
    assigned to 'Nerve' being an integer and the value assigned to 'Name' being a string
    :precondition: character must be a dictionary
    :postcondition: determines whether the value assigned to 'Nerve' is 0 or less
    :postcondition: prints loss statement, clears character dictionary, and restarts game if 'Nerve'
    is 0 or less
    :return: dictionary that is either empty or that represents the current player character
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
    new_character = make_character(input('What is the name of your Drag Persona?\n'))
    # deliver_introduction(new_character)
    # print(new_character)
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lip_sync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (6, 8), 'location': 'main_stage'}
    # you_win(character, {'Name': 'test'}, 'read_battle')
    print(new_character)
    # print(power_up(character, [0, 0, 0, 8]))


if __name__ == '__main__':
    main()
