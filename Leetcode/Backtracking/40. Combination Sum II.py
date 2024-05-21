from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans, subarray = [], []
        def backtrack(i: int, val: int):
            if val == target:
                ans.append(subarray[:])
                return
            
            if i == len(candidates):
                return
            
            if target < val + candidates[i]:
                return
            
            subarray.append(candidates[i])
            backtrack(i+1, val+candidates[i])

            subarray.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, val)
        
        backtrack(0, 0)
        return ans