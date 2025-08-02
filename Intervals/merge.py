def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort()
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            result[-1] = [min(result[-1][0], intervals[i][0]), max(result[-1][1], intervals[i][1])]
        else:
            result.append(intervals[i])
    return result


print(merge([[1,3],[2,6],[8,10],[15,18]])) # Output: [[1, 6], [8, 10], [15, 18]]
print(merge([[1,4],[4,5]])) # Output: [[1, 5]]
print(merge([[1,3],[1,5],[6,7]])) # Output: [[1, 5], [6, 7]]
print(merge([[1,2],[2,3]])) # Output: [[1, 3]]