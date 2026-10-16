import unittest

from examples.simple import divide, is_even


class SimpleTests(unittest.TestCase):
    def test_divide_by_zero(self):
        """Деление на ноль вызывает ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_even_odd(self):
        """Чётность числа определяется верно."""
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))


if __name__ == "__main__":
    unittest.main()
