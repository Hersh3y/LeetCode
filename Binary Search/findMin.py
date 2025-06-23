def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    r = len(nums) - 1
    while r > l:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]


print(findMin([3,4,5,1,2])) # Output: 1
print(findMin([4,5,6,7,0,1,2])) # Output: 0
print(findMin([11,13,15,17])) # Output: 11
print(findMin([3,4,5,6,1,2])) # Output: 1
print(findMin([4,5,0,1,2,3])) # Output: 0
print(findMin([4,5,6,7])) # Output: 4
print(findMin([1])) # Output: 1
print(findMin([2,1])) # Output: 1