class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: (x[1], x[0]))
        i = 0
        while meetings:
            i = len(meetings)-1
            last = meetings[i]
            l, r = last[0], last[1]
            while i >= 0 and l <= meetings[i][1] <= r:
                l = min(l, meetings[i][0])
                r = max(r, meetings[i][1])
                meetings.pop()
                i -= 1
            days -= r - l + 1
        return days