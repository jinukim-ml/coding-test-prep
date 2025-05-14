class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing, decreasing = False, False
        for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    increasing = True
                elif nums[i] < nums[i-1]:
                    decreasing = True
                if increasing and decreasing:
                    return False
        return True