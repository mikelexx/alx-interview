#!/usr/bin/python3
"""contains interview question solution for Lockboxes """


def unlock_box(boxes, idx, box_size, vis_boxes):
    """unlocks all the boxes it can using the keys provided
    at the box at idx position
    """
    for key in boxes[idx]:
        if type(key) is int \
         and key not in vis_boxes and key < box_size:
            vis_boxes.add(key)
            unlock_box(boxes, key, box_size, vis_boxes)


def canUnlockAll(boxes):
    """
    determines if all locked boxes can be
    unlocked using keys provied at zeroth box
    """
    if not boxes or type(boxes) is not list:
        return False
    vis_boxes = set([0])
    unlock_box(boxes, 0, len(boxes), vis_boxes)
    return len(vis_boxes) == len(boxes)
