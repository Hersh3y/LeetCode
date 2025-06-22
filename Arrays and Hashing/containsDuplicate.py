def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums_set = set()
    for i in nums:
        if i in nums_set:
            return True
        nums_set.add(i)
    return False


print(containsDuplicate([1,2,3,1])) # Outputs True
print(containsDuplicate([1,2,3,4])) # Outputs False
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # Outputs True