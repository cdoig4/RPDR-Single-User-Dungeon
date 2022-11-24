import itertools

def generate_directional_tools():

    pairs = []

    input_letters = ['W', 'S', 'A', 'D']
    directions = ['Up', 'Down', 'Left', 'Right']

    for pair in zip(input_letters, directions):
        pairs.append(pair)
    return pairs

def generate_game_input(answers: list):
    """
    """
    answers = ['a1', 'a2', 'a3', 'a4']

    for number, answer in enumerate(answers, 1):

        print(number, answer)


def main():
    """
    Drive the program
    """
    print(generate_directional_tools())

if __name__ == '__main__':
    main()