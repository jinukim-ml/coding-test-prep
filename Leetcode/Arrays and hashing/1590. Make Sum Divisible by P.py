class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        prefix = []
        total = 0
        for n in nums:
            total = (total + n) % p
        
        target = total % p
        if target == 0:
            return 0
        
        hashmap = {0: -1}

        curr, ans = 0, len(nums)
        
        for i in range(len(nums)):
            curr = (curr + nums[i]) % p

            key = (curr - target) % p
            if (curr - target) % p in hashmap:
                ans = min(ans, i - hashmap[key])
            hashmap[curr] = i
        
        if ans == len(nums):
            return -1
        else:
            return ans