from math import ceil
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        plength = len(potions)
        res = []
        for s in spells:
            target = ceil(success/s)
            index = bisect_left(potions, target)
            res.append(plength - index)
        return res