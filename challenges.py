"""
Challenges for the user to help them increase their level!
"""
import json
import math
import random
import controls
import queens


CHER_LIP_SYNC_CHALLENGE = {'Song Title': 'Believe by Cher',
                           'Correct Answer': ['No matter how hard I try, you keep pushing me aside',
                                              'Do you believe in life after love?',
                                              "Well I know that I'll get through this, Cause I know that I am strong"],
                           'Initial Lyrics': ['No matter how hard I try, you keep pushing me aside',
                                              'No matter how much effort I put in, you never let me win',
                                              'Regardless of what I do, I can never get to you'],
                           'Chorus Lyrics': ['Do you believe in sun after rain?',
                                             'Do you believe that you know the words?',
                                             'Do you believe in life after love?'],
                           'Final Lyrics': ["I know that I'll get through this, because I found a really cool frog",
                                            "Well I know that I'll get through this, Cause I know that I am strong",
                                            "Well I know that I'll get through this, Cause I know that I'm not wrong"]}
MADONNA_LIP_SYNC_CHALLENGE = {'Song Title': 'Vogue by Madonna',
                              'Correct Answer':
                                  ['When all else fails and you long to be Something better than you are today',
                                   'Come on, vogue. Let your body move to the music',
                                   "Magical, life's a ball So get up on the dance floor"],
                              'Initial Lyrics':
                                  ['When all else fails and you long to be Somewhere other than you are right now',
                                   'When all else fails and you take a stand To make tomorrow a brighter day',
                                   'When all else fails and you long to be Something better than you are today'],
                              'Chorus Lyrics': ['Come on, vogue. Let your body move to the music',
                                                'Come on, vogue. Let yourself get into the groovin',
                                                "Hey let's vogue. Nod your head to the beat"],
                              'Final Lyrics': ["Beautiful, life's magical So let the music take you home",
                                               "Magic, in the ballroom So get onto the cat walk",
                                               "Magical, life's a ball So get up on the dance floor", ]}
CARLY_RAE_JEPSEN_LIP_SYNC_CHALLENGE = {'Song Title': 'Run Away With Me by Carly Rae Jepsen',
                                       'Correct Answer':
                                           ["You're stuck in my head, stuck in my heart, stuck in my body- body",
                                            'When the lights go out, Run away with me! Run away with me!',
                                            'Over the weekend, we could turn the world to gold'],
                                       'Initial Lyrics':
                                           ["You're stuck on my shoe, stuck on my sole, please get off me- off me",
                                            "You're stuck in my head, stuck in my heart, stuck in my body- body",
                                            f"You're stuck in my head, stuck in my heart, "
                                            f"we're both at the party- party"],
                                       'Chorus Lyrics': [f'When the power goes out, Come and look for me! '
                                                         f'Come and look for me!',
                                                         'When the lights go out, Run away with me! Run away with me!',
                                                         'When the lights go out, We have to leave! We have to leave!'],
                                       'Final Lyrics': ["What's that smell, I think it might be mold.",
                                                        'Over the weekend, we could turn the world to gold',
                                                        'Over the summer, we could make the world turn gold']}
LIP_SYNCS = (CHER_LIP_SYNC_CHALLENGE, MADONNA_LIP_SYNC_CHALLENGE, CARLY_RAE_JEPSEN_LIP_SYNC_CHALLENGE)
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


def perform_lip_sync(character: dict) -> dict:
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
        character = character.update({'completed_lipsync': True})
    elif correct_second_lyrics and (correct_first_lyrics or correct_final_lyrics):
        character = character.update({'completed_lipsync': True})
    elif correct_final_lyrics and (correct_first_lyrics or correct_second_lyrics):
        character = character.update({'completed_lipsync': True})
    return character


def runway_event(character_dictionary):
    """

    :param character_dictionary:
    :return:
    """
    event_results = perform_lip_sync(LIP_SYNCS)
    if event_results:
        character_dictionary['level'] += 1
        character_dictionary['Charisma'] += random.randint(20, 30)
        character_dictionary['Uniqueness'] += random.randint(20, 30)
        character_dictionary['Nerve'] += random.randint(20, 30)
        print(f"RuPaul's voice echoes: 'ConDRAGulations {character_dictionary['Name']}, you're a winner baby!'\n"
              f"You feel your inner saboteur melting away.\nYou are now level {character_dictionary['level']}\n"
              f"Your Charisma increases to {character_dictionary['Charisma']}!\nYour Uniqueness increases to"
              f" {character_dictionary['Uniqueness']}!\nYour Nerve increases to {character_dictionary['Nerve']}"
              f"\nYou are ushered towards the Judge's Panel.")
        return character_dictionary
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
    while enemy_character_dictionary['Nerve'] > 0 and player_character_dictionary['Nerve'] > 0:
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
            player_character_dictionary['Nerve'] -= damage_to_player
            print(f"{enemy_character_dictionary['Name']} says {random.choice(POTENTIAL_READS)}.\n"
                  f"Your Nerve is reduced by {damage_to_player}.")
        else:
            print(f"{enemy_character_dictionary['Name']} has clearly never been to the library in her life.")


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
    location = character.get('location')
    coordinates = character.get('coordinates')

    if location == 'werk_room' and coordinates != (0, 4) and coordinates != (6, 4):
        return werk_room_events(character)
    if location == 'judges_panel' and coordinates != (1, 6) and coordinates != (2, 0):
        return perform_lip_sync(character)


def main():
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lipsync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (6, 8), 'location': 'main_stage'}
    perform_lip_sync(character)
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
