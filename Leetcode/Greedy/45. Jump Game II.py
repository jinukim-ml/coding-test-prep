from typing import List

class Solution: # faster solution
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

class Solution: # traverse from behind
    def jump(self, nums: List[int]) -> int:
        i = len(nums)-1
        ans = 0
        while i > 0:
            idx = float('inf')
            for j in range(i-1, -1, -1):
                if j + nums[j] >= i and j < idx:
                    idx = j
            
            ans += 1
            i = idx
        return ans