# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start = []
        for i in intervals:
            start.append(i.start)
        start.sort()
        end = []
        for i in intervals:
            end.append(i.end)
        end.sort()
        result = 0
        count = 0
        s = 0
        e = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            result = max(result, count)
        return result