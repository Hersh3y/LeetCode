def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    result = 0
    for i in range(32):
        if (n & (1 << i)) > 0:
            result += 1
    return result


print(hammingWeight(11)) # Output: 3
print(hammingWeight(128)) # Output: 1
print(hammingWeight(2147483645)) # Output: 30