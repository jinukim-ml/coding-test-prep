class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        self.nums = nums
        ans = 0

        for i in range(len(nums)):
            left = self.binary_search(i+1, len(nums)-1, lower - nums[i])
            right = self.binary_search(i+1, len(nums)-1, upper - nums[i] + 1)
            ans += right - left
        return ans
    
    def binary_search(self, l: int, r: int, target: int) -> int:
        while l <= r:
            mid = (l + r) // 2
            if self.nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l