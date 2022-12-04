"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from challenges import generate_challenge_input


class TestGenerateChallengeInput(TestCase):
    def test_empty_list(self):
        self.assertEqual([], generate_challenge_input([]))

    def test_list_length_one_empty_string(self):
        self.assertEqual([('1', '')], generate_challenge_input(['']))

    def test_list_length_one_non_empty_string(self):
        self.assertEqual([('1', 'string_for_test')], generate_challenge_input(['string_for_test']))

    def test_list_larger_list_all_empty_strings(self):
        self.assertEqual([('1', ''), ('2', ''), ('3', '')], generate_challenge_input(['', '', '']))

    def test_list_larger_all_non_empty_strings(self):
        self.assertEqual([('1', '1, 2, 3, Repeat after me!'), ('2', 'Say what you want to say'), ('3', 'Hello')],
                         generate_challenge_input(['1, 2, 3, Repeat after me!', 'Say what you want to say', 'Hello']))

    def test_list_larger_mix_empty_and_non_empty_strings(self):
        self.assertEqual([('1', 'Say what you want to say'), ('2', ''), ('3', '1, 2, 3, Repeat after me!')],
                         generate_challenge_input(['Say what you want to say', '', '1, 2, 3, Repeat after me!']))
