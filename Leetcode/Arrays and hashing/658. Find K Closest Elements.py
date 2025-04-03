import heapq

class Solution: # O(n log n) solution using min heap
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        res = []
        h = []
        for i in range(len(arr)):
            heapq.heappush(h, (abs(arr[i] - x), i))
        
        for _ in range(k):
            _, i = heapq.heappop(h)
            res.append(arr[i])
        return sorted(res)