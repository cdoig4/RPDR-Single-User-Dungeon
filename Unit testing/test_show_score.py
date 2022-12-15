"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from controls import show_score


class TestShowScore(TestCase):
    def test_stats_all_negative_values(self):
        self.assertEqual(
            None, show_score({'Charisma': -5, 'Uniqueness': -25, 'Nerve': -400, 'Talent': -8}))

    def test_stats_all_zero_values(self):
        self.assertEqual(None,
                         show_score({'Charisma': 0, 'Uniqueness': 0, 'Nerve': 0, 'Talent': 0}))

    def test_stats_all_positive_values(self):
        self.assertEqual(None,
                         show_score({'Charisma': 5, 'Uniqueness': 25, 'Nerve': 400, 'Talent': 8}))

    def test_stats_mix_of_values(self):
        self.assertEqual(None,
                         show_score({'Charisma': -5, 'Uniqueness': -25, 'Nerve': 500, 'Talent': 0}))
