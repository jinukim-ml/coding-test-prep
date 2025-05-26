from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        g = defaultdict(list)
        indegrees = [0] * n
        for u, v in edges:
            g[u].append(v)
            indegrees[v] += 1
        
        q = deque()
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)

        res, visited = 0, 0
        dp = [[0 for _ in range(26)] for _ in range(n)]
        while q:
            node = q.popleft()
            visited += 1
            c = ord(colors[node]) - 97
            dp[node][c] += 1
            res = max(res, dp[node][c])

            for v in g[node]:
                for c in range(26):
                    dp[v][c] = max(dp[v][c], dp[node][c])
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        
        if visited == n:
            return res
        else:
            return -1