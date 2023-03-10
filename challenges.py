"""
Challenges for the user to help them increase their level!
"""


import json
import math
import random
import character_setup
import itertools


def read_battle(character: dict) -> dict:
    """
    Run read_battle event for player.

    :param character: a dictionary representing the player character with the keys
    'Charisma', 'Uniqueness', and 'Nerve' present with each of their values being positive integers
    :precondition: character must be a dictionary
    :precondition: input must be provided by the user for the function to complete
    :postcondition: randomly pulls a queen dictionary from a JSON file and sets them as the enemy
    :postcondition: update player and queen stats throughout gameplay
    :postcondition: run combat for the player
    :postcondition: set player health ('Nerve') back to full on success
    :postcondition: print combat events as they occur
    :postcondition: run functions check_if_dead, power_up_or_down and you_win based on events
    :return: character dictionary updated to reflect in-game events
    """
    potential_reads = ('Legendary you think you are. Legendary? Looks like leg AND dairy.',
                       'Beauty fades, dumb is forever',
                       'The last time you got fucked was by genetics')

    filename = './json_files/queens.json'
    with open(filename) as file_object:
        queens = json.load(file_object)

    queen_names = list(queens.keys())
    queen_names.remove('queen_bitch_rupaul')
    enemy_queen = random.choice(queen_names)

    print(f"{queens[enemy_queen]['Name']} approaches you, placing the dreaded Reading Glasses on "
          f"her face as\nthe library opens.")

    starting_nerve = character['Nerve']
    while queens[enemy_queen]['Nerve'] > 0:
        print("The queen stands strong, what will you do?")
        player_choice = get_challenge_input_from_user(['Read', 'Act Unimpressed', 'Flee'])
        if player_choice == 'Read':
            if random.randint(1, 20) > 2:
                print(f"You read {queens[enemy_queen]['Name']} for filth, she looks shaken.")
                damage = -(random.randint(1, 8) + math.ceil(character['Charisma'] / 4))
                character_setup.power_up_or_down(queens[enemy_queen],
                                                 [random.choice([-1, 0]), damage], True)
            else:
                print(f"Your read falls flat and {queens[enemy_queen]['Name']} scoffs.")
        elif player_choice == 'Act Unimpressed':
            print("You are emotionally preparing yourself for your opponent to speak")
            character_setup.power_up_or_down(character, [0, 2, 0, 0], False)
        elif player_choice == 'Flee':
            if random.randint(1, 100) > 33:
                print("You successfully sashay away from the queen.")
                return character_setup.power_up_or_down(character, [0, 0, 0, 0], False)
            else:
                print(f"You try to get away but {queens[enemy_queen]['Name']} steps in front of "
                      f"you once again.")

        if queens[enemy_queen]['Nerve'] > 0:
            if random.randint(1, 20) > 6:
                damage_to_player = -(random.randint(1, 3)
                                     + math.ceil(queens[enemy_queen]['Charisma'] / 5))
                print(f"{queens[enemy_queen]['Name']} says {random.choice(potential_reads)}.")
                character_setup.power_up_or_down(character, [0, 0, damage_to_player, 0], False)
                character_setup.check_if_dead(character)
            else:
                print(f"{queens[enemy_queen]['Name']}'s read is laughably bad and has no effect!"
                      f"\nShe's clearly never been to the library in her life.")

    if character['level'] != 2:
        character['Nerve'] = starting_nerve
        character_setup.you_win(character, queens[enemy_queen]['Name'], 'read_battle')
        return character_setup.check_for_level_up(character)
    else:
        character.update({'Nerve': 0})
        return character


def generate_random_answers(correct_answer: tuple) -> list:
    """
    Get all permutations of a tuple and return a random list of 4 tuples including the original.

    :param correct_answer: a tuple
    :precondition: correct_answer must be a tuple
    :postcondition: generate all permutations of a tuple and return a random list of 4 tuples
    including the original
    :return: a random list of 4 tuples with 1 being the original and 3 others being randomly
    selected permutations of the original
    """
    all_permutations = list(itertools.permutations(correct_answer))
    all_permutations.remove(tuple(correct_answer))
    random.shuffle(all_permutations)
    sliced = all_permutations[:3]
    sliced.append(tuple(correct_answer))
    random.shuffle(sliced)
    return sliced


