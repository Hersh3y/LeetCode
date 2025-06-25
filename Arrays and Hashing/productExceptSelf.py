def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result


print(productExceptSelf([1,2,3,4])) # Output: [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3])) # Output: [0,0,9,0,0]
print(productExceptSelf([1,2,4,6])) # Output: [48,24,12,8]
print(productExceptSelf([-1,0,1,2,3])) # Output: [0,-6,0,0,0]