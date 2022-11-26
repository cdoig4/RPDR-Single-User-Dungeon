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
MADONNA_LIP_SYNC_CHALLENGE = ['Vogue by Madonna',
                              ('When all else fails and you long to be Something better than you are today',),
                              ('Come on, vogue. Let your body move to the music', ),
                              ("Magical, life's a ball So get up on the dance floor",)]
CARLY_RAE_JEPSEN_LIP_SYNC_CHALLENGE = ['Runaway With Me by Carly Rae Jepsen',
                                       ("You're stuck in my head, stuck in my heart, stuck in my body- body",),
                                       ('When the lights go out, Run away with me! Run away with me!',),
                                       ('Over the weekend, we could turn the world to gold',)]
RUNWAY_EVENTS = [CHER_LIP_SYNC_CHALLENGE, MADONNA_LIP_SYNC_CHALLENGE, CARLY_RAE_JEPSEN_LIP_SYNC_CHALLENGE]


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


def perform_lip_sync(event_nested_list):
    """

    :param event_nested_list:
    :return:
    """
    event_check = random.randint(0, 2)
    print(f'Rupauls voice echoes:\n"Two queens stand before me. For tonight Ive asked you to prepare a lip sync '
          f'performance of {event_nested_list[event_check][0]}. Ladies...\n the time has come....'
          f'\n for you to lip sync\nFOR\nYOUR\nLEGACY.')
    return check_lip_sync(event_nested_list[event_check + 1])


@perform_lip_sync
def check_lip_sync(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    """
    lip_sync = perform_lip_sync(*args, **kwargs)

    if lip_sync[0] == 'Believe by Cher':
        print(f'The music starts and you need to remember the first line of the song, which do you lip sync?')
        for pair in list(enumerate(lip_sync[1])):
            print(f'{pair[0]}: {pair[1]}')
            if input() == 0:
                print("You flawlessly mouth along to the first words of the song, giving you a boost in confidence.")
            else:
                print(f"You fumble the first few words and your opponent performs an effortless reveal, leaving you"
                      f"shaken")
        print(f'You make it to the chorus and you know you have to start it off right, which do you lip sync?')
        for pair in list(enumerate(lipsync[2])):
            print(f'{pair[0]}: {pair[1]}')
            if input() == 2:
                print("You start the chorus perfectly, giving it the energy required to sell it to the judges.")
            else:
                print(f"You trip on a loose stage screw and it throws you off, and it takes you a few seconds to"
                      f"figure out where you are in the song now.")
        print(f"It's the last verse before the closing chorus, you're so close and you know you have to end strong."
              f"Which do you lip sync?
        for pair in list(enumerate(lipsync[3])):
            print(f"{pair[0]}: {pair[1]}")
            if input() == 1:
                print("You end the performance with a bang! The judges cheer and clap and you know you've done well.")
            else:
                print(f"You end on a sour note, while you gave it everything you had you're worried the minor mistakes"
                      f"you made have seriously affected your chances.")



def runway_events(position, character_dictionary):
    """

    :param position:
    :param character_dictionary:
    :return:
    """


def main(character_dictionary: dict):
    """

    :param character_dictionary:
    """
    if character_dictionary.get('level') == 3:
        judge_events()
    elif character_dictionary.get('level') == 2:
        runway_events()
    else:
        werkroom_events()


if __name__ == '__main__':
    main()
