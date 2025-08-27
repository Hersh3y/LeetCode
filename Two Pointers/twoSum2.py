def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = 0
    r = len(numbers) - 1
    while r > l:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        if target - numbers[l] - numbers[r] < 0:
            r -= 1
        else:
            l += 1


print(twoSum([2,7,11,15], 9)) # Output: [1, 2]
print(twoSum([2,3,4], 6)) # Output: [1, 3]
print(twoSum([-1,0], -1)) # Output: [1, 2]
print(twoSum([1,2,3,4], 3)) # Output: [1, 2]