🔴🌈
import unittest
from fibonacci import fib

class TestFib(unittest.TestCase):

    def test_fib(self):
        """
        Test fibonacci sequence
        """
        result = fib(5)
        self.assertEqual(result, [0, 1, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()
