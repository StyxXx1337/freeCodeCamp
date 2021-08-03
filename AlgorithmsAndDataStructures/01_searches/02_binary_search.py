def binary_search(numbers_list: list[int], target: int) -> int:
    first = 0
    last = len(numbers_list) - 1

    while (last-first) > 1:
        middle = (last + first)//2
        if numbers_list[middle] == target:
            return middle
        elif numbers_list[middle] > target:
            last = middle - 1
        elif numbers_list[middle] < target:
            first = middle + 1

    return None


def verify(index: int) -> None:
    if index is None:
        print("Target not found in the list.")
    else:
        print("Target found at index: ", index)


numbers = [i for i in range(1,21)]

result = binary_search(numbers, 22)
verify(result)

result = binary_search(numbers, 12)
verify(result)
