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
    def dec_to_bin(num):
        """
        Converts the number from decimal to binary
        Returns: List of binary representation of num
        """
        # val = [int(x) for x in bin(num)[2:]]
        # if len(val) > 8:
        #     return val[1:]
        # return [0] * (8 - len(val)) + val
        val = [int(x) for x in f"{num:08b}"]
        return val

    continuation_bits = 0
    # Iterate over all the characters in the data set
    for xter in data:
        val = dec_to_bin(xter)
        if 1 not in val:
            # print("False coz all 8 bits being 0")
            return False
        if continuation_bits > 0:
            # This character is part of the previous data set
            if val[0] != 1 and val[1] != 0:
                # print("False coz continuation is not [10xxxx]")
                return False
            continuation_bits -= 1
        else:
            # Start of new character set of data
            # print("val = {}".format(val))
            # Check for invalid starting patterns
            if val[0] == 1 and val[1] == 0:
                # Invalid start for a character
                return False

            # Count the number of continuation bits
            for i in val:
                if i == 1:
                    continuation_bits += 1
                else:
                    break
            # if continuation_bits == 1:
            #     # print("False coz not continuation and starts\
            #     with 1[1xxxx]")
            #     return False
            # if continuation_bits == 0:
            #     continue
            # elif continuation_bits > 1 and continuation_bits <= 6:
            #     continuation_bits -= 1
            # else:
            #     continuation_bits = 5
            # if continuation_bits:
            #     print("continuation_bits = {}".format(continuation_bits))
            #     print("We have continuation from {}".format(xter))
            # Validate the count of continuation bits
            if continuation_bits == 1 or continuation_bits > 4:
                # Invalid continuation bits count
                return False

            continuation_bits = max(continuation_bits - 1, 0)
    return continuation_bits == 0
