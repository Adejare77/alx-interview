#!/usr/bin/python3
"""UTF-8 Validation"""
"""
Write a method that determines if a given data set represents
a valid UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only
    need to handle the 8 least significant bits of each integer
"""


# def validUTF8(data):
#     """determines if a given data set represents a valid UTF-8
#     encoding. Return True if it is, else False
#     """
#     one_byte_utf8_seq = 1 << 7  # MSB mask for single-byte is '1' in 1000000

#     for item in data:
#         # when item is compared with one_byte_utf8_seq
#         # if item < 128, then the MSB will always be '0'
#         # if item  >= 128, the item MSB will be 1 OR
#         # length of item and one_byte_utf8_seq will differ
#         if one_byte_utf8_seq & item:
#             return False
#     return True

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    n_bytes = 0

    for num in data:
        # Get the last 8 bits in binary format
        bin_rep = format(num, '#010b')[-8:]
        if n_bytes == 0:
            if bin_rep[0] == '0':
                continue
            # elif bin_rep[:3] == '110':
            #     n_bytes = 1
            # elif bin_rep[:4] == '1110':
            #     n_bytes = 2
            # elif bin_rep[:5] == '11110':
            #     n_bytes = 3
            else:
                return False
        else:
            if bin_rep[:2] != '10':
                return False
            n_bytes -= 1

    return n_bytes == 0
