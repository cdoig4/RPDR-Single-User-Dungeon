import itertools
import json
import random
from challenges import get_challenge_input_from_user

makeup_question = ['Contouring', 'Foundation', 'Eye shadow']

lips_question = ['Lipstick', 'Lip Gloss', 'Lip Liner']

outfit_question = ['Gown', 'Shoes', 'Wig']


def makeover_challenge(character):
    """

    :param character:
    """
    filename = './json_files/queens.json'
    with open(filename) as file_object:
        queens = json.load(file_object)
    queen_names = list(queens.keys())
    fellow_queen = random.choice(queen_names)
    first_options = list(itertools.permutations(makeup_question))
    second_options = list(itertools.permutations(lips_question))
    final_options = list(itertools.permutations(outfit_question))
    correct_answers = 0

    print(f"You hear RuPaul's voice: \"My queens! You have 10 minutes to put one of your fellow queens into the best "
          f"quick drag you can manage. Get to it!\n{queens[fellow_queen]['Name']} approaches you, ready to have her "
          f"face beat for the gods.\n You know that to get the best results you have to put the makeup on in the right"
          f" order.\nWhat order do you apply makeup in?")
    first_answer = get_challenge_input_from_user(first_options)
    if first_answer == ['Foundation', 'Eye shadow', 'Contouring']:
        correct_answers += 1
        print(f"You take a step back to admire your work. {queens[fellow_queen]['Name']} is looking fierce!")
    else:
        print(f"You take a step back to examine {queens[fellow_queen]['Name']}'s face. It's looking a little busted.")
    print(f"Next you have to do the lips. What order do you apply makeup in?")
    second_answer = get_challenge_input_from_user(second_options)
    if second_answer == ['Lip Liner', 'Lipstick', 'Lip Gloss']:
        correct_answers += 1
        print(f"{queens[fellow_queen]['Name']}'s lips are looking luscious and divine! Way to go!")
    else:
        print(f"{queens[fellow_queen]['Name']}'s lips are looking a little crusty and dusty, but you don't have time to"
              f" fix them right now.")
    print(f"You hear a call for one minute left and you rush to get {queens[fellow_queen]['Name']} into an outfit!\n"
          f"What order do you dress her in?")
    final_answer = get_challenge_input_from_user(final_options)
    if final_answer == ['Gown', 'Shoes', 'Wig']:
        correct_answers += 1
        print(f"You finish dressing {queens[fellow_queen]['Name']} and the outfit looks stunning on her!")
    else:
        print(f"You finish dressing {queens[fellow_queen]['Name']} but her wig is sliding back and she has major"
              f" cliffhangers because the shoes are way too small.")
    print(f"RuPaul walks in wearing a Klein Epstein & Parker suit and examines each pair of queen. She clears"
          f" her throat.")
    if correct_answers > 1:
        print(f"She says: \"{queens[fellow_queen]['Name']}, {character['Name']}, conDRAGulations you are the"
              f" winners of this mini challenge!\n\"")
    else:
        print(f"...and gives the win to another team, who you have to admit do look fucking fierce. You feel "
              f"your confidence wane slightly.")
