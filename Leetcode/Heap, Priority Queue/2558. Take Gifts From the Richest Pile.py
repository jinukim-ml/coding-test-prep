import heapq

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        h = []
        for g in gifts:
            heapq.heappush(h, -g)
        for _ in range(k):
            g = -heapq.heappop(h)
            g = -int(g ** 0.5)
            heapq.heappush(h, g)
        return -1 * sum(h)