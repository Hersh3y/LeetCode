def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_product = nums[0]
    current_max = nums[0]
    current_min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            current_max, current_min = current_min, current_max
        current_max = max(current_max * nums[i], nums[i])
        current_min = min(current_min * nums[i], nums[i])
        max_product = max(max_product, current_max)
    return max_product


print(maxProduct([2, 3, -2, 4])) # Output: 6
print(maxProduct([-2, 0, -1])) # Output: 0
print(maxProduct([1, 2, -3, 4])) # Output: 4
print(maxProduct([-2, -1])) # Output: 2