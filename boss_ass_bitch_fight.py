"""
The time has come.... to Lip Sync for your mother tucking LIFE!!!
"""
import json
import random
import math

RUPAUL_READS = ("I never thought I'd meet a queen whose heels weigh more than her brain",
                "I've always wondered what the female Gremlin would look like in 25 years. Now I know.",
                f"Those other queens have been saying you have terrible makeup skills, no fashion sense, and you're"
                f"dumb as a rock. But they're wrong...\n you don't have terrible makeup skills.")


def final_battle(character_dictionary):
    """

    :param character_dictionary:
    """
    filename = './json_files/potential_queen_challengers.json'
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

    if character_dictionary['Nerve'] != 0:
        final_lipsync()
