from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        h, v = 0, 0
        hcnt, vcnt = 1, 1
        ans = 0

        while h < m-1 and v < n-1:
            if horizontalCut[h] >= verticalCut[v]:
                ans += horizontalCut[h] * vcnt
                hcnt += 1
                h += 1
            else:
                ans += verticalCut[v] * hcnt
                vcnt += 1
                v += 1
        
        while h < m-1:
            ans += horizontalCut[h] * vcnt
            hcnt += 1
            h += 1
        
        while v < n-1:
            ans += verticalCut[v] * hcnt
            vcnt += 1
            v += 1
        
        return ans