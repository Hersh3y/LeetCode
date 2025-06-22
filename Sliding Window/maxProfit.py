def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    l = 0
    for r in range(len(prices)):
        if prices[l] > prices[r]:
            l = r
        profit = prices[r] - prices[l]
        max_profit = max(max_profit, profit)
    return max_profit


print(maxProfit([7,1,5,3,6,4])) # Outputs 5
print(maxProfit([7,6,4,3,1])) # Outputs 0