def makeover_challenge(character: dict) -> dict:
    """
    Run makeover challenge for player character.

    :param character: a dictionary representing the player character with the key 'Name' present
    whose assigned value must be a string
    :precondition: character must be a dictionary
    :precondition: input must be provided by the user for the function to complete
    :postcondition: runs makeup challenge for player
    :postcondition: determine whether player succeeds or fails challenge
    :postcondition: print in-game events to user
    :postcondition: run you_win, power_up_or_down, and check_for_level_up based on game events
    :return: character dictionary updated to reflect in-game events
    """
    makeup_question = ('Foundation', 'Eye shadow', 'Contouring')
    lips_question = ('Lip Liner', 'Lipstick', 'Lip Gloss')
    outfit_question = ('Gown', 'Shoes', 'Wig')

    filename = './json_files/queens.json'
    with open(filename) as file_object:
        queens = json.load(file_object)
    queen_names = list(queens.keys())
    queen_names.remove('queen_bitch_rupaul')
    fellow_queen = random.choice(queen_names)
    correct_answers = 0

    print(f"You hear RuPaul's voice:\n\"My queens!\nYou have 10 minutes to put one of your fellow "
          f"queens into the best quick drag\nyou can manage. Get to it!\"\n\nYou run up to "
          f"{queens[fellow_queen]['Name']}, ready to beat her face for the gods.\nYou know that "
          f"in order to get the best results, you have to put the makeup\non in the right order."
          f"\nWhat order do you apply makeup in?")
    first_answer = get_challenge_input_from_user(generate_random_answers(makeup_question))
    if first_answer == makeup_question:
        correct_answers += 1
        print(f"You take a step back to admire your work. {queens[fellow_queen]['Name']} is looking"
              f" fierce!")
    else:
        print(f"You take a step back to examine {queens[fellow_queen]['Name']}'s face. It's looking"
              f" a little busted.")
    print(f"Next you have to do the lips. What order do you apply makeup in?")
    second_answer = get_challenge_input_from_user(generate_random_answers(lips_question))
    if second_answer == lips_question:
        correct_answers += 1
        print(f"{queens[fellow_queen]['Name']}'s lips are looking luscious and divine! Way to go!")
    else:
        print(f"{queens[fellow_queen]['Name']}'s lips are looking a little crusty and dusty,\nbut "
              f"you don't have time to fix them right now.")
    print(f"You hear a call for one minute left and you rush to get {queens[fellow_queen]['Name']}"
          f"\ninto an outfit! What order do you dress her in?")
    final_answer = get_challenge_input_from_user(generate_random_answers(outfit_question))
    if final_answer == outfit_question:
        correct_answers += 1
        print(f"You finish dressing {queens[fellow_queen]['Name']} and the outfit looks "
              f"stunning on her!")
    else:
        print(f"You finish dressing {queens[fellow_queen]['Name']} but her wig is sliding back and"
              f" she has major\ncliffhangers because the shoes are way too small.")
    print(f"RuPaul walks in wearing a Klein Epstein & Parker suit and examines each pair of\n"
          f"queens. She clears her throat in preparation to deliver the results...")
    if correct_answers > 1:
        character_setup.you_win(character, queens[fellow_queen]['Name'], 'makeover_challenge')
        return character_setup.check_for_level_up(character)
    else:
        print(f"...and gives the win to another team, who you have to admit look fucking fierce."
              f"\nYou feel your confidence wane slightly.")
        return character_setup.power_up_or_down(character, [-2, 0, 0, 0], False)


def judge_events(character: dict):
    """
    Provide possible random events for each character movement.

    :param character: a dictionary representing the player character
    :precondition: character must be a dictionary with the keys 'Charisma', 'Uniqueness', 'Nerve',
    and 'Talent' present
    and each must have a positive integer for their value
    :postcondition: print in-game events to user
    :postcondition: determine whether a random judge event happens or not
    :return: character dictionary updated to reflect in-game events
    """
    event_check = random.randint(1, 10)
    if event_check == 1:
        print(f'Michelle glares at you and says:\n"That dress is hideous. Where did you get it,'
              f' Party City?"')
        character_setup.power_up_or_down(character, [-5, 0, 0, 0], True)
        return get_challenge_input_from_user(['Continue'])
    elif event_check == 2:
        print(f'Ross shouts:\n"Your pussy is on fire! Go get your crown, girl!"')
        character_setup.power_up_or_down(character, [0, 4, 0, 0], True)
        return get_challenge_input_from_user(['Continue'])
    elif event_check == 3:
        print(f'Carson claps his hands and says:\n"Oh I just loved your lip syncs, they were so '
              f'fabulous!"')
        character_setup.power_up_or_down(character, [0, 0, 6, 0], True)
        return get_challenge_input_from_user(['Continue'])
    else:
        return character


