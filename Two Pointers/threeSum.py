def threeSum(nums: list[int]) -> list[list[int]]:
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while r > l:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while r > l and nums[l] == nums[l-1]:
                    l += 1
                while r > l and nums[r] == nums[r+1]:
                    r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1
    return result



print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print(threeSum([0,0,0,0]))