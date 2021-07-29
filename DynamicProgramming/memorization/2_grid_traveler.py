def grid_traveler(height: int, length: int) -> int:
    if height == 0 or length == 0:
        return 0
    elif height == 0 or length == 1:
        return 1

    ways = grid_traveler(height - 1, length) + grid_traveler(height, length - 1)
    return ways


def grid_traveler_memo(height: int, length: int, memo={}) -> int:
    id1 = str(height) + '-' + str(length)
    id2 = str(length) + '-' + str(height)

    if height == 0 or length == 0:
        return 0
    elif height == 1 or length == 1:
        return 1
    elif id1 in memo:
        return memo[id1]
    elif id2 in memo:
        return memo[id2]

    memo[id1] = grid_traveler_memo(height - 1, length, memo) + grid_traveler_memo(height, length - 1, memo)
    return memo[id1]


print("======================== Grid Traveler without memorization ==============================")
print(grid_traveler(1, 1))  # 1
print(grid_traveler(2, 3))  # 3
print(grid_traveler(5, 5))  # 70
print(grid_traveler(15, 15))  # 40,116,600

print("======================== Grid Traveler with memorization ==============================")
print(grid_traveler_memo(1, 1))  # 1
print(grid_traveler_memo(2, 3))  # 3
print(grid_traveler_memo(5, 5))  # 70
print(grid_traveler_memo(15, 15))  # 40,116,600
