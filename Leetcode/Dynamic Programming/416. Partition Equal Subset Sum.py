from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2:
            return False

        dp = set([0])
        target //= 2

        for i in range(len(nums)-1, -1, -1):
            nextdp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextdp.add(t + nums[i])
                nextdp.add(t)
            dp = nextdp
        return False