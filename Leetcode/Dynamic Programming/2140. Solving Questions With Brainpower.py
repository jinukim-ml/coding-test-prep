class Solution: # recursive DP. O(n)
    def mostPoints(self, questions: list[list[int]]) -> int:
        dp = {}
        def dfs(i: int) -> int:
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]
            points, brainpower = questions[i]
            taken = points + dfs(i + brainpower + 1)
            skipped = dfs(i+1)
            dp[i] =  max(taken, skipped)
            return dp[i]
        dfs(0)
        return dp[0]

class Solution: # iterative DP. same O(n) but faster than the recursive solution
    def mostPoints(self, questions: list[list[int]]) -> int:
        dp = [0] * len(questions)
        prev = questions[-1][0]
        for i in range(len(questions)-1, -1, -1):
            points, brainpower = questions[i]
            j = i + brainpower + 1
            if j < len(questions):
                points += dp[j]
            dp[i] = max(prev, points)
            prev = dp[i]
        return dp[0]