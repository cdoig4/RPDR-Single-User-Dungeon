from unittest import TestCase
from boards import clear_board


class TestClearBoard(TestCase):
    def test_clear_board_all_non_permitted_values(self):
        self.assertEqual('            ', clear_board('##!!xx$$EEee'))

    def test_clear_board_mix_permitted_non_permitted_values(self):
        self.assertEqual('    ?    H llo   ~~   ||', clear_board('#  #?!!xxHello$$E~~Eee||'))

    def test_clear_board_all_permitted_values(self):
        self.assertEqual('0123-|[ ]&QRJX<>.', clear_board('0123-|[ ]&QRJX<>.'))
