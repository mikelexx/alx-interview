#!/usr/bin/python3
"""contains interview question solution for Lockboxes """
import collections


def canUnlockAll(boxes):
    """
    determines if all locked boxes can be
    unlocked using keys provied at zeroth box
    """
    queue = collections.deque(boxes[0])
    vis = set([0])
    box_size = len(boxes)
    while len(queue):
        key = queue.popleft()
        if key not in vis and key < box_size:
            for el in boxes[key]:
                queue.append(el)
            vis.add(key)
    return len(vis) == box_size
