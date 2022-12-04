"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from controls import get_directional_input_from_user


class MyGenerateDirectionalInputs(TestCase):
    def test_generate_directional_entry_on_left(self):
        expected = [('E', 'Enter'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 0), 'judges_panel')
        self.assertEqual(expected, actual)