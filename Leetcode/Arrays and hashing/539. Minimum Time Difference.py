class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        for i, t in enumerate(timePoints):            
            timePoints[i] = int(t[:2]) * 60 + int(t[3:])
        timePoints.sort()
        
        ans = float('inf')
        prev = 0
        for curr in range(1, len(timePoints)):
            diff = timePoints[curr] - timePoints[prev]
            ans = min(ans, diff)
            prev = curr
        ans = min(ans, timePoints[-1] - timePoints[0], abs(1440 - (timePoints[-1] - timePoints[0])))
        return ans