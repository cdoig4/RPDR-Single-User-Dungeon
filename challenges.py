"""
Challenges for the user to help them increase their level!
"""
import json
import math
import random
import character_setup

RUPAUL_READS = ("I never thought I'd meet a queen whose heels weigh more than her brain",
                "I've always wondered what the female Gremlin would look like in 25 years. Now I know.",
                f"Those other queens have been saying you have terrible makeup skills, no fashion sense, and you're"
                f"dumb as a rock. But they're wrong...\n you don't have terrible makeup skills.")
RUPAUL_LIP_SYNC = {'Correct Answer': ["Who you waiting for? Another savior",
                                      "Who do you think you are? I'm telling the truth now",
                                      "I'll say it again It's never been the clothes that make the man"],
                   'Initial Lyrics': ["Who you waiting for? Another savior",
                                      "What you waiting for? Your best behaviour",
                                      "Who is that for? Another favor"],
                   'Chorus Lyrics': ["Where did you get that car? I'm going to Buick now",
                                     "Who do you think you are? I'm telling the truth now",
                                     "Who do you think you are? You're blowing a fuse now"],
                   'Final Lyrics': ["I'll say it again It's never been me who meets the fans",
                                    "I'll say it again It's always been the wig that makes the queen",
                                    "I'll say it again It's never been the clothes that make the man"]}

POTENTIAL_READS = ('Legendary you think you are. Legendary? Looks like leg AND dairy.', 'Beauty fades, dumb is forever',
                   'The last time you got fucked was by genetics')


def judge_events(character):
    """
    Provide possible random events for each character movement.

    :param character: a dictionary representing the player character
    :precondition: movement must be a Boolean and character must be a dictionary with the keys 'Charisma',
    'Uniqueness', and 'Nerve' present and each must have a positive integer for their value
    :postcondition: determine whether a random judge event happens or not
    :return: character that has either not been altered or has had a single value altered based which event
    occured
    """
    event_check = random.randint(1, 20)
    if event_check == 1:
        print(f'Michelle glares at you and says:\n"That dress is hideous. Where did you get it, Party City?"')
        character_setup.power_up_or_down(character, [-5, 0, 0, 0])
    elif event_check == 7:
        print(f'Ross shouts:\n"Your pussy is on fire! Go get your crown, girl!"')
        character_setup.power_up_or_down(character, [0, 4, 0, 0])
    elif event_check == 14:
        print(f'Carson claps his hands and says:\n"Oh I just loved your lip syncs, they were so fabulous!"')
        character_setup.power_up_or_down(character, [0, 0, 6, 0])
    else:
        return character


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


def runway_event(perform_lip_sync, character):  # can be removed
    """

    :param perform_lip_sync:
    :param character:
    :return:
    """
    if perform_lip_sync(character):
        character_setup.check_for_level_up(character)
    else:
        character['Nerve'] -= random.randint(5, 10)
        print(f"RuPaul's voice echoes: 'I'm sorry, {character['Name']}, but you are safe. But I'm"
              f"willing to give you another try. Practice up and assume the position when you're ready to "
              f"try again.'\n"
              f"You hear your inner saboteur cackling.\nYou have {character['Nerve']} Nerve "
              f"remaining.")
        return character


def fight(character):
    """

    :param character:
    :return:
    """
    filename = './json_files/queens.json'
    with open(filename) as file_object:
        queens = json.load(file_object)
    queen_names = list(queens.keys())
    enemy_queen = random.choice(queen_names)

    print(f"{queens[enemy_queen]['Name']} approaches you, placing the dreaded Reading Glasses on her face as the "
          f"library opens.")

    player_battle_nerve = character['Nerve']
    enemy_battle_nerve = queens[enemy_queen]['Nerve']
    while enemy_battle_nerve > 0 and player_battle_nerve > 0:
        print("The queen stands strong, what will you do?")
        player_choice = get_challenge_input_from_user(['Read', 'Act Unimpressed', 'Flee'])
        if player_choice == 'Read':
            if random.randint(1, 20) > 2:
                print(f"You read {queens[enemy_queen]['Name']} for filth, she looks shaken.")
                enemy_battle_nerve -= (random.randint(1, 8) +
                                       math.ceil(character['Charisma'] / 4))
            else:
                print(f"Your read falls flat and {queens[enemy_queen]['Name']} scoffs.")
        elif player_choice == 'Act Unimpressed':
            print("You are emotionally preparing yourself for your opponent to speak")
            character_setup.power_up_or_down(character, [0, 2, 0, 0])
        elif player_choice == 'Flee':
            if random.randint(1, 100) > 33:
                print("You successfully sashay away from the queen.")
            else:
                print(f"You try to get away but {queens[enemy_queen]['Name']} steps in front of you once again.")

        if random.randint(1, 20) > 4:
            damage_to_player = -(random.randint(1, 3) + math.ceil(queens[enemy_queen]['Charisma'] / 5))
            print(f"{queens[enemy_queen]['Name']} says {random.choice(POTENTIAL_READS)}.")
            character_setup.power_up_or_down(character, [0, 0, damage_to_player, 0])
            character_setup.check_if_dead(character)
        else:
            print(f"{queens[enemy_queen]['Name']} has clearly never been to the library in her life.")

    if enemy_battle_nerve <= 0:
        return character_setup.you_win(character, queens[enemy_queen]['Name'], 'fight')
    else:
        character['Nerve'] = 0
        return character


