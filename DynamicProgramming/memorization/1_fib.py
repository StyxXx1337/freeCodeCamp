def fibonacci_calculation(position: int) -> int:
    if position == 0:
        return 0
    elif position <= 2:
        return 1

    return fibonacci_calculation(position - 1) + fibonacci_calculation(position - 2)


def fibonacci_calculation_memo(position: int, memo={}) -> int:
    if position == 0:
        return 0
    elif position <= 2:
        return 1
    if position in memo:
        return memo[position]

    memo[position] = fibonacci_calculation_memo(position - 1, memo) + fibonacci_calculation_memo(position - 2, memo)
    return memo[position]


print("======================== Fibonacci Recursive without memorization ==============================")
print(fibonacci_calculation(0))  # 0
print(fibonacci_calculation(2))  # 1
print(fibonacci_calculation(10))  # 55
print(fibonacci_calculation(25))  # 75,025
print(fibonacci_calculation(40))  # 102,334,155

print("======================== Fibonacci Recursive with memorization ==============================")
print(fibonacci_calculation_memo(0))  # 0
print(fibonacci_calculation_memo(2))  # 1
print(fibonacci_calculation_memo(10))  # 55
print(fibonacci_calculation_memo(25))  # 75,025
print(fibonacci_calculation_memo(40))  # 102,334,155
