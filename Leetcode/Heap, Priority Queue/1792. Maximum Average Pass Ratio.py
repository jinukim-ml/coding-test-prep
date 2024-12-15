import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        h = []
        for p, t in classes:
            increment = (p+1)/(t+1) - p/t
            heapq.heappush(h, (-increment, p, t))
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(h)
            p += 1
            t += 1
            increment = (p+1)/(t+1) - p/t
            heapq.heappush(h, (-increment, p, t))
        
        res = 0
        for _, p, t in h:
            res += p/t
        return res/len(classes)