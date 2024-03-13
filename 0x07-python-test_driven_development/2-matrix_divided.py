#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a number.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The number to divide by.

    Returns:
    list of lists: A new matrix with all elements divided by div, rounded to 2 decimal places.
    """

    # Try to cast div and all elements of matrix to floats
    try:
        div = float(div)
        matrix = [[float(item) for item in row] for row in matrix]
    # If casting fails, raise a TypeError
    except ValueError:
        raise TypeError("div must be a number and matrix must be a matrix (list of lists) of integers/floats")
    else:
        # If div is zero, raise a ZeroDivisionError
        if div == 0:
            raise ZeroDivisionError("division by zero")
        # If not all rows of matrix have the same size, raise a TypeError
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    # Return a new matrix with all elements divided by div, rounded to 2 decimal places
    return [[round(item / div, 2) for item in row] for row in matrix]

