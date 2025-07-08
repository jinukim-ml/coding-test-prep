from bisect import bisect_right

class Solution: # top-down
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort()
        dp = [[-1 for _ in range(k+1)] for __ in range(len(events))]
        start_days = [e[0] for e in events]
        def dfs(i: int, remaining: int) -> int:
            if i == len(events) or remaining == 0:
                return 0
            if dp[i][remaining] != -1:
                return dp[i][remaining]
            
            skip = dfs(i+1, remaining)
            j = bisect_right(start_days, events[i][1])
            pick = events[i][2] + dfs(j ,remaining-1)

            val = max(skip, pick)
            dp[i][remaining] = val
            return val
        
        return dfs(0, k)

class Solution: # bottom-up
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort()
        start_days = [e[0] for e in events]
        n = len(events)
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(1, k+1):
                skip = dp[i+1][j]
                next_index = bisect_right(start_days, events[i][1])
                pick = events[i][2] + dp[next_index][j-1]
            
                dp[i][j] = max(skip, pick)
        return dp[0][k]