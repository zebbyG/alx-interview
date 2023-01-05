#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """Set of unlocked boxes"""
    unlocked = {0}

    """Iterate through the boxes, starting from the first one"""
    for i in range(len(boxes)):
        """If the current box has keys, add the corresponding boxes to the set of unlocked boxes"""
        for key in boxes[i]:
            unlocked.add(key)

    """Return whether all boxes can be unlocked"""
    return len(unlocked) == len(boxes)
