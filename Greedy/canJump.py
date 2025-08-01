def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    goal = len(nums) - 1
    for i in range(goal - 1, -1, -1):
        if goal - i <= nums[i]:
            goal = i
    return goal == 0
    

print(canJump([2,3,1,1,4])) # Output: True
print(canJump([3,2,1,0,4])) # Output: False
print(canJump([1,2,0,1,0])) # Output: True
print(canJump([1,2,1,0,1])) # Output: False