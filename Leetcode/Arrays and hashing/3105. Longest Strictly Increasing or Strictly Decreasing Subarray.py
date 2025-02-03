class Solution: # time complexity: O(n), space complexity: O(1)
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing = []
        decreasing = []
        res = 0
        for n in nums:
            if not increasing or increasing[-1] < n:
                increasing.append(n)
            else:
                increasing = [n]
            if not decreasing or decreasing[-1] > n:
                decreasing.append(n)
            else:
                decreasing = [n]
            res = max(res, len(increasing), len(decreasing))
        return res

class Solution: # time complexity: O(n), space complexity: O(1)
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing = 1
        decreasing = 1
        res = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                increasing += 1
                decreasing = 1
            elif nums[i] > nums[i+1]:
                increasing = 1
                decreasing += 1
            else:
                increasing = 1
                decreasing = 1
            res = max(res, increasing, decreasing)
        return res