def perform_lyrics(lip_sync_dictionary: dict, lyric_list: list) -> bool:
    """
    Perform section of lip sync event for player.

    :param lip_sync_dictionary: a dictionary representing the lip sync song with the key
    'Correct Answer' present whose value is a list of the correct lyrics
    :param lyric_list: a list containing multiple strings representing possible lyric selections
    :precondition: lip_sync_dictionary must be a dictionary and lyric_list must be a list
    :postcondition: receive input from player representing their answer
    :postcondition: determine whether the player's selection is present in the 'Correct Answer'
    key's value list
    :postcondition: print a positive statement on user success else print a negative statement
    :return: True if user's selection was correct else False
    """
    answer = get_challenge_input_from_user(lyric_list)
    if answer in lip_sync_dictionary['Correct Answer']:
        print("You flawlessly mouth the words of the song, giving you a boost in confidence.")
        return True
    else:
        print(f"You fumble a few words and inwardly curse yourself,\nbut a short instrumental gives"
              f" you the chance to gather yourself.")
        return False


def main_stage_lip_sync(character: dict) -> dict:
    """
    Run lip sync event for player.

    :param character: a dictionary representing the player character which contains the keys 'Name'
    'completed_lip_sync', and 'Nerve' where the value assigned to 'Name' is a string, the value
    assigned to 'completed_lip_sync' is a Boolean, and the value assigned to 'Nerve' is a
    positive integer
    :precondition: character must be a dictionary
    :precondition: input must be provided by the user for the function to complete
    :postcondition: print in-game events to user
    :postcondition: run the lip sync event for the player
    :postcondition: determine whether the player provided enough correct answers to pass the event
    :postcondition: set value assigned to 'completed_lip_sync' key in player character dictionary
    to True
    :return: character dictionary updated to reflect in-game events
    """
    filename = './json_files/lip_sync_data.json'
    with open(filename) as file_object:
        lip_sync_data = json.load(file_object)

    event_selection = lip_sync_data.get(random.choice(list(lip_sync_data)))

    print(f'RuPauls voice echoes:\n"Two queens stand before me. For tonight Ive asked you to '
          f'prepare a lip sync performance of {event_selection.get("Song Title")}. '
          f'Ladies...\nthe time has come....\nfor you to lip sync\nFOR\nYOUR\nLEGACY.\n'
          f'The music starts and you need to remember the first line of the song, which do you '
          f'lip sync?\n')
    correct_first_lyrics = perform_lyrics(event_selection, event_selection['Initial Lyrics'])

    print(f'You make it to the chorus and you know you have to start it off right,\nwhich do you '
          f'lip sync?')
    correct_second_lyrics = perform_lyrics(event_selection, event_selection['Chorus Lyrics'])
    print(f"It's the last verse before the closing chorus,\nyou're so close and you know you have "
          f"to end strong.\nWhich do you lip sync?")
    correct_final_lyrics = perform_lyrics(event_selection, event_selection['Final Lyrics'])
    print(f"The music stops and you catch your breath, your anticipation growing.")

    if correct_first_lyrics and (correct_second_lyrics or correct_final_lyrics):
        character["completed_lip_sync"] = True
        return character_setup.you_win(character, None, 'lip_sync')
    elif correct_second_lyrics and (correct_first_lyrics or correct_final_lyrics):
        character["completed_lip_sync"] = True
        return character_setup.you_win(character, None, 'lip_sync')
    elif correct_final_lyrics and (correct_first_lyrics or correct_second_lyrics):
        character["completed_lip_sync"] = True
        return character_setup.you_win(character, None, 'lip_sync')
    else:
        character_setup.power_up_or_down(character, [0, 0, -random.randint(5, 10), 0], False)
        character['coordinates'] = (6, 7)
        print(f"RuPaul's voice echoes:\n\"I'm sorry, {character['Name']}, you didn't win.\nBut..."
              f" I'm willing to give you another try. Practice up and assume the position\n"
              f"when you're ready to try again.\"\nYou hear your inner saboteur cackling.\nYou have"
              f" {character['Nerve']} Nerve remaining.")
    return character


