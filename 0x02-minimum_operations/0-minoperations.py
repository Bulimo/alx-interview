#!/usr/bin/python3
""" Module 0-minoperations """


def minOperations(n):
    """
    method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    Args:
      - n(int): Number of characters to have in the file

    Returns:
      - (int): Number of min operations or 0
    """
    if n == 0 or n == 1 or not (isinstance(n, int)):
        return 0

    xters = 1  # Initial character is 1
    copyXters = 0  # holds copied characters
    rem = n - xters  # holds remaining characters
    opCount = 0  # counter for operations

    while xters < n:
        if xters == 1 and opCount == 0:
            # This is case for the start of operations
            copyXters = xters
            opCount += 1
            xters += copyXters
            opCount += 1
            rem = n - xters
        elif xters < rem and rem % xters == 0:
            # if xters are multiples of rem, we copy then paste
            if 2 * xters <= n:
                copyXters = xters
                opCount += 1
            xters += copyXters
            opCount += 1
            rem = n - xters
        else:
            xters += copyXters
            opCount += 1
            rem = n - xters
    return opCount
