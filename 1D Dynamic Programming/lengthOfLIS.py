def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(lengthOfLIS([10,9,2,5,3,7,101,18])) # Output: 4
print(lengthOfLIS([0,1,0,3,2,3])) # Output: 4
print(lengthOfLIS([7,7,7,7,7,7,7])) # Output: 1
print(lengthOfLIS([9,1,4,2,3,3,7])) # Output: 4
print(lengthOfLIS([0,3,1,3,2,3])) # Output: 4