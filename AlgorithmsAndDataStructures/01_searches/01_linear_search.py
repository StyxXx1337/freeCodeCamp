def linear_search(number_list: list[int], target: int) -> int:
    for i in range(len(number_list)):
        if number_list[i] == target:
            return i

    return None


def verify(index: int) -> None:
    if index is None:
        print("Target not found in the list.")
    else:
        print("Target found at index: ", index)


numbers = [i for i in range(20)]

result = linear_search(numbers, 22)
verify(result)

result = linear_search(numbers, 12)
verify(result)
