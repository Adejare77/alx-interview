# UTF-8 Validation

Concepts Needed:

    Bitwise Operations in Python:
        Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).
        Python Bitwise Operators

    UTF-8 Encoding Scheme:
        Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
        Understanding the patterns that represent a valid UTF-8 encoded character.
        UTF-8 Wikipedia
        Characters, Symbols, and the Unicode Miracle
        The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets

    Data Representation:
        How to represent and work with data at the byte level.
        Handling the least significant bits (LSB) of integers to simulate byte data.

    List Manipulation in Python:
        Iterating through lists, accessing list elements, and understanding list comprehensions.
        Python Lists

    Boolean Logic:
        Applying logical operations to make decisions within the program.


## Valid UTF-8 Encoding Rules

1. Single-byte (ASCII): 0xxxxxxx (2^7) [0-127]
2. Two-byte Sequence: 110xxxxx 10xxxxxx  (2^11) [256 - 2^11]
3. Three-byte Sequence: 1110xxxx 10xxxxxx 10xxxxxx  (2^16) [2049 - 2^16]
4. Four-byte Sequence: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx (2^21)


### Examples: Using format() function

to_binary = format(num, '#08b'), where '#' => 0b, 0 is for padding, 8 is the width, 'b' is binary
to_binary = format(num, 'b')
to_integer = format(value, '05d'), where d is integer
to_hex = format(number, '#010x'), where '#' = 0x, 0 is padding and 10 is width. 'x' is hex
to_float = format(value, '08.3f')
to_string = format(text, '>10') # Right-Justify with space
to_string = format(text, '<10') # Left-Justify with space
