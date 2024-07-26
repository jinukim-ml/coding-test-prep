class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        mat = [[float('inf') for __ in range(n)] for _ in range(n)]
        for d in range(n): # diagonals
            mat[d][d] = 0

        for u, v, w in edges: # bidirectional graph
            mat[u][v] = w
            mat[v][u] = w

        for k in range(n): # Floyd-Warshall algorithm
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

        ans, num_cities = -1, float('inf')
        for i in range(n):
            cnt = 0
            for j in range(n):
                if mat[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= num_cities:
                num_cities = cnt
                ans = i
        return ans