class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        prefix = []
        running_sum = 0
        for n in nums:
            running_sum += n
            prefix.append(running_sum)
        
        res = 0
        for i in range(len(nums)-1):
            if prefix[i] >= prefix[-1] - prefix[i]:
                res += 1
        return res

class Solution: # a little more memory efficient way
    def waysToSplitArray(self, nums: list[int]) -> int:
        total = sum(nums)
        running_sum = 0
        res = 0
        for i in range(len(nums)-1):
            running_sum += nums[i]
            if running_sum >= total - running_sum:
                res += 1
        return res