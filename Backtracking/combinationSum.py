def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []
    def backtrack(start, current, current_sum):
        if current_sum == target:
            result.append(current[:])
            return
        elif current_sum > target:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, current_sum + candidates[i])
            current.pop()
    backtrack(0, [], 0)
    return result


print(combinationSum([2,3,6,7], 7)) # Output: [[2, 2, 3], [7]]
print(combinationSum([2,3,5], 8)) # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(combinationSum([2], 1)) # Output: []
print(combinationSum([2,5,6,9], 9)) # Output: [[2, 2, 5], [9]]
print(combinationSum([3,4,5], 16)) # Output: [[3, 3, 3, 3, 4], [3, 3, 5, 5], [3, 4, 4, 5], [4, 4, 4, 4]]
print(combinationSum([3], 5)) # Output: []