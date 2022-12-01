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


def final_lip_sync(character_dictionary):
    """

    :param character_dictionary:
    """
    print(f"RuPaul shouts \"The library is officially closed! Now {character_dictionary['Name']}\""
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
        print(f"RuPaul's face breaks into a smile. \"ConDRAGulations {character_dictionary['Name']}"
              f"you're the winner baby!\"\nTriumphant music starts up as confetti begins to fall from the ceiling.\n"
              f"\"You are now the Queen of the Mother Tucking UNIVERSE!\" Mother continues as she places a massive "
              f"bejeweled crown upon your head and a matching scepter in your hand.\nYou sob with happiness as you"
              f"know that this... is the beginning of the rest of your life.\nEND.")
        return character_dictionary.update({'met_rupaul': True})
    elif correct_second_lyrics and (correct_first_lyrics or correct_final_lyrics):
        print(f"RuPaul's face breaks into a smile. \"ConDRAGulations {character_dictionary['Name']}"
              f"you're the winner baby!\"\nTriumphant music starts up as confetti begins to fall from the ceiling.\n"
              f"\"You are now the Queen of the Mother Tucking UNIVERSE!\" Mother continues as she places a massive "
              f"bejeweled crown upon your head and a matching scepter in your hand.\nYou sob with happiness as you"
              f"know that this... is the beginning of the rest of your life.\nEND.")
        return character_dictionary.update({'met_rupaul': True})
    elif correct_final_lyrics and (correct_first_lyrics or correct_second_lyrics):
        print(f"RuPaul's face breaks into a smile. \"ConDRAGulations {character_dictionary['Name']}"
              f"you're the winner baby!\"\nTriumphant music starts up as confetti begins to fall from the ceiling.\n"
              f"\"You are now the Queen of the Mother Tucking UNIVERSE!\" Mother continues as she places a massive "
              f"bejeweled crown upon your head and a matching scepter in your hand.\nYou sob with happiness as you"
              f"know that this... is the beginning of the rest of your life.\nEND.")
        return character_dictionary.update({'met_rupaul': True})
    return character_dictionary.update({'Nerve': 0})


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

    if character_dictionary['Nerve'] != 0:
        final_lip_sync(character_dictionary)
