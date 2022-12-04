"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from unittest.mock import patch
from boards import set_board


class TestSetBoard(TestCase):
    def test_set_board(self, _):
        expected = []
        actual = []
        self.assertEqual(expected, actual)
