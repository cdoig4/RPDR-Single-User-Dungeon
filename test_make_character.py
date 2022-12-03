"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from unittest.mock import patch
from character_setup import make_character


class TestMakeCharacter(TestCase):
    @patch('challenges.get_challenge_input_from_user', return_value='look_queen')
    def test_look_queen(self, get_challenge_input_from_user):
        expected = {'Charisma': 14, 'Uniqueness': 15, 'Nerve': 10, 'Talent': 10,
                    'met_rupaul': False, 'completed_lip_sync': False, 'level': 1,
                    'Name': 'Ginger Snaps'}
        actual = make_character('Ginger Snaps')
        self.assertEqual(expected, actual)



