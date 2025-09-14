#!/usr/bin/python3
"""
This module defines the function `matrix_divided`.

The function divides all elements of a matrix by a given number.

It validates input types and sizes, and returns
a new matrix with results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists): A matrix of integers/floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by div,
                       rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows of the matrix are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix type
    if (not isinstance(matrix, list) or matrix == []
            or not all(isinstance(row, list) for row in matrix)
            or not all(isinstance(x, (int, float))
                       for row in matrix for x in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Validate rows size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix
    return [[round(x / div, 2) for x in row] for row in matrix]
