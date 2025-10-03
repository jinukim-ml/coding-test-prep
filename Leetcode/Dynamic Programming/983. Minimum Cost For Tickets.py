class Solution: # top-down solution
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = {len(days): 0}
        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            
            res = float('inf')
            j = i
            for cost, duration in zip(costs, [1,7,30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                res = min(res, cost + dfs(j))
            dp[i] = res
            return res
        return dfs(0)

class Solution: # bottom-up solution
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0 for _ in range(len(days)+1)]
        for i in range(len(days)-1, -1, -1):
            j = i
            dp[i] = float('inf')
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])
        return dp[0]