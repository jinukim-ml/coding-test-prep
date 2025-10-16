from collections import Counter

class Solution: # naive implementation O(n+MEX)
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        for i in range(len(nums)):
            nums[i] %= value
        freq = Counter(nums)
        key, expected = 0, 0
        while freq[key]:
            freq[key] -= 1
            expected += 1
            key = (key+1)%value
        return expected

class Solution: # more optimized O(n+value)
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        n = len(nums)
        mods = [0 for _ in range(value)]
        for x in nums:
            mods[x%value] += 1
        
        idx, min_mod = n+1, n+1
        for i, m in enumerate(mods):
            if m < min_mod:
                idx = i
                min_mod = m
        return min_mod * value + idx