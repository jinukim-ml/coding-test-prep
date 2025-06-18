class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []
        l = 0
        while l < n:
            r = l + 2
            if nums[r] - nums[l] > k:
                return []
            res.append(nums[l:r+1])
            l = r+1
        return res