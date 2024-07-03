from typing import List
import heapq

class Solution: # Time complexity: O(n)
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        smallest = sorted(heapq.nsmallest(4, nums))
        largest = sorted(heapq.nlargest(4, nums))
        ans = float('inf')
        for i in range(4):
            ans = min(ans, largest[i] - smallest[i])
        return ans

class Solution: # Sort + backtracking (exhaustive search). Time complexity: O(nlogn)
    def minDifference(self, nums: List[int]) -> int:
        def dfs(l:int, r:int, cnt:int) -> int:
            if cnt == 3:
                return nums[r] - nums[l]
            cnt += 1
            return min(dfs(l+1, r, cnt), dfs(l, r-1, cnt))

        if len(nums) <= 4:
            return 0
        
        nums.sort()
        return dfs(0, len(nums)-1, 0)