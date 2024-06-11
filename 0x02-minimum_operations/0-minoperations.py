#!/usr/bin/python3
"""Dynamic Programming"""
from math import sqrt


def minOperations(n):
    """returns length of Minimum Operations"""
    result = recursive_operation(n)[0]
    return len(result)


def recursive_operation(n):
    """returns Minimum Operations"""
    if n <= 1:
        return [[''], '']
    if n <= 2:
        return [['Copy All', 'Paste'], 'hh']

    mid_val = int(n/2) + 1
    factors = [fac for fac in range(2, mid_val) if not n % fac]

    if sqrt(n) == int(sqrt(n)):  # for perfect square root
        operations = recursive_operation(int(sqrt(n)))

    elif factors:
        for value in factors:
            if value > sqrt(n):
                break
        operations = recursive_operation(value)

    else:  # not divisible by any number
        operations = recursive_operation(2)
        for h in range(len(operations), n):
            operations[0].append('Paste')
            operations[1] = operations[1] + 'h'
        return operations

    stored_cpy = 0
    h = len(operations[1])
    while h < n:
        if not n % h:  # if we are to multiply we'll use Copy and Paste
            stored_cpy = h
            operations[0].extend(['Copy All', 'Paste'])
            operations[1] = operations[1] + (stored_cpy * 'h')
            h = h + stored_cpy
        elif stored_cpy:
            operations[0].append('Paste')
            operations[1] = operations[1] + (stored_cpy * 'h')
            h = h + stored_cpy
        else:
            operations[0].append('Paste')
            operations[1] = operations[1] + 'h'
            h += 1
    return operations
