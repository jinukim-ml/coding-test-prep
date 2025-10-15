class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)

        prefix = [1 for _ in range(n)]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                prefix[i] = prefix[i-1]+1

        def is_valid(k):
            for i in range(n-2*k+1):
                if prefix[i+k-1] >= k and prefix[i+2*k-1] >= k:
                    return True
            return False
        
        l, r = 1, n//2
        res = 0
        while l <= r:
            k = (l+r)//2
            if is_valid(k):
                l = k+1
                res = k
            else:
                r = k-1
        return res