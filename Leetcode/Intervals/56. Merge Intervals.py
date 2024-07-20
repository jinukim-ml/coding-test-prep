class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort() # the data is not guaranteed to be sorted in ascending order
        
        ans, i = [], 1
        ans.append(intervals[0])
        while i < len(intervals):
            st, en = ans[-1]

            if st <= intervals[i][0] <= en:
                en = max(en, intervals[i][1])
                ans[-1] = [st, en]
            else:
                ans.append(intervals[i])
            i += 1
        return ans