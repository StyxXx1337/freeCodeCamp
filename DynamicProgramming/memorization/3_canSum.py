def canSum(sum: int, numbers: list) -> bool:
    if sum == 0:
        return True
    elif sum < 0:
        return False

    for number in numbers:
        if canSum(sum - number, numbers):
            return True

    return False


def canSum_memo(sum: int, numbers: list, memo=None) -> bool:
    if memo is None:      # Since {} would be a mutable object ==> False
        memo = {}
    if sum in memo:
        return memo[sum]
    if sum == 0:
        return True
    elif sum < 0:
        return False

    for number in numbers:
        remainder = sum - number
        if canSum_memo(remainder, numbers, memo):
            memo[sum] = True
            return True

    memo[sum] = False
    return False


print("======================== Can Sum without memorization ==============================")
print(canSum(7, [5, 3, 4, 7]))       # True
print(canSum(7, [2, 4]))             # False
print(canSum(8, [5, 2, 4, 6]))       # True
print(canSum(17, [11, 4, 7]))        # False
# print(canSum(300, [7, 14]))        # False --> Takes very long
print()
print("======================== Can Sum with memorization ==============================")
print(canSum_memo(7, [5, 3, 4, 7]))  # True
print(canSum_memo(7, [2, 4]))        # False
print(canSum_memo(8, [5, 2, 4, 6]))  # True
print(canSum_memo(17, [11, 4, 7]))   # False
print(canSum_memo(300, [7, 14]))     # False
