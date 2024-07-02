from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gleft, sleft = 0, 0

        while sleft < len(s) and gleft < len(g):
            if s[sleft] >= g[gleft]:
                gleft += 1
            sleft += 1
        return gleft