"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


from unittest import TestCase
from unittest.mock import patch
from boards import place_character_in_board


class TestPlaceCharacterInBoard(TestCase):
    def test_place_character_in_board_middle(self):
        board = '     #   #   #   #   #   #\n' \
                   '    -------------------\n' \
                   '   | !   !   !   !   ! | x  $\n' \
                   '   |                    ---\n' \
                   '   | !   R   !   !   !  [E] $\n' \
                   '   |                    ---\n' \
                   '   | !   !   !   !   ! | x  $\n' \
                   '    -------------------\n'
        expected = '     #   #   #   #   #   #\n' \
                   '    -------------------\n' \
                   '   |                   |    $\n' \
                   '   |                    ---\n' \
                   '   |             &   x  [x] $\n' \
                   '   |                    ---\n' \
                   '   | x   x   x   x   x | x  $\n' \
                   '    -------------------\n'
        self.assertEqual(expected, place_character_in_board(board, (1, 3)))

    def test_place_character_in_board_exit(self):
        board = '    #   #   #   #   #   #   #   #   #   #\n' \
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
        expected = '    #   #   #   #   #   #   #   #   #   #\n' \
                   '                      |[ ]|                 $\n' \
                   '                   ---     ---\n' \
                   '                  |           |             $\n' \
                   '                  |           |\n' \
                   '                  |           |             $\n' \
                   '                  |           |\n' \
                   '                  |           |             $\n' \
                   '                  |           |\n' \
                   '                  |           |             $\n' \
                   '       -----------             -----------\n' \
                   '      |                                   | $\n' \
                   '   ---                                    |\n' \
                   '   <&.  x   x   x   x   x   x   x   x   x | $\n' \
                   '   ---                                    |\n' \
                   '    x | x   x   x   x   x   x   x   x   x | $\n' \
                   '       -----------------------------------\n'
        self.assertEqual(expected, place_character_in_board(board, (6, 0)))

    def test_place_character_in_board_door_entry(self):
        board = '     #   #   #   #   #   #\n' \
                   '    -------------------\n' \
                   '   | !   !   !   !   ! | x  $\n' \
                   '   |                    ---\n' \
                   '   | !   R   !   !   !  [E] $\n' \
                   '   |                    ---\n' \
                   '   | !   !   !   !   ! | x  $\n' \
                   '    -------------------\n'
        expected = '     #   #   #   #   #   #\n' \
                   '    -------------------\n' \
                   '   |                   |    $\n' \
                   '   |                    ---\n' \
                   '   |                    [&] $\n' \
                   '   |                    ---\n' \
                   '   | x   x   x   x   x | x  $\n' \
                   '    -------------------\n'
        self.assertEqual(expected, place_character_in_board(board, (1, 5)))