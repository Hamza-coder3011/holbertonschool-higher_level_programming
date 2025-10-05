#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]  # Last row added
        new_row = [1]  # Every row starts with 1

        # Compute middle values as sum of two adjacent values
        # from the previous row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
