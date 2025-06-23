def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hashmap = {}


print(topKFrequent([1,1,1,2,2,3], 2)) # Output: [1,2]
print(topKFrequent([1], 1)) # Output: [1]
print(topKFrequent([1,2,2,3,3,3], 2)) # Output: [2,3]
print(topKFrequent([7,7], 1)) # Output: [7]