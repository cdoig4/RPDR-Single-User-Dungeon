import itertools

def generate_directional_tools():

    pairs = []

    input_letters = ['W', 'S', 'A', 'D']
    directions = ['Up', 'Down', 'Left', 'Right']

    for pair in zip(input_letters, directions):
        pairs.append(pair)
    return pairs

def generate_challenge_input(answers: list):
    """
    """
    pairs = []

    for number, answer in enumerate([answers], 1):
        pair = (number, answer)
        pairs.append(pair)
    return pairs

def main():
    """
    Drive the program
    """
    print(generate_directional_tools())
    print(generate_challenge_input("answer 1, answer 2, answer 3, answer 4"))

if __name__ == '__main__':
    main()