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


def split(linked_list: LinkedList) -> Tuple[LinkedList, LinkedList]:
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

        mid_node = linked_list.node_at_index(midpoint - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes.
    Returns a new, merged list
    """

    # Creating a new linked list that contains nodes from
    # merging left and right

    merged = LinkedList()

    # Add a fake HEAD that is discarded later
    merged.add(0)

    # Set current to the head of the final linked list
    current = merged.head

    # Obtain the head of the list and right list
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node or either
    while left_head or right_head:

        # If the head node of the left is None, we're past the tail
        # Add the node from the right to the merged list
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node

        # If head node of the right is None, we're past the tail
        # Add the node from the left to the merge list
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node

        else:
            # Not at either tail node. Obtain Node data to compare
            left_data = left_head.data
            right_data = right_head.data

            # if left data is smaller than right data set left_data to current
            if left_data < right_data:
                current.next_node = left_head
                # Mode the head to the next Node
                left_head = left_head.next_node

            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Replace Fake Head
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_ll = merge_sort(l)
print(sorted_ll)
