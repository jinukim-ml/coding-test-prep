import heapq

class Solution:
    def maxProduct(self, n: int) -> int:
        h = []
        while n > 0:
            n, r =  divmod(n, 10)
            heapq.heappush(h, -r)

        a = -heapq.heappop(h)
        b = -heapq.heappop(h)
        return a*b