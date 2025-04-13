from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        h = []
        for k, v in count.items():
            heapq.heappush(h, (-v, k))
        
        res = ''
        while h:
            v, ch = heapq.heappop(h)
            res += ch * (-v)
        return res