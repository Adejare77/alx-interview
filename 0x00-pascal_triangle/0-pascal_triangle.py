#!/usr/bin/python3
"""Create a Pascal Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers"""
    if n <= 0:
        return []
    returned_list = []
    for height in range(n):
        _list = []
        for size in range(height):
            if size == 0:
                _list.append(1)
            else:
                prev_return_list = returned_list[height - 1]
                value = prev_return_list[size - 1] + prev_return_list[size]
                _list.append(value)
        _list.append(1)
        returned_list.append(_list)
    return returned_list
