"""
Challenges for the user to help them increase their level!
"""
import random

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
