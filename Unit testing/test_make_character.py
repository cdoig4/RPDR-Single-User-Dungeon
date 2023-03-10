from unittest import TestCase
from unittest.mock import patch
from character_setup import make_character


class TestMakeCharacter(TestCase):
    @patch('challenges.get_challenge_input_from_user', return_value='look_queen')
    def test_make_character_look_queen(self, _):
        expected = {'Charisma': 14, 'Uniqueness': 15, 'Nerve': 10, 'Talent': 10,
                    'met_rupaul': False, 'completed_lip_sync': False, 'level': 1,
                    'Name': 'Ginger Snaps', 'achieved_goal': False, 'location': 'werk_room',
                    'coordinates': (0, 4)}
        actual = make_character('Ginger Snaps')
        self.assertEqual(expected, actual)

    @patch('challenges.get_challenge_input_from_user', return_value='comedy_queen')
    def test_make_character_comedy_queen(self, _):
        expected = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10,
                    'met_rupaul': False, 'completed_lip_sync': False, 'level': 1,
                    'Name': 'Ginger Snaps', 'achieved_goal': False, 'location': 'werk_room',
                    'coordinates': (0, 4)}
        actual = make_character('Ginger Snaps')
        self.assertEqual(expected, actual)

    @patch('challenges.get_challenge_input_from_user', return_value='performance_queen')
    def test_make_character_performance_queen(self, _):
        expected = {'Charisma': 17, 'Uniqueness': 12, 'Nerve': 10, 'Talent': 10,
                    'met_rupaul': False, 'completed_lip_sync': False, 'level': 1,
                    'Name': 'Ginger Snaps', 'achieved_goal': False, 'location': 'werk_room',
                    'coordinates': (0, 4)}
        actual = make_character('Ginger Snaps')
        self.assertEqual(expected, actual)

    @patch('challenges.get_challenge_input_from_user', return_value='alternative_queen')
    def test_make_character_alternative_queen(self, _):
        expected = {'Charisma': 12, 'Uniqueness': 17, 'Nerve': 10, 'Talent': 10,
                    'met_rupaul': False, 'completed_lip_sync': False, 'level': 1,
                    'Name': 'Ginger Snaps', 'achieved_goal': False, 'location': 'werk_room',
                    'coordinates': (0, 4)}
        actual = make_character('Ginger Snaps')
        self.assertEqual(expected, actual)

    @patch('challenges.get_challenge_input_from_user', return_value='look_queen')
    def test_make_character_lowercase_name(self, _):
        expected = {'Charisma': 14, 'Uniqueness': 15, 'Nerve': 10, 'Talent': 10,
                    'met_rupaul': False, 'completed_lip_sync': False, 'level': 1,
                    'Name': 'ginger snaps', 'achieved_goal': False, 'location': 'werk_room',
                    'coordinates': (0, 4)}
        actual = make_character('ginger snaps')
        self.assertEqual(expected, actual)

    @patch('challenges.get_challenge_input_from_user', return_value='look_queen')
    def test_make_character_uppercase_name(self, _):
        expected = {'Charisma': 14, 'Uniqueness': 15, 'Nerve': 10, 'Talent': 10,
                    'met_rupaul': False, 'completed_lip_sync': False, 'level': 1,
                    'Name': 'GINGER SNAPS', 'achieved_goal': False, 'location': 'werk_room',
                    'coordinates': (0, 4)}
        actual = make_character('GINGER SNAPS')
        self.assertEqual(expected, actual)

    @patch('challenges.get_challenge_input_from_user', return_value='look_queen')
    def test_make_character_numbers_and_punctuation_in_name(self, _):
        expected = {'Charisma': 14, 'Uniqueness': 15, 'Nerve': 10, 'Talent': 10,
                    'met_rupaul': False, 'completed_lip_sync': False, 'level': 1,
                    'Name': '$@$G1Ng3r 2N^PS!#$#', 'achieved_goal': False, 'location': 'werk_room',
                    'coordinates': (0, 4)}
        actual = make_character('$@$G1Ng3r 2N^PS!#$#')
        self.assertEqual(expected, actual)
