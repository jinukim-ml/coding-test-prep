class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        l, res = 0, 0
        window = 0
        for r in range(len(fruits)):
            window += fruits[r][1]
            while fruits[r][0] - fruits[l][0] + min(abs(startPos - fruits[l][0]), abs(fruits[r][0] - startPos)) > k:
                window -= fruits[l][1]
                l += 1
                if l > r:
                    break
            res = max(res, window)
        return res

from bisect import bisect_left, bisect_right

class Solution: # binary search + sliding window
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        l = bisect_left(fruits, [startPos-k, float('-inf')])
        r = bisect_right(fruits, [startPos, float('inf')])
        
        window = 0
        for i in range(l, r):
            window += fruits[i][1]
        res = window
        
        for i in range(r, len(fruits)):
            curr_pos = fruits[i][0]
            if curr_pos - startPos > k:
                break
            
            window += fruits[i][1]
            while curr_pos - fruits[l][0] + min(abs(startPos - fruits[l][0]), curr_pos - startPos) > k:
                window -= fruits[l][1]
                l += 1
            res = max(res, window)
        return res