from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for schedule in intervals:
            time.append((schedule.start, 1))
            time.append((schedule.end,-1))
        
        time.sort(key=lambda x: (x[0], x[1]))

        cnt, maxcnt = 0, 0
        for t in time:
            cnt += t[1]
            maxcnt = max(maxcnt, cnt)
        
        return maxcnt