def final_lip_sync(character: dict) -> dict:
    """
    Run final lip sync challenge for the player.

    :param character: a dictionary representing the player character with the key 'Name' present
    whose assigned value is a string
    :precondition: character must be a dictionary
    :precondition: input must be provided by the user via perform_lyrics for the function to
    complete
    :postcondition: print in-game events to user
    :postcondition: determine whether the player successfully completed the challenge or not
    :return: character dictionary updated to reflect in-game events
    """
    filename = './json_files/rupaul_lip_sync.json'
    with open(filename) as file_object:
        event_selection = json.load(file_object)

    print(f"\nRuPaul shouts \"The library is officially closed! Now {character['Name']}\""
          f"...\n\nThe time has come...\nFor you to Lip Sync....\nFor. \nThe."
          f"\nCROWN.\n\nThe lights dim and the familiar beat of a RuPaul song begins.\n"
          f"Which do you lip sync?")
    correct_first_lyrics = perform_lyrics(event_selection, event_selection['Initial Lyrics'])
    print(f'You continue your performance, knowing that it all comes down to this.\nYour entire '
          f'journey has come down to one last performance\nWhich do you lip sync?')
    correct_second_lyrics = perform_lyrics(event_selection, event_selection['Chorus Lyrics'])
    print(f"It's the final stretch.\nYou've pulled out all your tricks and you know you have to "
          f"end strong.\nWhich do you lip sync?")
    correct_final_lyrics = perform_lyrics(event_selection, event_selection['Final Lyrics'])
    print(f"\nThe song ends. You stand in your pose, breathing heavily as RuPaul watches you.\n"
          f"Her face a mask...")
    if correct_first_lyrics and (correct_second_lyrics or correct_final_lyrics):
        return character_setup.you_win(character, 'rupaul', 'rupaul')
    elif correct_second_lyrics and (correct_first_lyrics or correct_final_lyrics):
        return character_setup.you_win(character, 'rupaul', 'rupaul')
    elif correct_final_lyrics and (correct_first_lyrics or correct_second_lyrics):
        return character_setup.you_win(character, 'rupaul', 'rupaul')
    character['Nerve'] = 0
    return character_setup.check_if_dead(character)


def final_battle(character: dict) -> None:
    """
    Run final battle event for player.

    :param character: a dictionary representing the player character with the keys 'Name',
    'Charisma', and 'Nerve' present, where the value assigned to 'Name' is a string, and the values
    assigned to 'Charisma' and 'Nerve' are both positive integers
    :precondition: character must be a dictionary
    :precondition: input must be provided by the user for the function to complete
    :postcondition: runs the final battle for the player
    :postcondition: print in-game events as they occur
    :postcondition: determine whether the player is successful in the final battle or not
    :postcondition: run final_lip_sync function if player character's health ('Nerve') does not
    reach or go below 0 before RuPaul's drops below 35
    """
    rupaul_reads = ("I never thought I'd meet a queen whose heels weigh more than her brain",
                    "I've always wondered what the female Gremlin would look like in 25 years."
                    "\nNow I know.",
                    "those other queens have been saying you have terrible makeup skills,"
                    "\nno fashion sense, and you're dumb as a rock. But they're wrong...\n"
                    "You don't have terrible makeup skills.")

    filename = './json_files/queens.json'
    with open(filename) as file_object:
        queens = json.load(file_object)
        queen_bitch_rupaul = queens.get('queen_bitch_rupaul')

    while queen_bitch_rupaul['Nerve'] > 35 and character['Nerve'] > 0:
        print("Mother stands strong, what will you do?")
        player_choice = get_challenge_input_from_user(['Read', 'Act Unimpressed', 'Flee'])
        if player_choice == 'Read':
            if random.randint(1, 20) > 2:
                print(f"You read {queen_bitch_rupaul['Name']} for the gods... "
                      f"her eye twitches slightly.")
                rupaul_damage = -(random.randint(1, 8) + math.ceil(character['Charisma'] / 6))
                character_setup.power_up_or_down(queen_bitch_rupaul, [0, rupaul_damage], True)
            else:
                print(f"Your read falls flat and {queen_bitch_rupaul['Name']} chuckles.")
        elif player_choice == 'Act Unimpressed':
            print("You are emotionally preparing yourself for RuPaul to read you for filth.")
            character_setup.power_up_or_down(character, [0, 6, 0, 0], True)
        else:
            print(f'{queen_bitch_rupaul["Name"]} says: "That\'s cute. '
                  f'You are staying right here till we\'re done"')

        if random.randint(1, 20) > 4:
            damage_to_player = -(random.randint(1, 7)
                                 + math.ceil(queen_bitch_rupaul['Charisma'] / 10))
            print(f"{queen_bitch_rupaul['Name']} says,\n\"{random.choice(rupaul_reads)}.\"")
            character_setup.power_up_or_down(character, [0, 0, damage_to_player, 0], False)
            character_setup.check_if_dead(character)
        else:
            print(f"{queen_bitch_rupaul['Name']} throws out a read that goes over your head.")

    if character['Nerve'] > 0:
        final_lip_sync(character)


