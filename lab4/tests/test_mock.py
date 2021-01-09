import unittest
# from mock import Mock
from unittest.mock import patch
import io
# from github.lab4.chain_of_responsibility import *
from chain_of_responsibility import *


class TestFoundation(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foo_one(self, mock_stdout):
        CakeChain().chain1.handle(6)
        assert mock_stdout.getvalue() == 'Больших тортов весом 5 кг -- 1\nМаленьких тортов весом 1 кг -- 1\n'

    def test_foo_two(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            CakeChain().chain1.handle(5)

        assert fake_stdout.getvalue() == 'Больших тортов весом 5 кг -- 1\n'


if __name__ == '__main__':
    unittest.main()
