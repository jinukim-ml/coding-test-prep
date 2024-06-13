from typing import List

class Solution: # Top-down solution
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)] = 0
            for i in range(l,r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l, r)]
            
        return dfs(1, len(nums)-2)
    
class Solution: # Bottom-up solution
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1] # nums = [1] + [x for x in nums if x != 0] + [1] for a little bit of performance boost

        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                    cache[(left, right)] = max(coins, cache.get((left, right), 0))
        return cache.get((0, len(nums) - 1), 0)