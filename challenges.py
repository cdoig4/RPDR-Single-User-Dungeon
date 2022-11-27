"""
Challenges for the user to help them increase their level!
"""
import random

CHER_LIP_SYNC_CHALLENGE = ['Believe by Cher', ('No matter how hard I try, you keep pushing me aside',
                                               'No matter how much effort I put in, you never let me win',
                                               'Regardless of what I do, I can never get to you'),
                           ('Do you believe in sun after rain?', 'Do you believe that you know the words?',
                            'Do you believe in life after love?'),
                           ( "I know that I'll get through this, because I found a really cool frog",
                             "Well I know that I'll get through this, Cause I know that I am strong",
                             "Well I know that I'll get through this, Cause I know that I'm not wrong")]
# MADONNA_LIP_SYNC_CHALLENGE = ['Vogue by Madonna',
#                               ('When all else fails and you long to be Something better than you are today',),
#                               ('Come on, vogue. Let your body move to the music', ),
#                               ("Magical, life's a ball So get up on the dance floor",)]
# CARLY_RAE_JEPSEN_LIP_SYNC_CHALLENGE = ['Runaway With Me by Carly Rae Jepsen',
#                                        ("You're stuck in my head, stuck in my heart, stuck in my body- body",),
#                                        ('When the lights go out, Run away with me! Run away with me!',),
#                                        ('Over the weekend, we could turn the world to gold',)]
# RUNWAY_EVENTS = [CHER_LIP_SYNC_CHALLENGE, MADONNA_LIP_SYNC_CHALLENGE, CARLY_RAE_JEPSEN_LIP_SYNC_CHALLENGE]


def judge_events(movement, character_dictionary):
    """


    :param movement:
    :param character_dictionary:
    :return:
    """
    if movement:
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
    else:
        return character_dictionary


def first_lyrics(lyric_tuple: tuple) -> bool:
    """

    :param lyric_tuple:
    :return:
    """
    print(f'The music starts and you need to remember the first line of the song, which do you lip sync?')
    for pair in list(enumerate(lyric_tuple)):
        print(f'{pair[0]}: {pair[1]}')
        if input() == 0:
            print("You flawlessly mouth along to the first words of the song, giving you a boost in confidence.")
            return True
        else:
            print(f"You fumble the first few words and your opponent performs an effortless reveal, leaving you"
                  f"shaken")
            return False


def second_lyrics(lyric_tuple: tuple) -> bool:
    """

    :param lyric_tuple:
    :return:
    """
    print(f'You make it to the chorus and you know you have to start it off right, which do you lip sync?')
    for pair in list(enumerate(lyric_tuple)):
        print(f'{pair[0]}: {pair[1]}')
        if input() == 2:
            print("You start the chorus perfectly, giving it the energy required to sell it to the judges.")
            return True
        else:
            print(f"You trip on a loose stage screw and it throws you off, and it takes you a few seconds to"
                  f"figure out where you are in the song now.")
            return False

def final_lyrics(lyric_tuple: tuple) -> bool:
    """

    :param lyric_tuple:
    :return:
    """
    print(f"It's the last verse before the closing chorus, you're so close and you know you have to end strong."
          f"Which do you lip sync?
    for pair in list(enumerate(lyric_tuple))):
        print(f"{pair[0]}: {pair[1]}")
    if input() == 1:
        print("You end the performance with a bang! The judges cheer and clap and you know you've done well.")
        return True
    else:
        print(f"You end on a sour note, while you gave it everything you had you're worried the minor mistakes"
              f"you made have seriously affected your chances.")
        return False



def perform_lip_sync(event_list: list) -> bool:
    """

    :param event_list:
    :return:
    """
    # event_check = random.randint(0, 2)
    print(f'RuPauls voice echoes:\n"Two queens stand before me. For tonight Ive asked you to prepare a lip sync '
          f'performance of {event_list[0]}. Ladies...\n the time has come....'
          f'\n for you to lip sync\nFOR\nYOUR\nLEGACY.')
    correct_first_lyrics = first_lyrics(event_list[1])
    correct_second_lyrics = second_lyrics(event_list[2])
    correct_final_lyrics = final_lyrics(event_list[3])

    if correct_first_lyrics and correct_second_lyrics or correct_final_lyrics:
        return True
    if correct_second_lyrics and correct_first_lyrics or correct_final_lyrics:
        return True
    if correct_final_lyrics and correct_first_lyrics or correct_second_lyrics:
        return True
    else:
        return False


def runway_event(position, character_dictionary):
    """

    :param position:
    :param character_dictionary:
    :return:
    """
    if position == (0, 0):
        event_results = perform_lip_sync(CHER_LIP_SYNC_CHALLENGE)
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
        else:
            character_dictionary['Nerve'] -= random.randint(5, 10)
            print(f"RuPaul's voice echoes: 'I'm sorry, {character_dictionary['Name']}, but you are safe. But I'm"
                  f"willing to give you another try. Practice up and assume the position when you're ready to "
                  f"try again.'\n"
                  f"You hear your inner saboteur cackling.\nYou have {character_dictionary['Nerve']} Nerve "
                  f"remaining.")


def main(movement: bool, position: tuple, character_dictionary: dict) -> None:
    """

    :param character_dictionary:
    """
    if character_dictionary.get('level') == 3:
        judge_events(movement, character_dictionary)
    elif character_dictionary.get('level') == 2:
        runway_events(position, character_dictionary)
    else:
        werkroom_events()


if __name__ == '__main__':
    main()
