from typing import Tuple


def merge_sort(in_list: list[int]) -> list[int]:
    """ Sorts a list in ascending order
    :param in_list: list to be sorted
    :return sorted list[int]

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Time Complexity: O(n*log(n))
    """

    if len(in_list) <= 1:
        return in_list

    left_half, right_half = split(in_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(in_list) -> Tuple[list[int], list[int]]:
    """
    Divide the unsorted list at midpoint into sublists
    :param in_list:
    :return Tuple(list[int], list[int]):
    Time Complexity: O(log(n))
    """

    midpoint = len(in_list) // 2
    left = in_list[:midpoint]
    right = in_list[midpoint:]

    return left, right


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merges two lists, sorting them in the process
    :param left: list[int]
    :param right: list[int]
    :return list[int]
    Time Complexity: O(n)
    """

    result = []
    left_counter = 0
    right_counter = 0

    while left_counter < len(left) and right_counter < len(right):
        if left[left_counter] < right[right_counter]:
            result.append(left[left_counter])
            left_counter += 1
        else:
            result.append(right[right_counter])
            right_counter += 1

    while left_counter < len(left):
        result.append(left[left_counter])
        left_counter += 1

    while right_counter < len(right):
        result.append(right[right_counter])
        right_counter += 1

    return result


def verify_sorted(in_list: list[int]) -> True:
    n = len(in_list)

    if n == 0 or n == 1:
        return True

    return in_list[0] < in_list[1] and verify_sorted(in_list[1:])


alist = [90, 88, 67, 77, 102, 34, 23, 60, 2, 9]
print(verify_sorted(alist))
print(verify_sorted(merge_sort(alist)))
