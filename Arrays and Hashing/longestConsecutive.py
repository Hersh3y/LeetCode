def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    longest = 0
    set_nums = set(nums)
    for i in set_nums:
        if i - 1 not in set_nums:
            count = 1
            while i + 1 in set_nums:
                count += 1
                i += 1
            longest = max(longest, count)
    return longest


print(longestConsecutive([100,4,200,1,3,2])) # Output: 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # Output: 9
print(longestConsecutive([1,0,1,2])) # Output: 3
print(longestConsecutive([2,20,4,10,3,4,5])) # Output: 4
print(longestConsecutive([0,3,2,5,4,6,1,1])) # Output: 7