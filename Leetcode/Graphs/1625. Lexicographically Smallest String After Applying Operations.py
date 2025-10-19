from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def op1(s: str) -> str:
            res = ''
            for i, ch in enumerate(s):
                if i%2:
                    val = int(ch) + a
                    if val > 9:
                        val -= 10
                    res += str(val)
                else:
                    res += ch
            return res
        
        def op2(s: str) -> str:
            return s[-b:] + s[:-b]
        
        res = '9' * len(s)
        seen = set()
        q = deque([s])
        while q:
            t = q.popleft()
            res = min(res, t)
            o1 = op1(t)
            if o1 not in seen:
                seen.add(o1)
                q.append(o1)
            o2 = op2(t)
            if o2 not in seen:
                seen.add(o2)
                q.append(o2)
        return res