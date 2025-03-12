from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        def count_negatives() -> int:
            if nums[0] >= 0:
                return 0
            return bisect_left(nums, 0)
        def count_positives() -> int:
            if nums[-1] <= 0:
                return 0
            idx = bisect_right(nums, 0)
            return len(nums) - idx
        
        negatives = count_negatives()
        positives = count_positives()
        return max(negatives, positives)