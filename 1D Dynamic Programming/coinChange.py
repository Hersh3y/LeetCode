def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    result = [amount + 1] * (amount + 1)
    result[0] = 0
    for i in range(1, amount + 1):
        for j in coins:
            if i - j >= 0:
                result[i] = min(result[i], 1 + result[i - j])
    if result[amount] != amount + 1:
        return result[amount]
    else:
        return -1


print(coinChange([1, 2, 5], 11)) # Output: 3
print(coinChange([2], 3)) # Output: -1
print(coinChange([1], 0)) # Output: 0
print(coinChange([1, 5, 10], 12)) # Output: 3