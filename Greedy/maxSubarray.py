def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = nums[0]
    current = nums[0]
    for i in nums:
        current = max(current + i, i)
        result = max(result, current)
    return result


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # Output: 6
print(maxSubArray([5,4,-1,7,8])) # Output: 28
print(maxSubArray([2,-3,4,-2,2,1,-1,4])) # Output: 9
print(maxSubArray([-1])) # Output: -1