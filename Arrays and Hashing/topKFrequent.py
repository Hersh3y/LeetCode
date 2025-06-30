def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = 0
        hashmap[nums[i]] += 1
    result = []
    sorted_values = (sorted(hashmap.values()))[::-1]
    frequent_values = set(sorted_values[:k])
    for key, value in hashmap.items():
        if value in frequent_values:
            result.append(key)
    return result


print(topKFrequent([1,1,1,2,2,3], 2)) # Output: [1,2]
print(topKFrequent([1], 1)) # Output: [1]
print(topKFrequent([1,2,2,3,3,3], 2)) # Output: [2,3]
print(topKFrequent([7,7], 1)) # Output: [7]