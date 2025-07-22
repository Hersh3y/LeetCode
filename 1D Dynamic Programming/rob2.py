def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    
    def house_rob(houses):
        a = 0
        b = 0
        for i in houses:
            temp = max(i + a, b)
            a = b
            b = temp
        return b
    
    return max(house_rob(nums[:-1]), house_rob(nums[1:]))


print(rob([2, 3, 2])) # Output: 3
print(rob([1, 2, 3, 1])) # Output: 4
print(rob([1, 2, 3])) # Output: 3
print(rob([3, 4, 3])) # Output: 4
print(rob([2, 9, 8, 3, 6])) # Output: 15