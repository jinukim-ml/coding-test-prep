class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        prev = 0
        freetimes = []
        for i in range(len(startTime)):
            freetimes.append(startTime[i] - prev)
            prev = endTime[i]
        freetimes.append(eventTime - endTime[-1])
        l, res, window_sum = 0, 0, 0
        for r in range(len(freetimes)):
            window_sum += freetimes[r]
            if r-l == k:
                res = max(res, window_sum)
                window_sum -= freetimes[l]
                l += 1
        return res