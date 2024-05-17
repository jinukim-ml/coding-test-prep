from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]

        for _, (st, en) in enumerate(intervals, 1):
            right = ans[-1][1]

            if right >= st:
                ans[-1][1] = max(right, en)
            else:
                ans.append([st, en])
        return ans