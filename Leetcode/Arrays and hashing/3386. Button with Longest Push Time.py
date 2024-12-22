class Solution:
    def buttonWithLongestTime(self, events: list[list[int]]) -> int:
        ans = events[0][0]
        maxtime = events[0][1]
        for i in range(1, len(events)):
            index, t = events[i]
            diff = t - events[i-1][1]
            if diff > maxtime:
                ans = index
                maxtime = diff
            elif diff == maxtime:
                ans = min(ans, index)
        return ans