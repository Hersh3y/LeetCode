def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return (len(nums) * (len(nums) + 1) // 2) - sum(nums)


print(missingNumber([3,0,1])) # Output: 2
print(missingNumber([0,1])) # Output: 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # Output: 8
print(missingNumber([1,2,3])) # Output: 0
print(missingNumber([0,2])) # Output: 1