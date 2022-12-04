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
