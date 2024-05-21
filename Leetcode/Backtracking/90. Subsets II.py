from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        subarray = []
        def backtrack(idx):
            if idx == len(nums):
                ans.append(subarray[:])
                return
            
            subarray.append(nums[idx])
            backtrack(idx+1)

            subarray.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            backtrack(idx+1)
        
        backtrack(0)
        return ans