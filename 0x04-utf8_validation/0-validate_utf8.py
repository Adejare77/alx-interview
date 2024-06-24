#!/usr/bin/python3
"""UTF-8 Validation"""
"""
Write a method that determines if a given data set represents a valid UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
"""

# def validUTF8(data):
#     """determines if a given data set represents a valid UTF-8
#     encoding. Return True if it is, else False
#     """
#     # For Ascii characters
#     min_val = bin(0)
#     max_val = bin(127)
#     print(min_val, max_val)
#     for values in data:
#         print(values, bin(values))
#         if not (bin(values) >= min_val and bin(values) <= max_val):
#             return False
#         str_val = str(values)
#         # for character in str_val:
#         #     print(character)
#         #     print(ord(character))
#         #     if not (bin(ord(character)) >= min_val and bin(ord(character)) <= max_val):
#         #         return False
#     return True

def validUTF8(data):
    """determines if a given data set represents a valid UTF-8
    encoding. Return True if it is, else False
    """
    # For Ascii characters
    min_val = 0
    max_val = 127
    for values in data:
        if not (values >= min_val and values <= max_val):
            return False
    return True
