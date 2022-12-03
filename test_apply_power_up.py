from unittest import TestCase
from character_setup import apply_power_up


class TestApplyPowerUp(TestCase):
    def test_empty_tuple(self):
        self.assertEqual(None, apply_power_up((), 0))

    def test_tuple_single_element(self):
        self.assertEqual(None, apply_power_up(('test_string',), 0))

    def test_tuple_first_element_empty_string_second_element_plus_value_less_than_zero(self):
        self.assertEqual({'': 0}, apply_power_up(('', 110), -145))

    def test_tuple_first_element_empty_string_second_element_plus_value_equals_zero(self):
        self.assertEqual({'': 0}, apply_power_up(('', -45), 45))

    def test_tuple_first_element_empty_string_second_element_plus_value_greater_than_zero(self):
        self.assertEqual({'': 200}, apply_power_up(('', 135), 65))

    def test_tuple_first_element_non_empty_string_second_element_plus_value_less_than_zero(self):
        self.assertEqual({'test_string': 0}, apply_power_up(('test_string', 4), -10))

    def test_tuple_first_element_non_empty_string_second_element_plus_value_equals_zero(self):
        self.assertEqual({'test_string': 0}, apply_power_up(('test_string', 4), -4))

    def test_tuple_first_element_non_empty_string_second_element_plus_value_greater_than_zero(self):
        self.assertEqual({'test_string': 16}, apply_power_up(('test_string', 8), 8))
