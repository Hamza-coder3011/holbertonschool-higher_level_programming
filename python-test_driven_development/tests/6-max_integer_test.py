#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max is at the beginning of the list."""
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_at_middle(self):
        """Test when the max is in the middle of the list."""
        self.assertEqual(max_integer([1, 5, 3, 2]), 5)

    def test_negative_numbers(self):
        """Test list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, 0, -5]), 2)

    def test_one_element(self):
        """Test list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test list with floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_identical_elements(self):
        """Test list where all elements are identical."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_large_list(self):
        """Test a large list."""
        large_list = list(range(1000))
        self.assertEqual(max_integer(large_list), 999)
