class Solution: # O(n^2)
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        length = len(nums)
        lis = [1] * length
        lds = [1] * length

        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        for i in range(length-1, -1, -1):
            for j in range(i+1, length):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        ans = float('inf')
        for i in range(length):
            if lis[i] > 1 and lds[i] > 1:
                ans = min(ans, length - lis[i] - lds[i] + 1)
        return ans