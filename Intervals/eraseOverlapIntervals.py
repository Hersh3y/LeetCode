def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort()
    result = 0
    prev_end = intervals[0][1]
    for i in range(1, len(intervals)):
        if prev_end <= intervals[i][0]:
            prev_end = intervals[i][1]
        else:
            prev_end = min(prev_end, intervals[i][1])
            result += 1
    return result


print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # Output: 1
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # Output: 2
print(eraseOverlapIntervals([[1,2],[2,3]])) # Output: 0
print(eraseOverlapIntervals([[1,2],[2,4],[1,4]])) # Output: 1