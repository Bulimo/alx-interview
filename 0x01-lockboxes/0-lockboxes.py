#!/usr/bin/python3
""" Module 0-lockboxes """


def canUnlockAll(boxes):
    """
    Function  that determines if all the boxes can be opened.
    Returns True or False
    """
    can_unlock = {0}
    all_boxes = set(range(1, len(boxes)))

    if len(boxes) > 0:
        # Keep track of newly opened boxes
        new_boxes = {0}

        while new_boxes:
            # Reset new_boxes for the next round of keys
            next_keys = set()
            for i in new_boxes:
                next_keys.update(boxes[i])
            new_boxes = next_keys.difference(can_unlock)
            can_unlock.update(next_keys)
            all_boxes.difference_update(can_unlock)

    return len(all_boxes) == 0
