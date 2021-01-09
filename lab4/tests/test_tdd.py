import unittest
import sys
import os
# from github.lab4.builder import *
from builder import *


sys.path.append(os.getcwd())


class TestFoundation(unittest.TestCase):
    def test_yogurt_cake_returns_string(self):
        self.assertEqual('{}'.format(YogurtDirector.construct()),
                         'Это бисквитный торт в форме овала с йогуртовой начинкой и 3 ярусами.')

    def test_strawberry_cake_returns_string(self):
        self.assertEqual('{}'.format(StrawberryDirector.construct()),
                         'Это бисквитный торт в форме сердца с клубничной начинкой и 1 ярусами.')

    def test_chocolate_cake_returns_string(self):
        self.assertEqual('{}'.format(ChocolateDirector.construct()),
                         'Это шоколадный торт в форме квадрата с ореховой начинкой и 1 ярусами.')


if __name__ == '__main__':
    unittest.main()
