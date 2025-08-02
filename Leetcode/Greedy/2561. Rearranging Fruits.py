from collections import Counter

class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter(basket2)
        cnt_all = cnt1 + cnt2
        for k in cnt_all:
            if cnt_all[k]%2:
                return -1
        min_cost = 2*min(min(basket1), min(basket2))
        
        swaps = []
        for k in cnt1:
            diff = cnt1[k] - cnt_all[k]//2
            for _ in range(diff):
                swaps.append(k)
        for k in cnt2:
            diff = cnt2[k] - cnt_all[k]//2
            for _ in range(diff):
                swaps.append(k)
        
        swaps.sort()
        res = 0
        for i in range(len(swaps)//2):
            res += min(swaps[i], min_cost)
        return res