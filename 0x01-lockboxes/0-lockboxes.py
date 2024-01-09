#!/usr/bin/python3
""" Module 0-lockboxes """


def canUnlockAll(boxes):
    """
    Function  that determines if all the boxes can be opened.
    Returns True or False
    """
    if type(boxes) is not list or len(boxes) == 0:
        return False

    # visited = set()
    # # use deep search first algorithm

    # def dfs(box):
    #     if box in visited:
    #         return
    #     visited.add(box)
    #     for key in boxes[box]:
    #         # print('key is {}'.format(key))
    #         dfs(key)

    # dfs(0)  # Start DFS from box 0

    # return len(visited) == len(boxes)
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    available_boxes = [0]

    while available_boxes:
        current_box = available_boxes.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                available_boxes.append(key)

    return all(visited)
