#!/usr/bin/python3
"""Dynamic Programming"""
from math import sqrt
from time import sleep


def minOperations(n):
    """returns length of Minimum Operations"""
    result = recursive_operation(n)[0]
    return len(result)


def recursive_operation(n):
    """returns Minimum Operations"""
    if n <= 1:
        return [[], 'h']
    if n <= 2:
        return [['Copy All', 'Paste'], 'hh']

    mid_val = int(n/2) + 1
    # sqrt of any number is always less than mid-point of that number.
    # We only need this to be sure that it is not an indivisible number
    factor = 0
    for fac in range(int(sqrt(n)), mid_val):
        if not n % fac:
            factor = fac
            break

    if sqrt(n) == int(sqrt(n)):  # for perfect square root
        operations = recursive_operation(int(sqrt(n)))

    elif factor:  # for a divisible number
        operations = recursive_operation(factor)

    else:  # not an indivisible number
        operations = recursive_operation(2)
        # for h in range(len(operations), n):
        #     operations[0].append('Paste')
        #     operations[1] = operations[1] + 'h'

        paste = list(['Paste']) * (n - 2)
        store = 'h' * (n - 2)
        operations[0].extend(paste)
        operations[1] = operations[1] + store
        return operations

    stored_cpy = 0
    h = len(operations[1])
    while h < n:
        if not n % h:  # if we are to multiply we'll use Copy and Paste
            stored_cpy = h
            operations[0].extend(['Copy All', 'Paste'])
            operations[1] = operations[1] + (stored_cpy * 'h')
        else:
            operations[0].append('Paste')
            operations[1] = operations[1] + (stored_cpy * 'h')
        h = h + stored_cpy

    return operations
