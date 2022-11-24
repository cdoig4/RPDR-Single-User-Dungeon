"""
Create the player character and give them the introduction
"""
LOOK_QUEEN = {"Charisma": 14, "Uniqueness": 15, "Nerve": 10, "Talent": 10}
COMEDY_QUEEN = {"Charisma": 15, "Uniqueness": 14, "Nerve": 10, "Talent": 10}
PERFORMANCE_QUEEN = {"Charisma": 17, "Uniqueness": 12, "Nerve": 10, "Talent": 10}
ALTERNATIVE_QUEEN = {'Charisma': 12, 'Uniqueness': 17, 'Nerve': 10, 'Talent': 10}
CHARACTER_CLASSES = ['Look Queen', 'Comedy Queen', 'Performance Queen', 'Alternative Queen']


def make_character(character_name):
    """

    :param character_name:
    :return:
    """
    print("What type of queen are you?")
    for pair in list(enumerate(CHARACTER_CLASSES)):
        print(f'{pair[0]}: {pair[1]}')

    answer = int(input())
    if answer == 0:
        character = {key: value for key, value in LOOK_QUEEN.items()}
    elif answer == 1:
        character = {key: value for key, value in COMEDY_QUEEN.items()}
    elif answer == 2:
        character = {key: value for key, value in PERFORMANCE_QUEEN.items()}
    else:
        character = {key: value for key, value in ALTERNATIVE_QUEEN.items()}
    character['Name'] = character_name
    return character
