"""
Challenges for the user to help them increase their level!
"""
import random

CHER_LIP_SYNC = ['Believe by Cher', 'No matter how hard I try, you keep pushing me aside',
                 'Do you believe in life after love?',
                 "Well I know that I'll get through this, Cause I know that I am strong"]
MADONNA_LIP_SYNC = ['Vogue by Madonna', 'When all else fails and you long to be Something better than you are today',
                    'Come on, vogue. Let your body move to the music',
                    "Magical, life's a ball So get up on the dance floor"]
CARLY_RAE_JEPSEN_LIP_SYNC = ['Runaway With Me by Carly Rae Jepsen',
                             "You're stuck in my head, stuck in my heart, stuck in my body- body",
                             'When the lights go out, Run away with me! Run away with me!',
                             'Over the weekend, we could turn the world to gold']
RUNWAY_EVENTS = [CHER_LIP_SYNC, MADONNA_LIP_SYNC, CARLY_RAE_JEPSEN_LIP_SYNC]
MICHELLE_EVENT = f'Michelle glares at you and says:\n"That dress is hideous. Where did you get it, Party City?"'
CARSON_EVENT = f'Carson claps his hands and says:\n"Oh I just loved your lip syncs, they were so fabulous!"'
ROSS_EVENT = f'Ross shouts:\n"Your pussy is on fire! Go get your crown, girl!"'


def judge_events(movement, character_dictionary):
    """


    :param movement:
    :param character_dictionary:
    :return:
    """
    if movement:
        event_check = random.randint(1, 20)
        if event_check == 1:
            print(MICHELLE_EVENT)
            character_dictionary['Charisma'] -= 5
        elif event_check == 7:
            print(ROSS_EVENT)
            character_dictionary['Uniqueness'] += 4
        elif event_check == 14:
            print(CARSON_EVENT)
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
    check_lip_sync(event_nested_list[event_check])
    return


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
