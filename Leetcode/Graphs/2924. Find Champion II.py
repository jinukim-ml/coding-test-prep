class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        degrees = [0] * n
        for u, v in edges:
            degrees[v] += 1
        
        ans, cnt = -1, 0
        for node in range(n):
            if degrees[node] == 0:
                cnt += 1
                ans = node
        
        if cnt == 1:
            return ans
        else:
            return -1