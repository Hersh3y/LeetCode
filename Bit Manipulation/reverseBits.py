def reverseBits(n):
    """
    :type n: int
    :rtype: int
    """
    result = 0
    for i in range(32):
        if ((n >> i) & 1) == 1:
            result = result | (1 << (31 - i))
    return result


print(reverseBits(43261596)) # Output: 964176192
print(reverseBits(2147483644)) # Output: 1073741822