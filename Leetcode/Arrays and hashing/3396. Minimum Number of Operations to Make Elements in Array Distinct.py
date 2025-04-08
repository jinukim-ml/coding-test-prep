from collections import Counter

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        counter = Counter(nums)
        res = 0
        i = 0
        while i < len(nums) and len(counter.keys()) < len(nums) - i:
            j = 0
            while i < len(nums) and j < 3:
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    counter.pop(nums[i])
                i += 1
                j += 1
            res += 1
        return res