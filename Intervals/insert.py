def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    result = []
    for i in range(len(intervals)):
        if intervals[i][0] > newInterval[1]:
            result.append(newInterval)
            return result + intervals[i:]
        if intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    result.append(newInterval)
    return result


print(insert([[1,3],[6,9]], [2,5])) # Output: [[1, 5], [6, 9]]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # Output: [[1, 2], [3, 10], [12, 16]]
print(insert([[1,2],[3,5],[9,10]], [6,7])) # Output: [[1, 2], [3, 5], [6, 7], [9, 10]]