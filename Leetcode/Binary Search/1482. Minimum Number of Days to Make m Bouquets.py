from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def is_possible(d):
            cnt, num_bou = 0, 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= d:
                    cnt += 1
                    if cnt == k:
                        num_bou += 1
                        cnt = 0
                else:
                    cnt = 0
                if num_bou >= m:
                    return True
            return False

        l, r = float('inf'), float('-inf')
        for val in bloomDay:
            if val < l:
                l = val
            if val > r:
                r = val
        
        while l < r:
            mid = (l + r) // 2
            if is_possible(mid):
                r = mid
            else:
                l = mid +1
        return l