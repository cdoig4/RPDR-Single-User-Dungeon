"""
Challenges for the user to help them increase their level!
"""
import json
import math
import random
import queens
import character_setup


POTENTIAL_READS = ('Legendary you think you are. Legendary? Looks like leg AND dairy.', 'Beauty fades, dumb is forever',
                   'The last time you got fucked was by genetics')


def judge_events(character_dictionary):  #could print to user that their stats have changed & call the show score function in controls
    """
    Provide possible random events for each character movement.

    :param character_dictionary: a dictionary representing the player character
    :precondition: movement must be a Boolean and character_dictionary must be a dictionary with the keys 'Charisma',
    'Uniqueness', and 'Nerve' present and each must have a positive integer for their value
    :postcondition: determine whether a random judge event happens or not
    :return: character_dictionary that has either not been altered or has had a single value altered based which event
    occured
    """
    event_check = random.randint(1, 20)
    if event_check == 1:
        print(f'Michelle glares at you and says:\n"That dress is hideous. Where did you get it, Party City?"')
        character_dictionary['Charisma'] -= 5
    elif event_check == 7:
        print(f'Ross shouts:\n"Your pussy is on fire! Go get your crown, girl!"')
        character_dictionary['Uniqueness'] += 4
    elif event_check == 14:
        print(f'Carson claps his hands and says:\n"Oh I just loved your lip syncs, they were so fabulous!"')
        character_dictionary['Nerve'] += 6
    else:
        return character_dictionary


def perform_lyrics(lip_sync_dictionary: dict, lyric_list: list) -> bool:
    """
    Provide first set of lyrics to user.

    :param lip_sync_dictionary: a dictionary representing the lip sync song with the key 'Correct Answer' present whose
    value is a list of the correct lyrics
    :param lyric_list: a list containing multiple strings representing possible lyric selections
    :precondition: lip_sync_dictionary must be a dictionary and lyric_list must be a list
    :postcondition: determine whether the user's selection is present in the 'Correct Answer' key's value list
    :return: True if user's selection was correct else False
    """
    answer = get_challenge_input_from_user(lyric_list)
    if answer in lip_sync_dictionary['Correct Answer']:
        print("You flawlessly mouth along to the words of the song, giving you a boost in confidence.")
        return True
    else:
        print(f"You fumble a few words and inwardly curse yourself, but a short instrumental gives you the chance to"
              f" gather yourself.")
        return False


def perform_lip_sync() -> bool:
    """
    Perform full lip sync event for user.

    :precondition: event_list must be a tuple
    :postcondition: determines whether enough correct selections were made to complete event successfully
    :return: True if user was successful else False
    """
    filename = './json_files/lip_sync_data.json'
    with open(filename) as file_object:
        lip_sync_data = json.load(file_object)

    event_selection = lip_sync_data.get(random.choice(list(lip_sync_data)))

    print(f'RuPauls voice echoes:\n"Two queens stand before me. For tonight Ive asked you to prepare a lip sync '
          f'performance of {event_selection.get("Song Title")}. Ladies...\nthe time has come....'
          f'\nfor you to lip sync\nFOR\nYOUR\nLEGACY.\nThe music starts and you need to remember the first line '
          f'of the song, which do you lip sync?\n')
    correct_first_lyrics = perform_lyrics(event_selection, event_selection['Initial Lyrics'])

    print(f'You make it to the chorus and you know you have to start it off right, which do you lip sync?')
    correct_second_lyrics = perform_lyrics(event_selection, event_selection['Chorus Lyrics'])
    print(f"It's the last verse before the closing chorus, you're so close and you know you have to end strong."
          f"Which do you lip sync?")
    correct_final_lyrics = perform_lyrics(event_selection, event_selection['Final Lyrics'])
    print(f"The music stops and you catch your breath, your anticipation growing.")

    if correct_first_lyrics and (correct_second_lyrics or correct_final_lyrics):
        return True
    elif correct_second_lyrics and (correct_first_lyrics or correct_final_lyrics):
        return True
    elif correct_final_lyrics and (correct_first_lyrics or correct_second_lyrics):
        return True
    return False


def runway_event(perform_lip_sync, character_dictionary):
    """

    :param perform_lip_sync:
    :param character_dictionary:
    :return:
    """
    if perform_lip_sync(character_dictionary):
        character_setup.level_up(character_dictionary)
    else:
        character_dictionary['Nerve'] -= random.randint(5, 10)
        print(f"RuPaul's voice echoes: 'I'm sorry, {character_dictionary['Name']}, but you are safe. But I'm"
              f"willing to give you another try. Practice up and assume the position when you're ready to "
              f"try again.'\n"
              f"You hear your inner saboteur cackling.\nYou have {character_dictionary['Nerve']} Nerve "
              f"remaining.")
        return character_dictionary


