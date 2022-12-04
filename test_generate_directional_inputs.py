"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from controls import generate_directional_inputs


class TestGenerateDirectionalInputs(TestCase):
    def test_generate_directional_entry_on_left(self):
        expected = [('E', 'Enter'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 0), 'judges_panel')
        self.assertEqual(expected, actual)

    def test_generate_directional_entry_at_bottom(self):
        expected = [('E', 'Enter'), ('W', 'Up'), ('0', 'Stats')]
        actual = generate_directional_inputs((6, 4), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_exit_at_top(self):
        expected = [('X', 'Exit'), ('S', 'Down'), ('0', 'Stats')]
        actual = generate_directional_inputs((0, 5), 'main_stage')
        self.assertEqual(expected, actual)

    def test_generate_directional_exit_on_right(self):
        expected = [('X', 'Exit'), ('A', 'Left'), ('0', 'Stats')]
        actual = generate_directional_inputs((1, 5), 'dressing_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_middle(self):
        expected = [('W', 'Up'), ('S', 'Down'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 5), 'main_stage')
        self.assertEqual(expected, actual)

    def test_generate_directional_stage_X(self):
        expected = [('W', 'Up'), ('S', 'Down'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((6, 8), 'main_stage')
        self.assertEqual(expected, actual)

    def test_generate_directional_left_wall(self):
        expected = [('W', 'Up'), ('S', 'Down'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 0), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_right_wall(self):
        expected = [('W', 'Up'), ('S', 'Down'), ('A', 'Left'), ('0', 'Stats')]
        actual = generate_directional_inputs((3, 6), 'main_stage')
        self.assertEqual(expected, actual)

    def test_generate_directional_top_wall(self):
        expected = [('S', 'Down'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((1, 3), 'judges_panel')
        self.assertEqual(expected, actual)

    def test_generate_directional_bottom_wall(self):
        expected = [('W', 'Up'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((5, 5), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_top_left_corner(self):
        expected = [('S', 'Down'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((1, 4), 'main_stage')
        self.assertEqual(expected, actual)

    def test_generate_directional_top_right_corner(self):
        expected = [('S', 'Down'), ('A', 'Left'), ('0', 'Stats')]
        actual = generate_directional_inputs((1, 8), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_bottom_left_corner(self):
        expected = [('W', 'Up'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 0), 'dressing_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_bottom_right_corner(self):
        expected = [('W', 'Up'), ('A', 'Left'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 5), 'judges_panel')
        self.assertEqual(expected, actual)

    def test_generate_directional_queen_on_right(self):
        expected = [('Q', 'Challenge her'), ('W', 'Up'), ('S', 'Down'), ('A', 'Left'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 4), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_queen_on_left(self):
        expected = [('Q', 'Challenge her'), ('W', 'Up'), ('S', 'Down'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((3, 2), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_queen_above(self):
        expected = [('Q', 'Challenge her'), ('S', 'Down'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((3, 5), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_queen_below(self):
        expected = [('Q', 'Challenge her'), ('W', 'Up'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 1), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_left_wall_queen_on_right(self):
        expected = [('Q', 'Challenge her'), ('W', 'Up'), ('S', 'Down'), ('0', 'Stats')]
        actual = generate_directional_inputs((3, 0), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_right_wall_queen_on_left(self):
        expected = [('Q', 'Challenge her'), ('W', 'Up'), ('S', 'Down'), ('0', 'Stats')]
        actual = generate_directional_inputs((4, 8), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_top_wall_queen_below(self):
        expected = [('Q', 'Challenge her'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((1, 5), 'werk_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_bottom_wall_queen_above(self):
        expected = [('Q', 'Challenge her'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((7, 2), 'main_stage')
        self.assertEqual(expected, actual)

    def test_generate_directional_top_wall_rupaul_below(self):
        expected = [('Q', 'Challenge her'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((0, 1), 'dressing_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_bottom_wall_rupaul_above(self):
        expected = [('Q', 'Challenge her'), ('A', 'Left'), ('D', 'Right'), ('0', 'Stats')]
        actual = generate_directional_inputs((2, 1), 'dressing_room')
        self.assertEqual(expected, actual)

    def test_generate_directional_left_wall_rupaul_on_right(self):
        expected = [('Q', 'Challenge her'), ('W', 'Up'), ('S', 'Down'), ('0', 'Stats')]
        actual = generate_directional_inputs((1, 0), 'dressing_room')
        self.assertEqual(expected, actual)