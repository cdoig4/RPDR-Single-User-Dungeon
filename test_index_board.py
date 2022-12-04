"""
Colin Doig A01334230
Kelly Hagg A01324804
"""

from unittest import TestCase
from unittest.mock import patch
from boards import index_board


class TestIndexBoard(TestCase):
    def test_index_board(self, _):
        expected = [0]
        actual = []
        self.assertEqual(expected, actual)
