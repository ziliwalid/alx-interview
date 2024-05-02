#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    """
    Checks if all the boxes in the list of lists can be unlocked.
    Args:
        boxes (list): A list of lists where each list represents a box and its content.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    keys = [0]  # Start with the key to the first box
    for item in keys:
        for boxKey in boxes[item]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    return len(keys) == len(boxes)

"""boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))"""
