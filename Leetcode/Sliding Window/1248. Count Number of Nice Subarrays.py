from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        
        prefix = [0] * (len(nums) + 1)
        prefix[0] = 1
        s, ans = 0, 0

        for n in nums:
            s += n
            if s >= k:
                ans += prefix[s - k]
            prefix[s] += 1
        return ans