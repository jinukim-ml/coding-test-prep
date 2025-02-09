from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        cnt = defaultdict(int)
        for i, n in enumerate(nums):
            cnt[n-i] += 1
        
        res = 0
        for i, n in enumerate(nums):
            val = n - i
            cnt[val] -= 1
            num_match = len(nums) - i - 1 - cnt[val] # the number of the rest of the elements
            if num_match > 0:
                res += num_match
        return res