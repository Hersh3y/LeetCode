def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = (i >> 1) + (i & 1)
    return result


print(countBits(2)) # Output: [0, 1, 1]
print(countBits(5)) # Output: [0, 1, 1, 2, 2, 3]
print(countBits(4)) # Output: [0, 1, 1, 2, 2]