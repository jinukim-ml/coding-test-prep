class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        res = []
        l = 0
        for i in range(n):
            if nums[i] == key:
                l = max(l, i-k)
                r = min(n-1, i+k)
                while l <= r:
                    res.append(l)
                    l += 1
        return res