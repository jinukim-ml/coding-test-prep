class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        target = max(nums)
        cnt = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == target:
                cnt += 1
            while cnt == k:
                if nums[l] == target:
                    cnt -= 1
                res += len(nums) - r
                l += 1
        return res