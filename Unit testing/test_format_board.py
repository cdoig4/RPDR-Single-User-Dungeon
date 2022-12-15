from unittest import TestCase
from boards import format_board


class TestFormatBoard(TestCase):
    def test_format_board_character_not_placed(self):
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
                   '   | !   !   !   !   ! | x  $\n' \
                   '   |                    ---\n' \
                   '   | !   R   !   !   !  [E] $\n' \
                   '   |                    ---\n' \
                   '   | !   !   !   !   ! | x  $\n' \
                   '    -------------------\n'
        self.assertEqual(expected, format_board(board, {'location': 'dressing_room'}))

    def test_format_board_character_placed(self):
        board = '     #   #   #   #   #   #\n' \
                   '    -------------------\n' \
                   '   |                   |    $\n' \
                   '   |                    ---\n' \
                   '   | &   x   x   x   x  [x] $\n' \
                   '   |                    ---\n' \
                   '   | x   x   x   x   x | x  $\n' \
                   '    -------------------\n'
        expected = '     #   #   #   #   #   #\n' \
                   '    -------------------\n' \
                   '   |                   |    $\n' \
                   '   |                    ---\n' \
                   '   | &   R   x   x   x  [x] $\n' \
                   '   |                    ---\n' \
                   '   | x   x   x   x   x | x  $\n' \
                   '    -------------------\n'
        self.assertEqual(expected, format_board(board, {'location': 'dressing_room'}))

    def test_format_board_cleared_board(self):
        board = '                          \n' \
                   '    -------------------\n' \
                   '   |                   | x  $\n' \
                   '   |                    ---\n' \
                   '   |                    [ ] $\n' \
                   '   |                    ---\n' \
                   '   |                   |    $\n' \
                   '    -------------------\n'
        expected = '                          \n' \
                   '    -------------------\n' \
                   '   |                   | x  $\n' \
                   '   |                    ---\n' \
                   '   |     R              [ ] $\n' \
                   '   |                    ---\n' \
                   '   |                   |    $\n' \
                   '    -------------------\n'
        self.assertEqual(expected, format_board(board, {'location': 'dressing_room'}))

    def test_format_board_incorrect_location(self):
        board = '                          \n' \
                   '    -------------------\n' \
                   '   |                   | x  $\n' \
                   '   |                    ---\n' \
                   '   |                    [ ] $\n' \
                   '   |                    ---\n' \
                   '   |                   |    $\n' \
                   '    -------------------\n'
        expected = '                          \n' \
                   '    -------------------\n' \
                   '   |                   | x  $\n' \
                   '   |                    ---\n' \
                   '   |                    [ ] $\n' \
                   '   |                    ---\n' \
                   '   |                   |    $\n' \
                   '    -------------------\n'
        self.assertEqual(expected, format_board(board, {'location': 'brazil'}))

    def test_format_board_judges_panel(self):
        expected = '    #   #   #   #   #   #   #\n' \
                   '                               $\n' \
                   '       -----------------------\n' \
                   '      |         &   !   !  .E> $\n' \
                   '   ---                     ---\n' \
                   '   [e]  !   !   !   !   ! | x  $\n' \
                   '   -----------------------\n' \
                   '            _________\n' \
                   '           [_________]\n' \
                   '             J  J  J\n'
        self.assertEqual(expected, format_board(expected, {'location': 'judges_panel'}))

    def test_format_board_main_stage(self):
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
                   '   <e.  !       !   !   !   !   !       ! | $\n' \
                   '   ---                                    |\n' \
                   '    x | !   !   !   !   !   !   !   !   ! | $\n' \
                   '       -----------------------------------\n'
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
        self.assertEqual(expected, format_board(board, {'location': 'main_stage'}))

    def test_format_board_werk_room(self):
        board = '     #   #   #   #   #   #   #   #   #\n' \
                   '                   |[&]| x   x   x   x   $\n' \
                   '    ---------------     ---------------\n' \
                   '   | !   !   !   !   !   !   !   !   ! | $\n' \
                   '   |                                   |\n' \
                   '   | !   !   !   !   !       !   !   ! | $\n' \
                   '   |                                   |\n' \
                   '   | !       !   !   !   !   !   !   ! | $\n' \
                   '   |                                   |\n' \
                   '   | !   !   !   !   !   !   !       ! | $\n' \
                   '   |                                   |\n' \
                   '   | !   !   !       !   !   !   !   ! | $\n' \
                   '    ---------------     ---------------\n' \
                   '     x   x   x   x |[e]| x   x   x   x   $\n'
        expected = '     #   #   #   #   #   #   #   #   #\n' \
                   '                   |[&]| x   x   x   x   $\n' \
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
        self.assertEqual(expected, format_board(board, {'location': 'werk_room'}))
