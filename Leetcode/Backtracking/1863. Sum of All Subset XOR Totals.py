from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(idx: int, val: int):
            if idx == len(nums):
                return val
            
            return dfs(idx+1, val^nums[idx]) + dfs(idx+1, val)
        
        return dfs(0, 0)