def final_lip_sync(character):
    """

    :param character:
    """
    print(f"RuPaul shouts \"The library is officially closed! Now {character['Name']}\""
          f"...\nThe time has come...\nFor you to Lip Sync....\nFor. The. CROWN.\"\nThe lights"
          f" dim and the familiar beat of a RuPaul song begins.\n"
          f"Which do you lip sync?")
    correct_first_lyrics = perform_lyrics(event_selection, event_selection['Initial Lyrics'])
    print(f'You continue your performance, knowing that it all comes down to this. Your entire journey has come down'
          f'to one last performance\nWhich do you lip sync?')
    correct_second_lyrics = perform_lyrics(event_selection, event_selection['Chorus Lyrics'])
    print(f"It's the final stretch. You've pulled out all your tricks and you know you have to end strong.\n"
          f"Which do you lip sync?")
    correct_final_lyrics = perform_lyrics(event_selection, event_selection['Final Lyrics'])
    print(f"The song ends. You stand in your pose, breathing heavily as RuPaul watches you. Her face a mask.")
    if correct_first_lyrics and (correct_second_lyrics or correct_final_lyrics):
        return character.update({'met_rupaul': True})
    elif correct_second_lyrics and (correct_first_lyrics or correct_final_lyrics):
        return character.update({'met_rupaul': True})
    elif correct_final_lyrics and (correct_first_lyrics or correct_second_lyrics):
        return character.update({'met_rupaul': True})
    return character.update({'Nerve': 0})


def final_battle(character_dictionary):
    """

    :param character_dictionary:
    """
    filename = './json_files/queens.json'
    with open(filename) as file_object:
        queens = json.load(file_object)
        queen_bitch_rupaul = queens.get('queen_bitch_rupaul')

    while queen_bitch_rupaul['Nerve'] > 35 and character_dictionary['Nerve'] > 0:
        print("Mother stands strong, what will you do?")
        player_choice = get_challenge_input_from_user(['Read', 'Act Unimpressed', 'Flee'])
        if player_choice == 'Read':
            if random.randint(1, 20) > 2:
                print(f"You read {queen_bitch_rupaul['Name']} for the gods... her eye twitches slightly.")
                queen_bitch_rupaul['Nerve'] -= (random.randint(1, 8) + math.ceil(character_dictionary['Charisma'] / 4))
            else:
                print(f"Your read falls flat and {queen_bitch_rupaul['Name']} chuckles.")
        elif player_choice == 'Act Unimpressed':
            print("You are emotionally preparing yourself for RuPaul to read you for filth.")
            character_dictionary['Uniqueness'] += 2
        else:
            print(f'{queen_bitch_rupaul["Name"]} says: "That\'s cute. You are staying right here till we\'re done"')

        if random.randint(1, 20) > 4:
            damage_to_player = random.randint(1, 7) + math.ceil(queen_bitch_rupaul['Charisma'] / 10)
            character_dictionary['Nerve'] -= damage_to_player
            print(f"{queen_bitch_rupaul['Name']} says {random.choice(RUPAUL_READS)}.\n"
                  f"Your Nerve is reduced by {damage_to_player}.")
        else:
            print(f"{queen_bitch_rupaul['Name']} throws out a read that goes over your head.")

    if character_dictionary['Nerve'] > 0:
        final_lip_sync(character_dictionary)

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
        if random.randint(1, 10) <= 3:
            return fight(character)
    if location == 'main_stage' and coordinates == (0, 0) #placeholder:
        return perform_lip_sync()
    if location == 'judges_panel' and coordinates != (1, 6) and coordinates != (2, 0):
        return runway_event(perform_lip_sync, character)


def main():
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lipsync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (6, 8), 'location': 'main_stage'}
    # runway_event(perform_lip_sync, character)
    lyric_options = ('When all else fails and you long to be Somewhere other than you are right now',
                                   'When all else fails and you take a stand To make tomorrow a brighter day',
                                   'When all else fails and you long to be Something better than you are today')
    # print(generate_challenge_input(lyric_options))
    # print(get_challenge_input_from_user(lyric_options))
    fight(character)


if __name__ == '__main__':
    main()
