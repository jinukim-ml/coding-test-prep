from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ans = 0
        vis = {}
        def backtrack(i, length):
            nonlocal ans
            if i == len(nums):
                if length > 0:
                    ans += 1
                return

            if nums[i] - k in vis and vis[nums[i]-k]:
                backtrack(i+1, length)
            else:
                if nums[i] not in vis:
                    vis[nums[i]] = set([i])
                else:
                    vis[nums[i]].add(i)
                backtrack(i+1, length+1)
                vis[nums[i]].remove(i)

                backtrack(i+1, length)

        backtrack(0, 0)
        return ans