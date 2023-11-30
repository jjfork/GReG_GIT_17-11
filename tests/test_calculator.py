import unittest

from calculator import add, subtract, divide, multiply, square, power, sqrt, trick


class MyTestCase(unittest.TestCase):
    def test_add(self):
        results = add(1, 2)
        self.assertEqual(results, 3)

    def test_divide(self):
        results = divide(6, 2)
        self.assertEqual(results, 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(99, 0)

    def test_multiply(self):
        results = multiply(2, 3)
        self.assertEqual(results, 6)

    def test_power(self):
        results = power(3, 2)
        self.assertEqual(results, 9)

        results = power(3, 3)
        self.assertEqual(results, 27)

    def test_square(self):
        results = square(3)
        self.assertEqual(results, 9)

    def test_subtract(self):
        results = subtract(10, 7)
        self.assertEqual(results, 3)

    def test_sqrt(self):
        results = sqrt(9)
        self.assertEqual(results, 3)

        results = sqrt(16)
        self.assertEqual(results, 4)

    def test_trick(self):
        results = trick('58008')
        self.assertEqual(results, '58008')


if __name__ == "__main__":
    unittest.main()
