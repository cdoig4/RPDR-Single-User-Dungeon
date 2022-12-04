"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


import io
from unittest import TestCase
from unittest.mock import patch
from boards import display_board


class TestDisplayBoard(TestCase):
    @patch('boards.format_board', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_werk_room(self, mock_output, formatted_board):
        display_board({'location': 'werk_room', 'coordinates': (0, 0)})
        printed = mock_output.getvalue()
        expected = '----------------------------------------------------------------------' \
                   '----------\nYou are currently in the Drag Race Werk Room. There are mirrors' \
                   ' along the side\nof the room, a fabric wall covered in rolls of fabric, and ' \
                   'several tables with\nsewing machines.\n\n'
        self.assertEqual(expected, printed)

    @patch('boards.format_board', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_main_stage(self, mock_output, formatted_board):
        display_board({'location': 'main_stage', 'coordinates': (0, 0)})
        printed = mock_output.getvalue()
        expected = '---------------------------------------------------------------------' \
                   '-----------\nYou are currently on the main stage. As you walk along the' \
                   ' runway, the lights\nshine and flash. The anticipation hangs heavy in the' \
                   ' air.\n\n'
        self.assertEqual(expected, printed)

    @patch('boards.format_board', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_judges_panel(self, mock_output, formatted_board):
        display_board({'location': 'judges_panel', 'coordinates': (0, 0)})
        printed = mock_output.getvalue()
        expected = '----------------------------------------------------------------------' \
                   '----------\nYou can see the judges looking down on you as you make your way ' \
                   'towards\nRuPaul\'s Dressing Room. With every step it feels like one of them ' \
                   'might open\ntheir mouth to say something.\n\n'
        self.assertEqual(expected, printed)

    @patch('boards.format_board', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_dressing_room(self, mock_output, formatted_board):
        display_board({'location': 'dressing_room', 'coordinates': (0, 0)})
        printed = mock_output.getvalue()
        expected = '----------------------------------------------------------------------' \
                   '----------\nYou see Mother herself standing in the centre of the room, ' \
                   'posing imperiously\nas her eyes watch you like a hawk.\n\n'
        self.assertEqual(expected, printed)
