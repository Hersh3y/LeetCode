def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        othernum = target - nums[i]
        if othernum in hashmap and hashmap[othernum] != i:
            return [i, hashmap[othernum]]


print(twoSum([2,7,11,15], 9)) # Outputs [0, 1]
print(twoSum([3,2,4], 6)) # Outputs [1, 2]
print(twoSum([3,3], 6)) # Outputs [0, 1]