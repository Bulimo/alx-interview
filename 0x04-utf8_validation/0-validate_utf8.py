#!/usr/bin/python3
"""
Module 0-validate_utf8
Implements validUTF8() method
"""


def validUTF8(data):
    """
    Method that determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
      data(list): data to check that is a list of integers

    Return:
      True if data is a valid UTF-8 encoding, else return False
    """
    def countLeadingOnes(byte):
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    # Check each byte in the data
    i = 0
    while i < len(data):
        num_bytes = 0

        # Count leading '1' bits to determine the number of
        # bytes in the current character
        leading_ones = countLeadingOnes(data[i])

        # Handle the special case where the first byte has 0 leading '1' bits
        if leading_ones == 0:
            num_bytes = 1
        else:
            # Invalid case if leading '1' bits are more than 4 or less than 1
            if leading_ones < 1 or leading_ones > 4:
                return False

            num_bytes = leading_ones

        # Check if there are enough bytes in the data
        if i + num_bytes > len(data):
            return False

        # Check if the following bytes have the correct format (10xxxxxx)
        for j in range(1, num_bytes):
            if not (data[i + j] & 0b11000000 == 0b10000000):
                return False

        i += num_bytes

    return True
