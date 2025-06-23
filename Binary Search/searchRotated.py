def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums) - 1
    while r >= l:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > nums[r]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


print(search([4,5,6,7,0,1,2], 0)) # Output: 4
print(search([4,5,6,7,0,1,2], 3)) # Output: -1
print(search([1], 0)) # Output: -1
print(search([3,4,5,6,1,2], 1)) # Output: 4
print(search([3,5,6,0,1,2], 4)) # Output: -1
print(search([6,7,0,1,2,4,5], 4))  # Output: 5
print(search([8,9,2,3,4], 9))  # Output: 1
print(search([4,5,6,7,0,1,2], 5))  # Output: 1