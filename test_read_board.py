"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from unittest.mock import patch
from boards import read_board


class TestReadBoard(TestCase):
    def test_read_board_werk_room(self):
        expected = '     #   #   #   #   #   #   #   #   #\n' \
                   '     x   x   x   x |[E]| x   x   x   x   $\n' \
                   '    ---------------     ---------------\n' \
                   '   | !   !   !   !   !   !   !   !   ! | $\n' \
                   '   |                                   |\n' \
                   '   | !   !   !   !   !   Q   !   !   ! | $\n' \
                   '   |                                   |\n' \
                   '   | !   Q   !   !   !   !   !   !   ! | $\n' \
                   '   |                                   |\n' \
                   '   | !   !   !   !   !   !   !   Q   ! | $\n' \
                   '   |                                   |\n' \
                   '   | !   !   !   Q   !   !   !   !   ! | $\n' \
                   '    ---------------     ---------------\n' \
                   '     x   x   x   x |[e]| x   x   x   x   $\n'
        self.assertEqual(expected, read_board('werk_room'))

    def test_read_board_main_stage(self):
        expected = '    #   #   #   #   #   #   #   #   #   #\n' \
                   '    x   x   x   x   x |[E]| x   x   x   x   $\n' \
                   '                   ---     ---\n' \
                   '    x   x   x   x | !   !   ! | x   x   x   $\n' \
                   '                  |           |\n' \
                   '    x   x   x   x | !   !   ! | x   x   x   $\n' \
                   '                  |           |\n' \
                   '    x   x   x   x | !   !   ! | x   x   x   $\n' \
                   '                  |           |\n' \
                   '    x   x   x   x | !   !   ! | x   x   x   $\n' \
                   '       -----------             -----------\n' \
                   '    x | !   !   !   !   !   !   !   !   ! | $\n' \
                   '   ---                                    |\n' \
                   '   <e.  !   Q   !   !   !   !   !   X   ! | $\n' \
                   '   ---                                    |\n' \
                   '    x | !   !   !   !   !   !   !   !   ! | $\n' \
                   '       -----------------------------------\n'
        self.assertEqual(expected, read_board('main_stage'))

    def test_read_board_judges_panel(self):
        expected = '    #   #   #   #   #   #   #\n' \
                   '    x   x   x   x   x   x   x  $\n' \
                   '       -----------------------\n' \
                   '    x | !   !   !   !   !  .E> $\n' \
                   '   ---                     ---\n' \
                   '   [e]  !   !   !   !   ! | x  $\n' \
                   '   -----------------------\n' \
                   '            _________\n' \
                   '           [_________]\n' \
                   '             J  J  J\n'
        self.assertEqual(expected, read_board('judges_panel'))

    # def test_read_board_dressing_room(self):
    #     expected = ''
    #     self.assertEqual(expected, read_board('dressing_room'))