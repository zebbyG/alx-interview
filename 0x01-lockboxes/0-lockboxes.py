#!/usr/bin/python3


def canUnlockAll(boxes):
    # Set to store visited boxes
    visited = set()
    # Queue for breadth-first search
    queue = []

    # Start with the first box
    queue.append(boxes[0])
    visited.add(0)

    # Perform breadth-first search
    while queue:
        # Get the next box
        box = queue.pop(0)
        # Check all the keys in the box
        for key in box:
            # If the key corresponds to a not visited box, add it to the queue
            if key not in visited:
                queue.append(boxes[key])
                visited.add(key)

    # Return whether all boxes have been visited
    return len(visited) == len(boxes)
