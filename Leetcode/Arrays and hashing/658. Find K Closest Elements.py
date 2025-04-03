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

class Solution: # O(n) two pointer solution
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l, r = 0, len(arr)-1
        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l:r+1]