def binary_search_recursive_binary(numbers_list: list[int], target: int) -> bool:
    """ Executes a binary search algorithm and returns True if found, False otherwise """
    if len(numbers_list) == 0:
        return False

    midpoint = len(numbers_list) // 2
    if numbers_list[midpoint] == target:
        return True
    elif numbers_list[midpoint] > target:
        new_list = numbers_list[:midpoint]
        return binary_search_recursive_binary(new_list, target)
    elif numbers_list[midpoint] < target:
        new_list = numbers_list[midpoint + 1:]
        return binary_search_recursive_binary(new_list, target)

    return False


def binary_search_recursive(numbers_list: list[int], target: int, first=0, last=None) -> int:
    """ Executes a binary search algorithm and returns the Index at which it was found """

    if last is None:
        last = len(numbers_list) - 1

    if last <= first:
        return None

    midpoint = (first + last) // 2

    if numbers_list[midpoint] == target:
        return midpoint
    elif numbers_list[midpoint] > target:
        new_last = midpoint - 1
        return binary_search_recursive(numbers_list, target, first=first, last=new_last)
    elif numbers_list[midpoint] < target:
        new_first = midpoint + 1
        return binary_search_recursive(numbers_list, target, first=new_first, last=last)

    return None


def verify(index: int) -> None:
    """ Prints out the result to the console """
    if index is None:
        print("Target not found in the list.")
    else:
        print("Target found at index: ", index)


def verify_binary(is_in: bool) -> None:
    """ Prints out the result to the console """
    if is_in is False:
        print("Target not found in the list.")
    else:
        print("Target found in the list.")


numbers = [i for i in range(1, 21)]

# Returns the Index where it is found
result = binary_search_recursive(numbers, 22)
verify(result)
result = binary_search_recursive(numbers, 12)
verify(result)

# Binary Check
result = binary_search_recursive_binary(numbers, 22)
verify_binary(result)
result = binary_search_recursive_binary(numbers, 12)
verify_binary(result)
