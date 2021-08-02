def howSum(target_sum: int, numbers: list[int]) -> list[int]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        if howSum(remainder, numbers) != None:
            result = howSum(remainder, numbers)
            result.append(num)
            return result

    return None


def howSum_memo(target_sum: int, numbers: list[int], memo=None) -> list[int]:
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        result = howSum_memo(remainder, numbers, memo)
        if result is not None:
            memo[remainder] = result
            result.append(num)
            return result

    memo[target_sum] = None
    return None


print("======================== How Sum without memorization ==============================")
print(howSum(7, [5, 3, 4, 7]))   # [4, 3]
print(howSum(7, [2, 4]))         # None
print(howSum(8, [5, 2, 4, 6]))   # [2, 2, 2, 2]
print(howSum(17, [11, 4, 7]))    # None
# print(howSum(300, [7, 14]))      # False --> Takes very long
# print(howSum(300, [1, 14]))      # [1, ..., 1] --> Takes very long
print()
print("======================== How Sum with memorization ==============================")
print(howSum_memo(7, [5, 3, 4, 7]))    # [4, 3]
print(howSum_memo(7, [2, 4]))          # None
print(howSum_memo(8, [5, 2, 4, 6]))    # [2, 2, 2, 2]
print(howSum_memo(17, [11, 4, 7]))     # None
print(howSum_memo(300, [7, 14]))       # None
print(len(howSum_memo(300, [1, 14])))  # [1, ..., 1] -> len = 300
