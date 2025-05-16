#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -1, -20]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 15, 0, -3]), 15)

    def test_all_equal(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.8, 3.9, 2.3]), 3.9)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 3.5, 2]), 3.5)

    def test_string_list(self):
        self.assertEqual(max_integer("Holberton"), "t")  # max char by Unicode

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["alpha", "zeta", "gamma"]), "zeta")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable_argument(self):
        with self.assertRaises(TypeError):
            max_integer(42)

if __name__ == '__main__':
    unittest.main()
