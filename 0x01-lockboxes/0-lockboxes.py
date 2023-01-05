def canUnlockAll(boxes):
    # Set of boxes that we have keys for
    unlocked = set([0])

    # Stack of boxes to explore
    stack = [0]

    # Depth-first search
    while stack:
        # Get the next box to explore
        box = stack.pop()

        # Add all the boxes that we have keys for
        for key in boxes[box]:
            if key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    # Check if we have keys for all the boxes
    return len(unlocked) == len(boxes)
