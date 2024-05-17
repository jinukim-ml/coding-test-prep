from bisect import bisect_left
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = bisect_left(intervals, newInterval[0], key=lambda item: item[1])
        if idx == len(intervals):
            intervals.append(newInterval)
            return intervals

        ans = []
        for pos, (st, en) in enumerate(intervals):
            if idx == pos:
                ans.append(newInterval)
            if ans and st <= ans[-1][1]:
                ans[-1] = [min(ans[-1][0], st), max(ans[-1][1], en)]
            else:
                ans.append([st, en])
        
        return ans