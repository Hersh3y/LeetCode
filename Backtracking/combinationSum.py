class Solution(object):
    def combinationSum(self, candidates, target):
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
