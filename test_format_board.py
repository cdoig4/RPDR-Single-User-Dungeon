"""
Colin Doig A01334230
Kelly Hagg A01324804
"""

from unittest import TestCase
from unittest.mock import patch
from boards import format_board


class TestFormatBoard(TestCase):
    def test_format_board(self, _):
        expected = []
        actual = []
        self.assertEqual(expected, actual)
