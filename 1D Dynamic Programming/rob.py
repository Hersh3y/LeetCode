def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    b = 0
    for i in nums:
        x = max(i + a, b)
        a = b
        b = x
    return b


print(rob([1,2,3,1])) # Output: 4
print(rob([2,7,9,3,1])) # Output: 12
print(rob([2,1,1,2])) # Output: 4
print(rob([90,1,1,90,1,1,90])) # Output: 270