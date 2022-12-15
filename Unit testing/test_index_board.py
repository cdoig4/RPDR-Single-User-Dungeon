from unittest import TestCase
from boards import index_board


class TestIndexBoard(TestCase):
    def test_index_board_judges_panel(self):
        expected = {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False,
                    (0, 5): False, (0, 6): False, (1, 0): False, (1, 1): True, (1, 2): True,
                    (1, 3): True, (1, 4): True, (1, 5): True, (1, 6): 'exit', (2, 0): 'enter',
                    (2, 1): True, (2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True,
                    (2, 6): False}

        self.assertEqual(expected, index_board('judges_panel'))

    def test_index_board_dressing_room(self):
        expected = {(0, 0): True, (0, 1): True, (0, 2): True, (0, 3): True, (0, 4): True,
                    (0, 5): False, (1, 0): True, (1, 1): 'queen', (1, 2): True, (1, 3): True,
                    (1, 4): True, (1, 5): 'exit', (2, 0): True, (2, 1): True, (2, 2): True,
                    (2, 3): True, (2, 4): True, (2, 5): False}

        self.assertEqual(expected, index_board('dressing_room'))

    def test_index_board_werk_room(self):
        expected = {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): 'exit',
                    (0, 5): False, (0, 6): False, (0, 7): False, (0, 8): False, (1, 0): True,
                    (1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (1, 5): True,
                    (1, 6): True, (1, 7): True, (1, 8): True, (2, 0): True, (2, 1): True,
                    (2, 2): True, (2, 3): True, (2, 4): True, (2, 5): 'queen', (2, 6): True,
                    (2, 7): True, (2, 8): True, (3, 0): True, (3, 1): 'queen', (3, 2): True,
                    (3, 3): True, (3, 4): True, (3, 5): True, (3, 6): True, (3, 7): True,
                    (3, 8): True, (4, 0): True, (4, 1): True, (4, 2): True, (4, 3): True,
                    (4, 4): True, (4, 5): True, (4, 6): True, (4, 7): 'queen', (4, 8): True,
                    (5, 0): True, (5, 1): True, (5, 2): True, (5, 3): 'queen', (5, 4): True,
                    (5, 5): True, (5, 6): True, (5, 7): True, (5, 8): True, (6, 0): False,
                    (6, 1): False, (6, 2): False, (6, 3): False, (6, 4): 'enter', (6, 5): False,
                    (6, 6): False, (6, 7): False, (6, 8): False}
        self.assertEqual(expected, index_board('werk_room'))

    def test_index_board_main_stage(self):
        expected = {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False,
                    (0, 5): 'exit', (0, 6): False, (0, 7): False, (0, 8): False, (0, 9): False,
                    (1, 0): False, (1, 1): False, (1, 2): False, (1, 3): False, (1, 4): True,
                    (1, 5): True, (1, 6): True, (1, 7): False, (1, 8): False, (1, 9): False,
                    (2, 0): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): True,
                    (2, 5): True, (2, 6): True, (2, 7): False, (2, 8): False, (2, 9): False,
                    (3, 0): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): True,
                    (3, 5): True, (3, 6): True, (3, 7): False, (3, 8): False, (3, 9): False,
                    (4, 0): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): True,
                    (4, 5): True, (4, 6): True, (4, 7): False, (4, 8): False, (4, 9): False,
                    (5, 0): False, (5, 1): True, (5, 2): True, (5, 3): True, (5, 4): True,
                    (5, 5): True, (5, 6): True, (5, 7): True, (5, 8): True, (5, 9): True,
                    (6, 0): 'enter', (6, 1): True, (6, 2): 'queen', (6, 3): True, (6, 4): True,
                    (6, 5): True, (6, 6): True, (6, 7): True, (6, 8): True, (6, 9): True,
                    (7, 0): False, (7, 1): True, (7, 2): True, (7, 3): True, (7, 4): True,
                    (7, 5): True, (7, 6): True, (7, 7): True, (7, 8): True, (7, 9): True}
        self.assertEqual(expected, index_board('main_stage'))
