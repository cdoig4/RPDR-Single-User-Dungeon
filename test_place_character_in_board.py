"""
Colin Doig A01334230
Kelly Hagg A01324804
"""

from unittest import TestCase
from unittest.mock import patch
from boards import place_character_in_board


class TestPlaceCharacterInBoard(TestCase):
    def test_place_character_in_board(self, _):
        expected = [0]
        actual = []
        self.assertEqual(expected, actual)
