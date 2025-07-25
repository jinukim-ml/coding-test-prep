class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        i = 0
        res = 0
        while i < len(intervals):
            l, r = intervals[i]
            res += 1
            while i < len(intervals) and l <= intervals[i][0] and intervals[i][1] <= r:
                i += 1
        return res