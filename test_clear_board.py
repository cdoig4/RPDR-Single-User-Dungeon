"""
Colin Doig A01334230
Kelly Hagg A01324804
"""

from unittest import TestCase
from unittest.mock import patch
from boards import clear_board


class TestClearBoard(TestCase):
    def test_clear_board(self, _):
        expected = []
        actual = []
        self.assertEqual(expected, actual)
