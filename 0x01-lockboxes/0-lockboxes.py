#!/usr/bin/python3
"""Lock Boxes"""


def canUnlockAll(boxes):
    """Check if all Boxes can be Opened"""
    if not boxes:
        return
    keys = boxes[0]  # since the first box is always unlock
    result = set(recursion(boxes, keys, 0))
    result.add(0)  # include to result if not already present
    box_length = set(range(len(boxes)))  # inorder to compare
    if (box_length.issubset(result) or result == box_length):
        return True
    return False


def recursion(boxes, keys, index):
    if (index >= len(keys)):
        return keys
    key_idx = keys[index]

    if key_idx >= len(boxes):
        pass
    elif not (set(boxes[key_idx]).issubset(keys)):
        diff = list(set(boxes[key_idx]).difference(set(keys)))
        keys.extend(diff)
    index += 1
    return recursion(boxes, keys, index)
