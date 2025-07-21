import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        h = []
        for ch, v in Counter(s).items():
            heapq.heappush(h, (-v, ch))
        res = ''
        
        while h:
            if res:
                if res[-1] != h[0][1]:
                    neg_cnt, ch = heapq.heappop(h)
                    res += ch
                    if neg_cnt < -1:
                        heapq.heappush(h, (neg_cnt+1, ch))
                else:
                    temp_cnt, temp_ch = heapq.heappop(h)
                    if not h:
                        return ''
                    else:
                        neg_cnt, ch = heapq.heappop(h)
                        res += ch
                        if neg_cnt < -1:
                            heapq.heappush(h, (neg_cnt+1, ch))
                        heapq.heappush(h, (temp_cnt, temp_ch))
            else:
                neg_cnt, ch = heapq.heappop(h)
                res += ch
                if neg_cnt < -1:
                    heapq.heappush(h, (neg_cnt+1, ch))
        return res