class Character:
    """
    A class representing the character.
    """

    id_counter = 0

    def __init__(self, name, charisma, uniqueness, nerve, talent, location, coordinates):
        if name == '':
            raise ValueError("Character name cannot be empty.")
        else:
            self.name = name

        self.charisma = 10
        self.uniqueness = 10
        self.nerve = 10
        self.talent = 10
        self.location = 'werk_room'
        self.coordinates = (0, 4)

        self.id = Character.id_counter
        Character.id_counter += 1


def main():
    pass


if __name__ == '__main__':
    main()
