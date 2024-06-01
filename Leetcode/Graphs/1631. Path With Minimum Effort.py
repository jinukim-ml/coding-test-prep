from typing import List
import heapq

"""
Dijkstra's algorithm
"""

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        dist = [[float('inf') for _ in range(len(heights[0]))] for __ in range(len(heights))]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        
        while heap:
            effort, r, c = heapq.heappop(heap)

            if r == len(heights)-1 and c == len(heights[0])-1:
                return effort
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))