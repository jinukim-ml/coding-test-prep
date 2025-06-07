import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        h = []
        for i, ch in enumerate(s):
            if ch != '*':
                heapq.heappush(h, (ch, -i))
            else:
                s[i] = '!'
                _, idx = heapq.heappop(h)
                idx *= -1
                s[idx] = '!'
        
        res = ''
        for ch in s:
            if ch != '!':
                res += ch
        return res