def generate_challenge_input(possible_answers: list) -> list:
    """
    Generate potential inputs for player.

    :param possible_answers: a list of strings
    :precondition: possible_answers must be a list
    :postcondition: enumerate the list to show each potential input option
    :return: list of tuples representing all potential inputs
    >>> generate_challenge_input(['Option Number One', 2, -3.0])
    [('1', 'Option Number One'), ('2', 2), ('3', -3.0)]
    >>> generate_challenge_input([])
    []
    """
    pairs = []

    for number, possible_answers in enumerate(possible_answers, 1):
        pair = (str(number), possible_answers)
        pairs.append(pair)
    return pairs


def get_challenge_input_from_user(possible_answers: list) -> str:
    """
    Receive answer input from player.

    :param possible_answers: a list
    :precondition: possible_answers must be a list
    :precondition: input must be provided by the user for the function to complete
    :postcondition: print potential input options for player
    :postcondition: receive answer input from player
    :postcondition: raise SystemExit if player input is quit
    :postcondition: run recursively until input from possible accepted answers or 'quit' is given
    :return: a string representing the answer chosen by the player
    """
    acceptable_answers = []

    game_input = generate_challenge_input(possible_answers)

    print('Choices-------------------------------------------------------------------------')

    for pair in game_input:
        acceptable_answers += pair[0]
        print(f'{pair[0]}: {pair[1]}')

    answer = input()

    if answer == 'quit':
        raise SystemExit("You quit the game.")
    elif answer not in acceptable_answers:
        print('That is not an acceptable answer! Please try again:')
        return get_challenge_input_from_user(possible_answers)

    answer_index = acceptable_answers.index(answer)
    answer_string = game_input[answer_index][1]

    return answer_string


def run_challenges(character: dict):
    """
    Run challenges for player.

    :param character: a dictionary representing the player character with the keys 'location',
    'coordinates', and 'level' present where the value assigned to 'location' is a string, the
    value assigned to 'coordinates' is a tuple containing two positive integers, and the value
    assigned to 'level' is a positive integer
    :precondition: character must be a dictionary
    :postcondition: determine if a challenge is run based on the values stored in character
    :return: read_battle function if the value assigned to 'location' is 'werk_room', the value
    assigned to 'coordinates' is not (0, 4) or (6, 4) and the value assigned to 'level' is not 2,
    main_stage_lip_sync function if the value assigned to 'location' is 'main_stage' and the value
    assigned to 'coordinates' is (6, 8), judge_events function if the value assigned to 'location'
    is 'judges_panel' and the value assigned to 'coordinates' is not (1, 6) or (2, 0)
    """
    location = character['location']
    coordinates = character['coordinates']

    if location == 'werk_room' and coordinates != (0, 4) and coordinates != (6, 4) \
            and character['level'] != 2:
        if random.randint(1, 10) <= 3:
            return read_battle(character)
    if location == 'main_stage' and coordinates == (6, 8):
        return main_stage_lip_sync(character)
    if location == 'judges_panel' and coordinates != (1, 6) and coordinates != (2, 0):
        return judge_events(character)


def main():
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lip_sync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (6, 8), 'location': 'main_stage'}
    print('The following to functions utilize most of the functions within this module and how '
          'they work in tandem.')
    run_challenges(character)
    read_battle(character)


if __name__ == '__main__':
    main()
