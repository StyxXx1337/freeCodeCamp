from typing import Tuple

from data_linked_list import LinkedList

def merge_sort(linked_list: LinkedList) -> LinkedList:
    """Sorts a linked list in ascending order
    Recursively dived the linked list into sublists containing a single node
    Repeatedly merges the sublists to produce sorted sublists until one remains
    :param linked_list:
    :return LinkedList
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list: LinkedList) -> Tuple(LinkedList, LinkedList):
    """
    Divide the unsorted list at the midpoint into sublists
    :param linked_list:
    :return Tuple(LinkedList, LinkedList):
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size()
        midpoint = size // 2

