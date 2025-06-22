def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1


print(search([-1,0,3,5,9,12], 9)) # Outputs 4
print(search([-1,0,3,5,9,12], 2)) # Outputs -1
print(search([-1,0,2,4,6,8], 4)) # Outputs 3
print(search([-1,0,2,4,6,8], 3)) # Outputs -1