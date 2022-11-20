import unittest
from fib_num import fib_nums
from types import GeneratorType

class TestCases(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.f = list(fib_nums(10))
        super().__init__(methodName)

    def test_first_number(self):
        self.assertEqual(0, self.f[0])
    def test_second_number(self):
        self.assertEqual(1, self.f[1])
    def test_third_number(self):
        self.assertEqual(1, self.f[2])
    def test_forth_number(self):
        self.assertEqual(2, self.f[3])
    def test_if_lazy(self):
        self.assertIsInstance(fib_nums(1), GeneratorType)

if __name__ == '__main__':
    unittest.main()