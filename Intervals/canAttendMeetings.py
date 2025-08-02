# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals:
            return True
        for i in range(len(intervals)):
            intervals[i] = [intervals[i].start, intervals[i].end]
        intervals.sort()
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                return False
            prev_end = intervals[i][1]
        return True