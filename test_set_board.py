"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from unittest.mock import patch
from boards import set_board


class TestSetBoard(TestCase):

    def test_set_board_werk_room(self):
        expected = {'completed_lip_sync': False, 'met_rupaul': False, 'level': 1}
        actual = set_board({'completed_lip_sync': False, 'met_rupaul': False, 'level': 1})
        self.assertEqual(expected, actual)

    def test_set_board_main_stage(self):
        expected = {'completed_lip_sync': False, 'met_rupaul': False, 'level': 2,
                    'location': 'main_stage', 'coordinates': (0, 5)}
        actual = set_board({'completed_lip_sync': False, 'met_rupaul': False, 'level': 2})
        self.assertEqual(expected, actual)

    def test_set_board_judges_panel(self):
        expected = {'completed_lip_sync': True, 'met_rupaul': False, 'level': 3,
                    'location': 'judges_panel', 'coordinates': (1, 6)}
        actual = set_board({'completed_lip_sync': True, 'met_rupaul': False, 'level': 3})
        self.assertEqual(expected, actual)

    def test_set_board_judges_panel_level_too_low(self):
        expected = {'completed_lip_sync': True, 'met_rupaul': False, 'level': 1,
                    'location': 'judges_panel', 'coordinates': (1, 6)}
        actual = set_board({'completed_lip_sync': True, 'met_rupaul': False, 'level': 1})
        self.assertEqual(expected, actual)

    def test_set_board_judges_panel_level_too_high(self):
        expected = {'completed_lip_sync': True, 'met_rupaul': False, 'level': 3,
                    'location': 'judges_panel', 'coordinates': (1, 6)}
        actual = set_board({'completed_lip_sync': True, 'met_rupaul': False, 'level': 3})
        self.assertEqual(expected, actual)

    def test_set_board_dressing_room(self):
        expected = {'completed_lip_sync': True, 'met_rupaul': True, 'level': 3,
                    'location': 'dressing_room', 'coordinates': (1, 5)}
        actual = set_board({'completed_lip_sync': True, 'met_rupaul': True, 'level': 3})
        self.assertEqual(expected, actual)

    def test_set_board_dressing_room_level_too_low(self):
        expected = {'completed_lip_sync': True, 'met_rupaul': True, 'level': 1,
                    'location': 'dressing_room', 'coordinates': (1, 5)}
        actual = set_board({'completed_lip_sync': True, 'met_rupaul': True, 'level': 1})
        self.assertEqual(expected, actual)

    def test_set_board_dressing_room_incorrect_lip_sync(self):
        expected = {'completed_lip_sync': False, 'met_rupaul': True, 'level': 3,
                    'location': 'dressing_room', 'coordinates': (1, 5)}
        actual = set_board({'completed_lip_sync': False, 'met_rupaul': True, 'level': 3})
        self.assertEqual(expected, actual)
