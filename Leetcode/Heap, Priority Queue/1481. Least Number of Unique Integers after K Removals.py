from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freq = Counter(arr)
        h = []
        for key, val in freq.items():
            heapq.heappush(h, (val, key))
        
        for _ in range(k):
            val, key = heapq.heappop(h)
            val -= 1
            if val == 0:
                freq.pop(key)
            else:
                heapq.heappush(h, (val, key))
        return len(freq)