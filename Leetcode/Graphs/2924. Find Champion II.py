class Solution: # Second solution. A little bit faster than the first one. O(n)
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        nodes = set([node for node in range(n)])
        for u, v in edges:
            nodes.discard(v)
        
        if len(nodes) == 1:
            return nodes.pop()
        else:
            return -1

class Solution: # First solution. O(n)
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