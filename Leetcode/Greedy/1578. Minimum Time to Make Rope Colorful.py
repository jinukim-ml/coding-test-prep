class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n = len(colors)
        i, res = 0, 0
        while i < n:
            j = i
            maxval, total = 0, 0
            while j < n and colors[j] == colors[i]:
                maxval = max(maxval, neededTime[j])
                total += neededTime[j]
                j += 1
            if j > i+1:
                res += total - maxval
            i = j
        return res
    
class Solution: # more readable revision
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                res += min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        return res