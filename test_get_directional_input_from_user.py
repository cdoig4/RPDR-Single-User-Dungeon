"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from unittest.mock import patch
from controls import get_directional_input_from_user


class TestGetDirectionalInputFromUser(TestCase):
    @patch('builtins.input', return_value='W')
    def test_get_directional_input_from_user_W(self, _):
        game_input = [('W', 'Up'), ('S', 'Down'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = get_directional_input_from_user(game_input, {})
        self.assertEqual('up', actual)

    @patch('builtins.input', return_value='A')
    def test_get_directional_input_from_user_A(self, _):
        game_input = [('W', 'Up'), ('S', 'Down'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = get_directional_input_from_user(game_input, {})
        self.assertEqual('left', actual)

    @patch('builtins.input', return_value='S')
    def test_get_directional_input_from_user_S(self, _):
        game_input = [('W', 'Up'), ('S', 'Down'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = get_directional_input_from_user(game_input, {})
        self.assertEqual('down', actual)

    @patch('builtins.input', return_value='D')
    def test_get_directional_input_from_user_D(self, _):
        game_input = [('W', 'Up'), ('S', 'Down'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = get_directional_input_from_user(game_input, {})
        self.assertEqual('right', actual)

    """
    Cannot test further yet (recursive function calls).
    """