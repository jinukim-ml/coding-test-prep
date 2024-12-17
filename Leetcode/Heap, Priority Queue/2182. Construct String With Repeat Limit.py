from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        h = []
        for ch, cnt in Counter(s).items():
            heapq.heappush(h, (-ord(ch), cnt))
        res = ''
        while h:
            neg_ch, cnt = heapq.heappop(h)
            ch = chr(-neg_ch)
            i = 0
            while cnt > 0 and i < repeatLimit:
                res += ch
                cnt -= 1
                i += 1
            
            if h and cnt > 0:
                neg_ch2, cnt2 = heapq.heappop(h)
                res += chr(-neg_ch2)
                cnt2 -= 1
                if cnt2 > 0:
                    heapq.heappush(h, (neg_ch2, cnt2))
                heapq.heappush(h, (neg_ch, cnt))
        return res