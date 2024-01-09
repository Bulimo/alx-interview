#!/usr/bin/python3
""" Module 0-lockboxes """


def canUnlockAll(boxes):
    """
    Function  that determines if all the boxes can be opened.
    Returns True or False
    """
    if type(boxes) != list or len(boxes) == 0:
        return False

    visited = set()
    # use deep search first algorithm

    def dfs(box):
        if type(boxes[box]) != list:
            raise TypeError("boxes must be a list of list")
        if box in visited:
            return
        visited.add(box)
        for key in boxes[box]:
            # print('key is {}'.format(key))
            dfs(key)

    dfs(0)  # Start DFS from box 0

    return len(visited) == len(boxes)
