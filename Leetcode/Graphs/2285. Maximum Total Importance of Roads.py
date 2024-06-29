from typing import List
from collections import defaultdict
import heapq

class Solution: # optimized solution
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for st, de in roads:
            degrees[st] += 1
            degrees[de] += 1
        degrees.sort()
        
        ans = 0
        for i in range(1, n+1):
            ans += i * degrees[i-1]
        return ans

class Solution: # naive solution
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for st, de in roads:
            graph[st].append(de)
            graph[de].append(st)
        
        h = []
        for v in graph.keys():
            heapq.heappush(h, (-len(graph[v]), v))
        
        importance = {}
        i = n
        while h:
            _, v = heapq.heappop(h)
            importance[v] = i
            i -= 1

        ans = 0
        for st, de in roads:
            ans += importance[st] + importance[de]

        return ans