def fight(player_character_dictionary, enemy_character_dictionary):
    """

    :param player_character_dictionary:
    :param enemy_character_dictionary:
    :return:
    """
    player_battle_nerve = player_character_dictionary['Nerve']
    while enemy_character_dictionary['Nerve'] > 0 and player_battle_nerve > 0:
        print("The queen stands strong, what will you do?")
        player_choice = get_challenge_input_from_user(['Read', 'Act Unimpressed', 'Flee'])
        if player_choice == 'Read':
            if random.randint(1, 20) > 2:
                print(f"You read {enemy_character_dictionary['Name']} for filth, she looks shaken.")
                enemy_character_dictionary['Nerve'] -= (random.randint(1, 8) +
                                                        math.ceil(player_character_dictionary['Charisma'] / 4))
            else:
                print(f"Your read falls flat and {enemy_character_dictionary['Name']} scoffs.")
        elif player_choice == 'Act Unimpressed':
            print("You are emotionally preparing yourself for your opponent to speak")
            player_character_dictionary['Uniqueness'] += 2
        else:
            if random.randint(1, 100) > 33:
                print("You successfully sashay away from the queen.")
            else:
                print(f"You try to get away but {enemy_character_dictionary['Name']} steps in front of you once again.")

        if random.randint(1, 20) > 4:
            damage_to_player = random.randint(1, 7) + math.ceil(enemy_character_dictionary['Charisma'] / 5)
            player_battle_nerve -= damage_to_player
            print(f"{enemy_character_dictionary['Name']} says {random.choice(POTENTIAL_READS)}.\n"
                  f"Your Nerve is reduced by {damage_to_player}.")
        else:
            print(f"{enemy_character_dictionary['Name']} has clearly never been to the library in her life.")
    if enemy_character_dictionary['Nerve'] == 0:
        print(f"{enemy_character_dictionary['Name']} slinks away, clearly feeling the shade of it all.")
        player_character_dictionary['Talent'] += random.randint(8, 12)
        return player_character_dictionary
    else:
        player_character_dictionary['Nerve'] = 0
        return player_character_dictionary


def werk_room_events(character_dictionary):
    """

    :return:
    """
    if random.randint(1, 10) <= 3:
        enemy_queen = random.choice(queens.potential_queen_challengers)
        print(f"{enemy_queen['Name']} approaches you, placing the dreaded Reading Glasses on her face as the "
              f"library opens.")
        fight(character_dictionary, enemy_queen)
    else:
        return character_dictionary


def generate_challenge_input(possible_answers: list) -> list:
    """
    """
    pairs = []

    for number, possible_answers in enumerate(possible_answers, 1):
        pair = (str(number), possible_answers)
        pairs.append(pair)
    return pairs


def get_challenge_input_from_user(possible_answers: list):

    acceptable_answers = []

    game_input = generate_challenge_input(possible_answers)

    print('Choices-------------------------------------------------------------------------')

    for pair in game_input:
        acceptable_answers += pair[0]
        print(f'{pair[0]}: {pair[1]}')

    answer = input()

    if answer not in acceptable_answers:
        print('That is not an acceptable answer! Please try again:')
        return get_challenge_input_from_user(possible_answers)

    answer_index = acceptable_answers.index(answer)
    answer_string = game_input[answer_index][1]

    return answer_string


def run_challenges(character):
    """

    :param character:
    :return:
    """
    location = character['location']
    coordinates = character['coordinates']

    if location == 'werk_room' and coordinates != (0, 4) and coordinates != (6, 4):
        return werk_room_events(character)
    if location == 'judges_panel' and coordinates != (1, 6) and coordinates != (2, 0):
        return runway_event(perform_lip_sync, character)


def main():
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lipsync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (6, 8), 'location': 'main_stage'}
    runway_event(perform_lip_sync, character)
    lyric_options = ('When all else fails and you long to be Somewhere other than you are right now',
                                   'When all else fails and you take a stand To make tomorrow a brighter day',
                                   'When all else fails and you long to be Something better than you are today')
    # print(generate_challenge_input(lyric_options))
    # print(get_challenge_input_from_user(lyric_options))


if __name__ == '__main__':
    main()


# def main(movement: bool, position: tuple, character_dictionary: dict) -> None:
#     """
#
#
#     :param movement:
#     :param position:
#     :param character_dictionary:
#     """
#     if character_dictionary.get('level') == 3:
#         judge_events(movement, character_dictionary)
#     elif character_dictionary.get('level') == 2:
#         runway_event(position, character_dictionary)
#     else:
#         werkroom_events()
#
#
# if __name__ == '__main__':
#     main()
